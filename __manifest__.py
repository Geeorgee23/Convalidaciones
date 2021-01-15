# -*- coding: utf-8 -*-
{
    'name': "convalidaciones_app",

    'summary': """
        Aplicacion Convalidaciones
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Jorge Tarazona",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/alumnos_view.xml',
        'views/modulos_view.xml',
        'views/convalidaciones_view.xml',
        'views/ciclos_view.xml',
        'views/profesores_view.xml',
        'views/menu_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
    'installable': True,
}
