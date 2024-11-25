from odoo import models, fields

class Pedido(models.Model):
    _name = 'upobebe.pedido'
    _description = 'Pedido de UPOBEBÉ'

    id_pedido = fields.Integer(string="ID Pedido", required=True)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
        ('devuelto', 'Devuelto')
    ], string="Estado", default="pendiente")

    # Relación con Usuario (emulación de One2one para Usuario)
    usuario_id = fields.Many2one('upobebe.usuario', string="Usuario", required=True)

    # Relación con Compra (emulación de One2one)
    compra_id = fields.One2many('upobebe.compra', 'pedido_id', string='Compra')

    # Relación con Devolución (emulación de One2one)
    devolucion_id = fields.One2many('upobebe.devolucion', 'pedido_id', string='Devolución')

    # Relación con Productos (n productos en un pedido)
    productos_ids = fields.One2many('upobebe.producto', 'pedido_id', string="Productos")
