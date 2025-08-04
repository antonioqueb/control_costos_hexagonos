-e ### ./data/cost_groups.xml
```
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data noupdate="1">
        <!-- Asignar grupos a usuarios administradores existentes -->
        <function model="res.users" name="write">
            <value eval="[ref('base.user_admin')]"/>
            <value eval="{'groups_id': [(4, ref('group_cost_admin'))]}"/>
        </function>
    </data>
</odoo>
```

-e ### ./models/product_template.py
```
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
```

-e ### ./models/purchase_order.py
```
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
```

-e ### ./models/sale_order.py
```
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.depends('amount_total')
    def _compute_visible_amount_total(self):
        """Total visible basado en permisos"""
        for order in self:
            if self.env.user.has_group('control_costos_hexagonos.group_view_sale_total'):
                order.visible_amount_total = order.amount_total
            else:
                order.visible_amount_total = 0.0

    visible_amount_total = fields.Monetary(
        'Total Visible',
        compute='_compute_visible_amount_total',
        help='Total de la venta (visible según permisos)'
    )

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.depends('price_unit')
    def _compute_visible_price_unit(self):
        """Precio unitario visible basado en permisos"""
        for line in self:
            if self.env.user.has_group('control_costos_hexagonos.group_view_sale_price'):
                line.visible_price_unit = line.price_unit
            else:
                line.visible_price_unit = 0.0

    @api.depends('price_subtotal')
    def _compute_visible_price_subtotal(self):
        """Subtotal visible basado en permisos"""
        for line in self:
            if self.env.user.has_group('control_costos_hexagonos.group_view_sale_price'):
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
```

-e ### ./models/stock_move.py
```
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
```

-e ### ./salida_modulo_completo.md
```
-e ### ./data/cost_groups.xml
```
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data noupdate="1">
        <!-- Asignar grupos a usuarios administradores existentes -->
        <function model="res.users" name="write">
            <value eval="[ref('base.user_admin')]"/>
            <value eval="{'groups_id': [(4, ref('group_cost_admin'))]}"/>
        </function>
    </data>
</odoo>
```

-e ### ./models/product_template.py
```
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
```

-e ### ./models/purchase_order.py
```
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
```

-e ### ./models/sale_order.py
```
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.depends('amount_total')
    def _compute_visible_amount_total(self):
        """Total visible basado en permisos"""
        for order in self:
            if self.env.user.has_group('control_costos_hexagonos.group_view_sale_total'):
                order.visible_amount_total = order.amount_total
            else:
                order.visible_amount_total = 0.0

    visible_amount_total = fields.Monetary(
        'Total Visible',
        compute='_compute_visible_amount_total',
        help='Total de la venta (visible según permisos)'
    )

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.depends('price_unit')
    def _compute_visible_price_unit(self):
        """Precio unitario visible basado en permisos"""
        for line in self:
            if self.env.user.has_group('control_costos_hexagonos.group_view_sale_price'):
                line.visible_price_unit = line.price_unit
            else:
                line.visible_price_unit = 0.0

    @api.depends('price_subtotal')
    def _compute_visible_price_subtotal(self):
        """Subtotal visible basado en permisos"""
        for line in self:
            if self.env.user.has_group('control_costos_hexagonos.group_view_sale_price'):
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
```

-e ### ./models/stock_move.py
```
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
```
```

