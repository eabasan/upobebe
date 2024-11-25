from odoo import models, fields

class Catalogo(models.Model):
    _name = 'upobebe.catalogo'
    _description = 'Catálogo de Productos de UPOBEBÉ'

    tamanyo = fields.Integer(string="Capacidad", help="Capacidad del catálogo", required=True)
    num_prod = fields.Integer(string="Stock Total", help="Stock actual de todos los productos")
    catalogo_id = fields.Integer(string="Catalogo")

    # Relación con Productos (1 catálogo contiene varios productos)
    productos_ids = fields.One2many('upobebe.producto', 'catalogo_id', string='Productos')

    # Relación con Administrador (1 catálogo gestionado por 1 administrador)
    administrador_id = fields.Many2one('upobebe.administrador', string='Administrador', required=True)
