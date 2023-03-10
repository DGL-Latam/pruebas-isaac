# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.tools import date_utils
import datetime

today = fields.Date.today()
three_months = date_utils.add(today, months=3)

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property Plans"

    name = fields.Char("Title", required=True)
    description = fields.Text("Description")
    postcode = fields.Char("Postcode")
    date_availability = fields.Date("Available From", default=three_months, required=True, copy=False)
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", required=True, readonly=False, copy=False)
    bedrooms = fields.Integer("Bedrooms", default =2)
    living_areas = fields.Integer("Living Area (sqm)")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden area")
    garden_orientation = fields.Selection(string="Garden Orientation", selection =[("north", "North"), ("south", "South"), ("east", "East"), ("west", "West")])

    state = fields.Selection(string="Status", selection=[("new", "New"), ("offerReceived", "Offer Received"),
                                                         ("offeraccepted", "Offer Accepted"), ("sold", "Sold"),
                                                         ("canceled", "Canceled")], default="new", required=True,
                             copy=False)

    active = fields.Boolean("Active", default=True)

    property_type_id = fields.Many2one("estate.property.type", string="Property Type")

    user_id = fields.Many2one("res.users", string="Salesperson", index=True, tracking=True, default=lambda self: self.env.user)
    partner_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    tag_ids = fields.Many2many("estate.property.tag")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offer")

    # Computed fields
    total_area = fields.Integer(compute="_compute_total_area")
    best_offer = fields.Float(compute="_compute_best_offer")

    @api.depends("living_areas", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_areas + record.garden_area

    add_offer = fields.Integer(default=0)
    @api.depends("offer_ids.price", "add_offer")
    def _compute_best_offer(self):
        for record in self:
            record.add_offer = sum(record.mapped("offer_ids.price"))
        if record.add_offer > 0:
            record.best_offer = max(record.mapped("offer_ids.price"))
        else:
            record.best_offer = 0
class EstatePropertyType(models.Model):
    _name = "estate.property.type"

    name = fields.Char("Property Type", required=True)

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"

    name = fields.Char("Property Tag", required=True)

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"

    price = fields.Float("Price")
    status = fields.Selection(string="Status", copy=False, selection=[("accepted", "Accepted"), ("refused", "Refused")])
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)


    validity = fields.Integer(string="Validity", default=7)
    date_deadline = fields.Date(compute="_computed_date_deadline", inverse="_inverse_validity", string="Deadline")

    @api.depends("create_date", "validity")
    def _computed_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + datetime.timedelta(days=record.validity)

    def _inverse_validity(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date).days
