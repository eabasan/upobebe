from odoo import models, fields

class Producto(models.Model):
    _name = 'upobebe.producto'
    _description = 'Producto'

    id_producto = fields.Integer(string="ID Producto", required=True)
    nombre = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripción")
    tipo = fields.Selection([
        ('juguete', 'Juguete'),
        ('ropa', 'Ropa'),
        ('accesorio', 'Accesorio')
    ], string="Tipo", required=True)
    precio = fields.Float(string="Precio", required=True)
    stock = fields.Integer(string="Stock", required=True)
    edad_recomendada = fields.Integer(string="Edad Recomendada")

    # Relación con Proveedor (n productos distribuidos por 1 proveedor)
    proveedor_id = fields.Many2one('upobebe.proveedor', string="Proveedor")

    # Relación con Catálogo (1 catálogo contiene varios productos)
    catalogo_id = fields.Many2one('upobebe.catalogo', string="Catálogo", compute='_compute_catalogo', store=True, readonly=False)

    # Relación con Pedido (1 producto pertenece a un pedido)
    pedido_id = fields.Many2one('upobebe.pedido', string='Pedido', ondelete='cascade')

    # Relación con Valoraciones (1 producto tiene muchas valoraciones)
    valoracion_ids = fields.One2many('upobebe.valoracion', 'producto_id', string="Valoraciones")
