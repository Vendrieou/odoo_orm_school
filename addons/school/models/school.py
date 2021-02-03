# -*- coding: utf-8 -*-

from odoo import models, fields, api


class school(models.Model):
    _name = 'school.profile'
    _description = 'school.school'

    name = fields.Char(string="School Name")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
