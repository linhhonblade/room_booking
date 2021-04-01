# -*- coding: utf-8 -*-
{
    'name': "room_booking",

    'summary': """
        Book Meeting Room""",

    'description': """
        Allow user book meeting room fast and easily.
    """,

    'author': "AHT Jsc",
    'website': "https://arrowhitech.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity/Meeting',
    'version': '1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/room_booking_security.xml',
        'security/ir.model.access.csv',
        'views/room_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'qweb': [],
    'application': True,
    'installable': True
}
