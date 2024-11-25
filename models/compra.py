from odoo import models, fields

class Compra(models.Model):
    _name = 'upobebe.compra'
    _description = 'Compra de productos'

    fecha = fields.Datetime(string='Fecha', required=True)
    hora = fields.Char(string='Hora', required=True)
    id_compra = fields.Integer(string='ID de Compra', required=True)
    total = fields.Float(string='Total', required=True)

    # Relación con Usuario (n compras por usuario)
    usuario_id = fields.Many2one('upobebe.usuario', string='Usuario', required=True)

    # Relación con Pedido (emulación de One2one)
    pedido_id = fields.Many2one('upobebe.pedido', string='Pedido', unique=True)
