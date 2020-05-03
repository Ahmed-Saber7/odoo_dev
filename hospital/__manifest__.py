# -*- coding: utf-8 -*-
{
    'name': "hospital new3",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ahmed Saber",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/sequence.xml',
        'data/mail_template.xml',
        'data/cron.xml',
        'reports/report.xml',
        'reports/appointment.xml',
        'reports/patient_card.xml',
        'wizards/create_appointment.xml',
        'views/patient.xml',
        'views/templates.xml',
        'views/appointment.xml',
        'views/doctor.xml',
        'views/lab.xml',
        'views/settings.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
