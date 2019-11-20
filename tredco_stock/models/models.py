# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError,ValidationError

class StockPickingCT(models.Model):
    _inherit = "stock.picking"

    @api.multi
    def button_validate(self):
        self.ensure_one()
        if self.picking_type_code != 'incoming' and not all(self.move_ids_without_package.mapped('quantity_done')):
            raise UserError(_('You are not allowed to continue because there is a quantity = 0.'))
        for move_id in self.move_ids_without_package:
            if move_id.product_uom_qty > move_id.reserved_availability:
                raise ValidationError(_('You are allowed to continue because there is not enough quantity in stock'))
        return super(StockPickingCT, self).button_validate()