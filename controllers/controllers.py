# -*- coding: utf-8 -*-
# from odoo import http


# class ConvalidacionesApp(http.Controller):
#     @http.route('/convalidaciones_app/convalidaciones_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/convalidaciones_app/convalidaciones_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('convalidaciones_app.listing', {
#             'root': '/convalidaciones_app/convalidaciones_app',
#             'objects': http.request.env['convalidaciones_app.convalidaciones_app'].search([]),
#         })

#     @http.route('/convalidaciones_app/convalidaciones_app/objects/<model("convalidaciones_app.convalidaciones_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('convalidaciones_app.object', {
#             'object': obj
#         })
