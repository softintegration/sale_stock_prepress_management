# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    prepress_proof_id = fields.Many2one('prepress.proof', string='Prepress proof',related='move_id.prepress_proof_id')
    client_ref = fields.Char(string='Customer Prepress proof reference',related='prepress_proof_id.client_ref',)
