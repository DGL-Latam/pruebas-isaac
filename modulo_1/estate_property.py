# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property Plans"
    _order = "sequence"

    name = fields.Char("Plan", required=True, translate=True)
    number_of_months = fields.Integer("# Months", required=True)
    active = fields.Boolean("Active", default=True)
    sequence = fields.Integer("Sequence", default=10)

    _sql_constraints = [
        ("check_number_of_months", "CHECK(number_of_months >=0", "The number of month cannot be negative.")
    ]