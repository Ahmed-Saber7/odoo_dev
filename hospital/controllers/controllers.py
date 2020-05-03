# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Hospital(http.Controller):
    @http.route('/hospital/doctor/', website=True, auth='user')
    def hosptal_doctor(self, **kw):
        # return "hello, ahmed saber"
        patients = request.env['hospital.patient'].sudo().search([])
        return request.render('hospital.patients_page', {
            'patients': patients
        })

    # @http.route('/hospital/my_frist_module/', auth='public')
    # def index(self, **kw):
    #     return "Hello, world"
    #
    # @http.route('/hospital/my_frist_module/objects/', auth='public')
    # def list(self, **kw):
    #     return http.request.render('my_frist_module.listing', {
    #         'root': '/hospital/my_frist_module',
    #         'objects': http.request.env['hospital.my_frist_module'].search([]),
    #     })
    #
    # @http.route('/hospital/my_frist_module/objects/<model("hospital.my_frist_module"):obj>/',
    #             auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('hospital.object', {
    #         'object': obj
    #     })
