# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = 'mail.thread', 'mail.activity.mixin'
    _description = 'Appointment'
    _rec_name = "appointment_seq"
    # TODO create decrement order to field date
    _order = "appointment_date desc"

    # TODO set default name patient in appointment patient name by patient id
    def get_default_value(self):
        return 18

    # TODO How To Give Domain For A Field Based On Another Field
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        for rec in self:
            return {'domain': {'order_id': [('partner_id', '=', rec.partner_id.id)]}}

    # TODO this object used to get the all patient module fields
    patient_id = fields.Many2one('hospital.patient', string='Patient Name', required=True, default=get_default_value)
    # TODO this object used to get the patient age field from patient module and set in appointment
    patient_age = fields.Integer('Patient Age', related='patient_id.patient_age')
    # TODO this object used to get the patient number field from patient module and set in appointment
    patient_number = fields.Char('Contact Number', related='patient_id.patient_number')
    # TODO this object used to get the patient note field from patient module and set in appointment
    patient_notes = fields.Text("Registration Note", related='patient_id.patient_notes')
    # TODO this object used to get the patient image field from patient module and set in appointment
    patient_image = fields.Binary("Patient Image", related='patient_id.patient_image', attachment=True)

    name = fields.Char('Patient Name', related='patient_id.patient_name')

    partner_id = fields.Many2one('res.partner', string="Customer")
    order_id = fields.Many2one('sale.order', string="Sale Order")

    appointment_lines = fields.One2many('hospital.appointment.lines', 'appointment_id', string='Appointment Lines')
    appointment_notes = fields.Text(string="Appointment Note")

    # TODO get all doctors from Doctors module names in this field
    doctor_id = fields.Many2one('hospital.doctor', string='Doctors')

    appointment_date = fields.Date(string='Appointment Date', required=True)
    # TODO add state
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, default='draft')

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    # TODO this object used to get the sequence of patient and set in appointment
    patient_seq = fields.Char(string='Patient ID', related='patient_id.name_seq', required=True, copy=False,
                              readonly=True,
                              index=True, default=lambda self: _('New'))

    # TODO this object used in sequence
    appointment_seq = fields.Char(string='Appointment ID', required=True, copy=False, readonly=True,
                                  index=True, default=lambda self: _('New'))

    # TODO method to create sequence
    @api.model
    def create(self, vals):
        if vals.get('appointment_seq', _('New')) == _('New'):
            vals['appointment_seq'] = self.env['ir.sequence'].next_by_code('hospital.appointment.sequence') or _('New')
        result = super(HospitalAppointment, self).create(vals)
        return result


class HospitalAppointmentLines(models.Model):
    _name = 'hospital.appointment.lines'
    _description = 'Appointment Lines'
    product_id = fields.Many2one('product.product', string='Medicine')
    product_qty = fields.Integer(string='Quantity')
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment ID')

    #TODO Default Get Function: Set Default Values For Fields In Odoo
    # @api.model
    # def default_get(self, fields):
    #     res = super(HospitalAppointment, self).default_get(fields)
    #     res['patient_id'] =18
    #     return res