-e ### ./security/cost_security.xml
```
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data noupdate="1">
        <!-- Categoría de grupos -->
        <record id="module_category_cost_control" model="ir.module.category">
            <field name="name">Control de Costos</field>
            <field name="description">Control de visibilidad de valores de costo</field>
            <field name="sequence">20</field>
        </record>

        <!-- Grupo para ver costos de productos -->
        <record id="group_view_cost" model="res.groups">
            <field name="name">Ver Costos de Productos</field>
            <field name="category_id" ref="module_category_cost_control"/>
            <field name="comment">Permite ver los costos reales de los productos</field>
        </record>

        <!-- Grupo para ver precios de venta -->
        <record id="group_view_sale_price" model="res.groups">
            <field name="name">Ver Precios de Venta</field>
            <field name="category_id" ref="module_category_cost_control"/>
            <field name="comment">Permite ver los precios de venta reales</field>
        </record>

        <!-- Grupo para ver precios de compra -->
        <record id="group_view_purchase_price" model="res.groups">
            <field name="name">Ver Precios de Compra</field>
            <field name="category_id" ref="module_category_cost_control"/>
            <field name="comment">Permite ver los precios de compra reales</field>
        </record>

        <!-- Grupo para ver totales de compra -->
        <record id="group_view_purchase_total" model="res.groups">
            <field name="name">Ver Totales de Compra</field>
            <field name="category_id" ref="module_category_cost_control"/>
            <field name="comment">Permite ver los totales de órdenes de compra</field>
        </record>

        <!-- Grupo para ver totales de venta -->
        <record id="group_view_sale_total" model="res.groups">
            <field name="name">Ver Totales de Venta</field>
            <field name="category_id" ref="module_category_cost_control"/>
            <field name="comment">Permite ver los totales de órdenes de venta</field>
        </record>

        <!-- Grupo para ver costos de stock -->
        <record id="group_view_stock_cost" model="res.groups">
            <field name="name">Ver Costos de Stock</field>
            <field name="category_id" ref="module_category_cost_control"/>
            <field name="comment">Permite ver los costos en movimientos de stock</field>
        </record>

        <!-- Grupo administrador que tiene todos los permisos -->
        <record id="group_cost_admin" model="res.groups">
            <field name="name">Administrador de Costos</field>
            <field name="category_id" ref="module_category_cost_control"/>
            <field name="comment">Acceso completo a todos los valores de costo</field>
            <field name="implied_ids" eval="[(4, ref('group_view_cost')),
                                             (4, ref('group_view_sale_price')),
                                             (4, ref('group_view_purchase_price')),
                                             (4, ref('group_view_purchase_total')),
                                             (4, ref('group_view_sale_total')),
                                             (4, ref('group_view_stock_cost'))]"/>
        </record>
    </data>
</odoo>
```

-e ### ./security/ir.model.access.csv
```
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_product_cost_user,product.template.cost.user,product.model_product_template,group_view_cost,1,0,0,0
access_sale_cost_user,sale.order.cost.user,sale.model_sale_order,group_view_sale_price,1,0,0,0
access_purchase_cost_user,purchase.order.cost.user,purchase.model_purchase_order,group_view_purchase_price,1,0,0,0
```

-e ### ./views/product_template_views.xml
```
<odoo>
    <record id="view_product_template_form_cost_control" model="ir.ui.view">
        <field name="name">product.template.form.cost.control</field>
        <field name="model">product.template</field>
        <field name="inherit_id" ref="product.product_template_form_view"/>
        <field name="arch" type="xml">

            <!-- Campo standard_price editable solo para grupo autorizado -->
            <field name="standard_price" position="attributes">
                <attribute name="groups">control_costos_hexagonos.group_view_cost</attribute>
            </field>

            <!-- Campo visible para no autorizados -->
            <field name="standard_price" position="after">
                <field name="visible_standard_price" readonly="1" string="Costo Controlado"
                       groups="!control_costos_hexagonos.group_view_cost"/>
            </field>

            <!-- Campo list_price editable solo para grupo autorizado -->
            <field name="list_price" position="attributes">
                <attribute name="groups">control_costos_hexagonos.group_view_sale_price</attribute>
            </field>

            <!-- Campo visible para no autorizados -->
            <field name="list_price" position="after">
                <field name="visible_list_price" readonly="1" string="Precio Controlado"
                       groups="!control_costos_hexagonos.group_view_sale_price"/>
            </field>

        </field>
    </record>
</odoo>
```

