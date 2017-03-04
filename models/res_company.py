# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Company(models.Model):
    _inherit = 'res.company'
    
    province_id = fields.Many2one('res.country.province', compute='_compute_address', inverse='_inverse_province', string="Province")
    district_id = fields.Many2one('res.country.district', compute='_compute_address', inverse='_inverse_district', string="District")
    
    def _inverse_province(self):
        for company in self:
            company.partner_id.province_id = company.province_id
    
    def _inverse_district(self):
        for company in self:
            company.partner_id.district_id = company.district_id
    
    def _compute_address(self):
        super(Company, self)._compute_address()
        for company in self.filtered(lambda company: company.partner_id):
            address_data = company.partner_id.sudo().address_get(adr_pref=['contact'])
            if address_data['contact']:
                partner = company.partner_id.browse(address_data['contact'])
                company.province_id = partner.province_id.id
                company.district_id = partner.district_id.id
    
    @api.onchange('state_id')
    def _onchange_state_id(self):
        if self.state_id:
            if not self.country_id:
                self.country_id=self.state_id.country_id.id
            return {'domain': {'province_id': [('state_id', '=', self.state_id.id)]}}
        else:
            return {'domain': {'province_id': []}}
    
    
    @api.onchange('province_id')
    def _onchange_province_id(self):
        if self.province_id:
            if not self.state_id:
                self.state_id=self.province_id.state_id.id
            return {'domain': {'district_id': [('province_id', '=', self.province_id.id)]}}
        else:
            return {'domain': {'district_id': []}}
        
    @api.onchange('district_id')
    def _onchange_district_id(self):
        if self.district_id:
            if not self.province_id:
                self.province_id=self.district_id.province_id.id
        self.zip= self.district_id.code and self.district_id.code[2:] or False
        self.city = self.district_id.name 