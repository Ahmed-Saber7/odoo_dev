# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = 'mail.thread', 'mail.activity.mixin'
    _description = 'Doctors'
    _rec_name = "doctor_name"


    doctor_name = fields.Char(string="Doctor Name")
    user_id = fields.Many2one('res.users', string='Related User', required=True)

    doctor_gender = fields.Selection([
        ('male', 'Male'),
        ('fe_male', 'Female')
    ], default='male', string="Gender")


