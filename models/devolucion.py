from odoo import models, fields

class Devolucion(models.Model):
    _name = 'upobebe.devolucion'
    _description = 'Devolución'

    motivo = fields.Char(string='Motivo de devolución', required=True)
    estado = fields.Selection([ 
        ('pendiente', 'Pendiente'), 
        ('aceptada', 'Aceptada'), 
        ('rechazada', 'Rechazada') 
        ], string='Estado', default='pendiente', required=True)

    # Relación con Usuario (n devoluciones por usuario)
    usuario_id = fields.Many2one('upobebe.usuario', string='Usuario', required=True)

    # Relación con Pedido (emulación de One2one)
    pedido_id = fields.Many2one('upobebe.pedido', string='Pedido')

    def action_aceptada(self):
        self.write({'estado': 'aceptada'})
    def action_rechazada(self):
        self.write({'estado': 'rechazada'})
    