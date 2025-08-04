from odoo import models, fields, api

class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.depends('price_unit')
    def _compute_visible_price_unit(self):
        """Precio unitario visible en movimientos de stock"""
        for move in self:
            if self.env.user.has_group('control_costos_hexagonos.group_view_stock_cost'):
                move.visible_price_unit = move.price_unit
            else:
                move.visible_price_unit = 0.0

    visible_price_unit = fields.Float(
        'Costo Unit. Visible',
        compute='_compute_visible_price_unit',
        digits='Product Price',
        help='Costo unitario en movimiento (visible según permisos)'
    )
