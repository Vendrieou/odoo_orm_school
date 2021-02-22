# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class theme_vegetables_shop(models.Model):
#     _name = 'theme_vegetables_shop.theme_vegetables_shop'
#     _description = 'theme_vegetables_shop.theme_vegetables_shop'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
