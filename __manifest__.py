# -*- coding: utf-8 -*-
{
    'name': "l10n_pe_toponyms",

    'summary': """Peruvian toponyms""",

    'description': """
        Peruvian toponyms
	Lista de departamentos provincias y distritos peruanos
    """,

    'author': "Alexander Cuellar Morales",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Localization/Toponyms',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/pe_country_data.xml',
        'data/res_country_data.xml',
        'views/res_country_view.xml',
        'views/res_partner_view.xml',
        'views/res_company_view.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}
