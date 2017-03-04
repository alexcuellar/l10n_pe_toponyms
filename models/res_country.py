# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.addons.base.res.res_country import location_name_search

class CountryProvince(models.Model):
    _description = "Country Province"
    _name = 'res.country.province'
    _order = 'code'

    state_id = fields.Many2one('res.country.state', string='States', required=True)
    name = fields.Char(string='Province Name', required=True)
    code = fields.Char(string='Province Code', help='The province code.', required=True)

    name_search = location_name_search

    _sql_constraints = [
        ('name_code_uniq', 'unique(state_id, code)', 'The code of the province must be unique by country !')
    ]

class CountryDistrict(models.Model):
    _description = "Country District"
    _name = 'res.country.district'
    _order = 'code'

    province_id = fields.Many2one('res.country.province', string='Province', required=True)
    name = fields.Char(string='District Name', required=True)
    code = fields.Char(string='Province Code', help='The province code.', required=True)

    name_search = location_name_search

    _sql_constraints = [
        ('name_code_uniq', 'unique(province_id, code)', 'The code of the district must be unique by country !')
    ]
