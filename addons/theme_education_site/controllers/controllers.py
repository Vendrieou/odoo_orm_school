# -*- coding: utf-8 -*-
# from odoo import http


# class ThemeEducationSite(http.Controller):
#     @http.route('/theme_education_site/theme_education_site/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/theme_education_site/theme_education_site/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('theme_education_site.listing', {
#             'root': '/theme_education_site/theme_education_site',
#             'objects': http.request.env['theme_education_site.theme_education_site'].search([]),
#         })

#     @http.route('/theme_education_site/theme_education_site/objects/<model("theme_education_site.theme_education_site"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('theme_education_site.object', {
#             'object': obj
#         })
