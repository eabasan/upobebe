from odoo import models, fields

class Devolucion(models.Model):
    _name = 'upobebe.devolucion'
    _description = 'Devolución'

    motivo = fields.Char(string='Motivo de devolución', required=True)
    estado = fields.Char(string='Estado', required=True)

    # Relación con Usuario (n devoluciones por usuario)
    usuario_id = fields.Many2one('upobebe.usuario', string='Usuario', required=True)

    # Relación con Pedido (emulación de One2one)
    pedido_id = fields.Many2one('upobebe.pedido', string='Pedido')
