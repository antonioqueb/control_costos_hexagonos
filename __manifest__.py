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
