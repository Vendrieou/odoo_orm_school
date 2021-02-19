# -*- coding: utf-8 -*-
from odoo import http


class WebsitePharmacy(http.Controller):
    @http.route('/website_pharmacy/website_pharmacy/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/website_pharmacy/website_pharmacy/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('website_pharmacy.listing', {
            'root': '/website_pharmacy/website_pharmacy',
            'objects': http.request.env['website_pharmacy.website_pharmacy'].search([]),
        })

    @http.route('/website_pharmacy/website_pharmacy/objects/<model("website_pharmacy.website_pharmacy"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('website_pharmacy.object', {
            'object': obj
        })
