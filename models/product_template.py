from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.depends('standard_price')
    def _compute_visible_cost(self):
        """Calcula el costo visible basado en permisos del usuario"""
        for product in self:
            if self.env.user.has_group('control_costos_hexagonos.group_view_cost'):
                product.visible_standard_price = product.standard_price
            else:
                product.visible_standard_price = 0.0

    @api.depends('list_price')
    def _compute_visible_sale_price(self):
        """Calcula el precio de venta visible basado en permisos del usuario"""
        for product in self:
            if self.env.user.has_group('control_costos_hexagonos.group_view_sale_price'):
                product.visible_list_price = product.list_price
            else:
                product.visible_list_price = 0.0

    visible_standard_price = fields.Float(
        'Costo Visible',
        compute='_compute_visible_cost',
        digits='Product Price',
        help='Costo del producto (visible según permisos)'
    )
    
    visible_list_price = fields.Float(
        'Precio Venta Visible',
        compute='_compute_visible_sale_price',
        digits='Product Price',
        help='Precio de venta (visible según permisos)'
    )
