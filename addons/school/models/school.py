from odoo import models, fields


class school(models.Model):
    _name = 'school.profile'
    _description = 'school.description'

    name = fields.Char(string="School Name")
    email = fields.Char(string="Email")
    phone = fields.Char("Phone")
