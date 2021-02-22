# -*- coding: utf-8 -*-
# from odoo import http


# class ThemeVegetablesShop(http.Controller):
#     @http.route('/theme_vegetables_shop/theme_vegetables_shop/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/theme_vegetables_shop/theme_vegetables_shop/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('theme_vegetables_shop.listing', {
#             'root': '/theme_vegetables_shop/theme_vegetables_shop',
#             'objects': http.request.env['theme_vegetables_shop.theme_vegetables_shop'].search([]),
#         })

#     @http.route('/theme_vegetables_shop/theme_vegetables_shop/objects/<model("theme_vegetables_shop.theme_vegetables_shop"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('theme_vegetables_shop.object', {
#             'object': obj
#         })
