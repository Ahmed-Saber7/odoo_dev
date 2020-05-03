# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class HospitalLab(models.Model):
    _name = 'hospital.lab'
    _inherit = 'mail.thread', 'mail.activity.mixin'
    _description = 'Patient Laboratory'


    name = fields.Char(string="Name", required=True)
    user_id = fields.Many2one('res.users', string="Responsible")

