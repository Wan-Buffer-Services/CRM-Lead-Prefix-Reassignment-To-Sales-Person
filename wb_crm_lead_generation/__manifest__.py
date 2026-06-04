# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) Wan Buffer Solution (<https://wanbuffer.com/>).
#
#    For Module Support : info@wanbuffer.com  or Call : +91 9638442270
#
##############################################################################
# -*- coding: utf-8 -*-
{
    'name': 'CRM Lead Prefix & Reassignment To Sales Person',
    'version': '18.0.1.0.0',
    'author':'Wan Buffer Services',
    'category': 'Crm',
    'summary': 'Crm lead generation',
    'description': 'CRM lead generation',
    'website': 'https://wanbuffer.com',
    'depends': ['crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_view.xml',
        'wizard/wizard_view.xml',
        ],
    'images': ['static/description/banner.png',
        'static/description/icon.png'],

    'maintainer': 'Wan Buffer Services',
    'support': 'support@wanbuffer.com',
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
