# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
# How To Override Create Function in Odoo
# class ResPartners(models.Model):
#     _inherit = 'res.partner'

#     @api.model
#     def create(self, vals):
#         res = super(ResPartners, self).create(vals)
#         # do the custom code here
#         return res


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    patient_name = fields.Char(string="Patient Name")



class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = 'mail.thread', 'mail.activity.mixin'
    _description = 'Patient Record'
    _rec_name = "patient_name"


    # #TODO this method used to get patient {sequence + name} when i search in new appointment
    # @api.multi
    # def name_get(self):
    #     res = []
    #     for rec in self:
    #         res.append((rec.id, '%s - %s' % (rec.name_seq, rec.patient_name)))
    #     return res

    #TODO this method used to run the scheduled cron.xml file in data folder [SCHEDULED ACTION]
    @api.model
    def test_cron_job(self):
        print("ABCD")
        #code acccordingly to execute the cron


    #TODO get all doctors from Doctors module names in this field
    doctor_id = fields.Many2one('hospital.doctor', string='Doctors', required=True)

    #TODO get all users from users module to this field
    user_id = fields.Many2one('res.users', string='Related User')

    patient_name = fields.Char(string="Patient Name", required=True)
    patient_number = fields.Char('Contact Number')
    patient_email = fields.Char('Email')
    patient_age = fields.Integer('Patient Age')
    patient_notes = fields.Text(string="Registration Note")
    patient_image = fields.Binary(string="Patient Image", attachment=True)
    active = fields.Boolean('Active', default=True)
    # this object to choose gender
    gender = fields.Selection([
        ('male', 'Male'),
        ('fe_male', 'Female')
    ], default='male', string="Gender")
    age_group = fields.Selection([
        ('major', 'Major'),
        ('minor', 'Minor')
    ], string="Age Group", compute='set_age_group')

    #TODO this object used in sequence
    name_seq = fields.Char(string='Patient ID', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))

    #TODO method to create sequence
    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result

    #TODO method used to open appointment of patient when click the smart button
    @api.multi
    def open_patient_appointment(self):
        return {
            'name': _('Appointment'),
            'domain': [('patient_id', '=', self.id)],
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'hospital.appointment',
            'view_id': False,
            'type': 'ir.actions.act_window',
        }

    #TODO object used in appointment count of patient
    appointment_count = fields.Integer(string="Appointment", compute='get_appointment_count')

    #TODO method to get appointment count to patient
    def get_appointment_count(self):
        count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])
        self.appointment_count = count

    #TODO method to check patient age greater than 5 years or not
    @api.constrains('patient_age')
    def check_age(self):
        for rec in self:
            if rec.patient_age <= 5:
                raise ValidationError(_('The Age Must Be Greater Than 5 Years !'))

    #TODO method to check patient age greater than 18 years
    # and if yes set age_group value=minor
    # else set age_group value=major
    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self:
            if rec.patient_age:
                if rec.patient_age < 18:
                    rec.age_group = 'minor'
                else:
                    rec.age_group = 'major'

    #TODO method to SEND patient card
    def action_send_card(self):
        template_id = self.env.ref('hospital.patient_card_email_template').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)

    # TODO this method used to print patient report card
    @api.multi
    def print_report(self):
        return self.env.ref('hospital.action_report_patient_card') .report_action(self)