from odoo import fields, models
from odoo.tools import date_utils

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"

    name = fields.Char("Title", requiered=True)
