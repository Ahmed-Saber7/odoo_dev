# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class CreateAppointment(models.TransientModel):
    _name = 'create.appointment'
    _description = "Create Appointment Wizard"

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    appointment_date = fields.Date(string="Appointment Date")

    # TODO this method used to print patient report card
    # https: // www.youtube.com / watch?v = NXWmBWgGVh8 & list = PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM & index = 76
    def print_report(self):
        data = {
            'model': 'create.appointment',
            'form': self.read()[0],
        }
        if data['form']['patient_id']:
            selected_patient = data['form']['patient_id'][0]
            appointments = self.env['hospital.appointment'].search([('patient_id', '=', selected_patient)])
        else:
            appointments = self.env['hospital.appointment'].search([])
        appointment_list = []
        for app in appointments:
            vals = {
                'patient_name': app.name,
                'appointment_notes': app.appointment_notes,
                'appointment_date': app.appointment_date
            }
            appointment_list.append(vals)
        # print("appointments", appointments)
        data['appointments'] = appointment_list
        # print("Data", data)

        return self.env.ref('hospital.report_appointment').report_action(self, data=data)

    # TODO this methid to create new appointment for patient and save it in appointment model
    def create_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'appointment_date': self.appointment_date,
        }
        self.patient_id.message_post(body="Appointment Created Successfully", subject="Appointment Creation")
        self.env['hospital.appointment'].create(vals)

    # TODO this method used to det data of patient
    def get_data(self):
        appointments = self.env['hospital.appointment'].search([])
        for rec in appointments:
            print("appointment name", rec.name)
        return {
            "type": "ir.actions.do_nothing"
        }

    # TODO this method used to delete patient from create appointment
    def delete_patient(self):
        for rec in self:
            rec.patient_id.unlik()
