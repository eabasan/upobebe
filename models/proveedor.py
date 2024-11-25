
from odoo import models, fields

class Proveedor(models.Model):
    _name = 'upobebe.proveedor'
    _description = 'Proveedor de Productos'

    id_proveedor = fields.Integer(string="ID Proveedor", required=True)
    nombre = fields.Char(string="Nombre", required=True)
    telefono = fields.Integer(string="Teléfono", required=True)

    # Relación con Productos (1 proveedor distribuye varios productos)
    producto_ids = fields.One2many('upobebe.producto', 'proveedor_id', string="Productos Distribuidos")
