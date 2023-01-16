# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

today = fields.Date.today()
class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property Plans"
    #_order = "sequence"

    name = fields.Char("Plan", required=True)
    description = fields.Text("Description")
    postcode = fields.Char("Postcode")
    date_availability = fields.Date("Date Availability", default =today, required=True, copy=False)
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", required=True, readonly=True, copy=False)
    bedrooms = fields.Integer("Bedrooms", default =2)
    living_areas = fields.Integer("Living Areas")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden area")
    garden_orientation = fields.Selection(string="Type", selection =[("north", "North"), ("south", "South"), ("east", "East"), ("west", "West")])
