# -*- coding: utf-8 -*-

from openerp import api, fields, models

class Partner(models.Model):
    _inherit = 'res.partner'
    
    province_id = fields.Many2one('res.country.province', string='Province')
    district_id = fields.Many2one('res.country.district', string='District')

    @api.onchange('state_id')
    def _onchange_state_id(self):
        if self.state_id:
            if not self.country_id:
                self.country_id=self.state_id.country_id.id
    
    @api.onchange('province_id')
    def _onchange_province_id(self):
        if self.province_id:
            if not self.state_id:
                self.state_id=self.province_id.state_id.id
        
    @api.onchange('district_id')
    def _onchange_district_id(self):
        if self.district_id:
            if not self.province_id:
                self.province_id=self.district_id.province_id.id
        self.zip= self.district_id.code and self.district_id.code[2:] or False
        self.city = self.district_id.name 
