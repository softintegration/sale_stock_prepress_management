# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class StockMove(models.Model):
    _inherit = 'stock.move'

    prepress_proof_id = fields.Many2one('prepress.proof', string='Prepress proof',related='sale_line_id.prepress_proof_id',store=True)
    client_ref = fields.Char(string='Customer Prepress proof reference',related='prepress_proof_id.client_ref',)

    @api.onchange('product_id', 'picking_type_id')
    def _onchange_product_id(self):
        res = super(StockMove, self)._onchange_product_id()
        warning = self._update_prepress_proof()
        if warning:
            return warning
        return res

    def _update_prepress_proof(self):
        if not self.product_id:
            return
        prepress_proof = self.env['prepress.proof']._get_by_product(self.product_id)
        self.update({'prepress_proof_id': prepress_proof and prepress_proof.id or False})
        if prepress_proof.quarantined:
            warning = {
                'title': _("Warning"),
                'message': _(
                    "Prepress Proof %s has already been quarantined!"
                ) % prepress_proof.name,
            }
            return {'warning': warning}

