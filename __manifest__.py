# -*- coding: utf-8 -*-
{
    'name': "upobebe",

    'summary': "Tienda de articulos para bebes",

    'description': """Gestión de la pedidos, catalogo de productos, devoluciones...""",

    'author': "Grupo 7",
    'website': "https://www.upobebe.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        'security/security.xml',  # Seguridad y reglas de acceso
        'security/ir.model.access.csv',  # Accesos al modelo 
        'reports/reports.xml', # Definiciones de informes 
        'reports/reports_producto.xml', # Definiciones específicas de informes para Producto 
        'reports/reports_reclamacion.xml', # Definiciones específicas de informes para Reclamación
        'reports/reports_pedido.xml', # Informes y plantillas de pedidos
        'views/producto_view.xml',  # Vistas para el modelo Producto
        'views/usuario_view.xml',  # Vistas para el modelo Usuario
        'views/pedido_view.xml',  # Vistas para el modelo Pedido
        'views/catalogo_view.xml',  # Vistas para el modelo Catálogo
        'views/reclamacion_view.xml',  # Vistas para el modelo Reclamación
        'views/devolucion_view.xml',  # Vistas para el modelo Devolución
        'views/administrador_view.xml',  # Vistas para el modelo Administrador
        'views/proveedor_view.xml',  # Vistas para el modelo Proveedor
        'views/valoracion_view.xml',  # Vistas para el modelo Valoración
        'views/compra_view.xml',  # Vistas para el modelo Compra
        'views/menu.xml',  # El archivo del menú que creamos
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/upobebe.usuario.csv',
        'demo/upobebe.producto.csv',
        'demo/upobebe.pedido.csv',
        'demo/upobebe.reclamacion.csv',
        'demo/upobebe.devolucion.csv',
        'demo/upobebe.administrador.csv',
        'demo/upobebe.proveedor.csv',
        'demo/upobebe.valoracion.csv',
        'demo/upobebe.compra.csv',
        'demo/upobebe.catalogo.csv',
    ],
    'application':True, 
    
    'assets': {
        'web.assets_backend': [
            'upobebe/static/src/scss/puntuacion_widget.scss',
            'upobebe/static/src/js/puntuacion_widget.js',
            'upobebe/static/src/xml/puntuacion_widget.xml',
        ],
    },
    
}

