from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.depends('amount_total')
    def _compute_visible_amount_total(self):
        """Total visible basado en permisos"""
        for order in self:
            if self.env.user.has_group('control_costos_hexagonos.group_view_purchase_total'):
                order.visible_amount_total = order.amount_total
            else:
                order.visible_amount_total = 0.0

    visible_amount_total = fields.Monetary(
        'Total Visible',
        compute='_compute_visible_amount_total',
        help='Total de la orden (visible según permisos)'
    )

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    @api.depends('price_unit')
    def _compute_visible_price_unit(self):
        """Precio unitario visible basado en permisos"""
        for line in self:
            if self.env.user.has_group('control_costos_hexagonos.group_view_purchase_price'):
                line.visible_price_unit = line.price_unit
            else:
                line.visible_price_unit = 0.0

    @api.depends('price_subtotal')
    def _compute_visible_price_subtotal(self):
        """Subtotal visible basado en permisos"""
        for line in self:
            if self.env.user.has_group('control_costos_hexagonos.group_view_purchase_price'):
                line.visible_price_subtotal = line.price_subtotal
            else:
                line.visible_price_subtotal = 0.0

    visible_price_unit = fields.Float(
        'Precio Unit. Visible',
        compute='_compute_visible_price_unit',
        digits='Product Price'
    )
    
    visible_price_subtotal = fields.Monetary(
        'Subtotal Visible',
        compute='_compute_visible_price_subtotal'
    )
