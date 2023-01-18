# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.tools import date_utils
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

    property_type = fields.Many2one("estate.property.type", string="Property Types")

class EstatePropertyType(models.Model):
    _name = "estate.property.type"

    name = fields.Char("Property Types", required=True)