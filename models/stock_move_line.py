# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    prepress_proof_id = fields.Many2one('prepress.proof', string='Prepress proof',related='move_id.prepress_proof_id')
    client_ref = fields.Char(string='Customer Prepress proof reference',related='prepress_proof_id.client_ref',)

    def _get_aggregated_product_quantities(self, **kwargs):
        aggregated_move_lines = super()._get_aggregated_product_quantities(**kwargs)
        for key,aggr_move_line in aggregated_move_lines.items():
            product_id = key.split("_")[0]
            move_line = self.filtered(lambda ml:ml.product_id.id == int(product_id))
            aggr_move_line.update({'prepress_proof_id':move_line[0].prepress_proof_id.name,
                                   'client_ref':move_line[0].client_ref,
                                   'picking_type_code':move_line[0].picking_id.picking_type_code})
        return aggregated_move_lines
