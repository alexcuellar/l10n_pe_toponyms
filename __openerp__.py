# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 Cubic ERP - Teradata SAC (<http://cubicerp.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Perú Localización - Topónimos",
    "version": "1.0",
    "author": "Cubic ERP",
    "website": "http://cubicERP.com",
    "category": "Localization",
    'summary': """Peruvian toponyms""",
    'description': """
        Peruvian toponyms
    Lista de departamentos provincias y distritos peruanos
    """,
    "depends": ["base"],
    "data": [
        'security/ir.model.access.csv',
        'data/pe_country_data.xml',
        'data/res_country_data.xml',
        'views/res_country_view.xml',
        'views/res_partner_view.xml',
        'views/res_company_view.xml',
        ],
    'installable': True,
    'active': False,
}
