# -*- coding: utf-8 -*-

from openerp import fields, models

class CountryState(models.Model):
    _inherit = 'res.country.state'
    
    code = fields.Char('State Code', size=8, help='The state code in max. 8 chars.', required=True)


class CountryProvince(models.Model):
    _description = "Country Province"
    _name = 'res.country.province'
    _order = 'code'

    state_id = fields.Many2one('res.country.state', string='States', required=True)
    name = fields.Char(string='Province Name', required=True)
    code = fields.Char(string='Province Code', size=8, help='The province code.', required=True)

    _sql_constraints = [
        ('name_code_uniq', 'unique(state_id, code)', 'The code of the province must be unique by country !')
    ]
    
    
class CountryDistrict(models.Model):
    _description = "Country District"
    _name = 'res.country.district'
    _order = 'code'

    province_id = fields.Many2one('res.country.province', string='Province', required=True)
    name = fields.Char(string='District Name', required=True)
    code = fields.Char(string='Province Code', size=8, help='The province code.', required=True)

    _sql_constraints = [
        ('name_code_uniq', 'unique(province_id, code)', 'The code of the district must be unique by country !')
    ]