-e ### ./views/purchase_order_views.xml
```
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="view_purchase_order_form_cost_control" model="ir.ui.view">
        <field name="name">purchase.order.form.cost.control</field>
        <field name="model">purchase.order</field>
        <field name="inherit_id" ref="purchase.purchase_order_form"/>
        <field name="arch" type="xml">

            <!-- Insertar visible_amount_total después del bloque tax_totals -->
            <xpath expr="//group[@class='oe_subtotal_footer']/field[@name='tax_totals']" position="after">
                <field name="visible_amount_total" nolabel="0"
                    class="oe_subtotal_footer_separator"
                    widget="monetary" options="{'currency_field': 'currency_id'}"/>
            </xpath>

            <!-- Campos en líneas de la orden (Corregido con <list>) -->
            <xpath expr="//field[@name='order_line']/list/field[@name='price_unit']" position="after">
                <field name="visible_price_unit" string="Precio Unitario"/>
            </xpath>
            <xpath expr="//field[@name='order_line']/list/field[@name='price_unit']" position="attributes">
                <attribute name="column_invisible">1</attribute>
            </xpath>

            <xpath expr="//field[@name='order_line']/list/field[@name='price_subtotal']" position="after">
                <field name="visible_price_subtotal" string="Subtotal"/>
            </xpath>
            <xpath expr="//field[@name='order_line']/list/field[@name='price_subtotal']" position="attributes">
                <attribute name="column_invisible">1</attribute>
            </xpath>

        </field>
    </record>
</odoo>
```

-e ### ./views/sale_order_views.xml
```
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="view_sale_order_form_cost_control" model="ir.ui.view">
        <field name="name">sale.order.form.cost.control</field>
        <field name="model">sale.order</field>
        <field name="inherit_id" ref="sale.view_order_form"/>
        <field name="arch" type="xml">

            <!-- Corregido: Insertar visible_amount_total justo después del tax_totals -->
            <xpath expr="//group[contains(@class, 'oe_subtotal_footer')]/field[@name='tax_totals']" position="after">
                <field name="visible_amount_total" nolabel="0"
                    class="oe_subtotal_footer_separator"
                    widget="monetary" options="{'currency_field': 'currency_id'}"/>
            </xpath>

            <!-- Campos en líneas de la orden (Corregido con <list>) -->
            <xpath expr="//field[@name='order_line']/list/field[@name='price_unit']" position="after">
                <field name="visible_price_unit" string="Precio Unitario"/>
            </xpath>
            <xpath expr="//field[@name='order_line']/list/field[@name='price_unit']" position="attributes">
                <attribute name="column_invisible">1</attribute>
            </xpath>

            <xpath expr="//field[@name='order_line']/list/field[@name='price_subtotal']" position="after">
                <field name="visible_price_subtotal" string="Subtotal"/>
            </xpath>
            <xpath expr="//field[@name='order_line']/list/field[@name='price_subtotal']" position="attributes">
                <attribute name="column_invisible">1</attribute>
            </xpath>

        </field>
    </record>
</odoo>
```

### __init__.py
```python
from . import models
```

### __manifest__.py
```python
{
    'name': 'Control de Costos Hexágonos',
    'version': '18.0.1.0.0',
    'category': 'Inventory/Inventory',
    'summary': 'Control de visibilidad de valores de costo por grupos de usuario',
    'description': """
        Módulo que controla la visibilidad de valores sensibles:
        - Los valores de costo se muestran como 0 si el usuario no tiene permisos
        - Control granular por grupos de usuario
        - Aplica a productos, órdenes de compra y ventas
    """,
    'author': 'Tu Empresa',
    'depends': ['base', 'product', 'purchase', 'sale', 'stock'],
    'data': [
        'security/cost_security.xml',
        'security/ir.model.access.csv',
        'data/cost_groups.xml',
        'views/product_template_views.xml',
        'views/purchase_order_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
```

