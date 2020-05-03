from odoo import models, api


class PatientCardReport(models.AbstractModel):
    _name = 'report.hospital.report_patient'
    _description = 'Patient Card Report'

    # TODO how to inherit and modify existing pdf report
    @api.model
    def get_report_values(self, docids, data=None):
        docs = self.env['hospital.patient'].browse(docids[0])
        appointments = self.env['hospital.appointment'].search([('patient_id', '=', docids[0])])
        appointment_list = []

        for app in appointments:
            vals = {
                'name': app.appointment_seq,
                'appointment_note': app.appointment_notes,
                'appointment_date': app.appointment_date,
            }
            appointment_list.append(vals)
        print("appintments_list", appointment_list)
        return {
            'doc_model': 'hospital.patient',
            'data': data,
            'docs': docs,
            'appointment_list': appointment_list,
        }
