from odoo import models, fields

class Reclamacion(models.Model):
    _name = 'upobebe.reclamacion'
    _description = 'Reclamación'

    mensaje = fields.Char(string='Mensaje', required=True)
    nombre = fields.Char(string='Nombre', required=True)
    telefono = fields.Integer(string='Teléfono', required=True)
    producto = fields.Integer(string='Producto', required=True)

    usuario_id = fields.Many2one('upobebe.usuario', string='Usuario', required=True)
    administrador_id = fields.Many2one('upobebe.administrador', string='Administrador')

    estado = fields.Selection([ 
        ('nueva', 'Nueva'), 
        ('en_proceso', 'En Proceso'), 
        ('resuelta', 'Resuelta'), 
        ('rechazada', 'Rechazada') 
        ], string='Estado', default='nueva', required=True) 
    def action_en_proceso(self): 
        self.write({'estado': 'en_proceso'}) 
    def action_resuelta(self): 
        self.write({'estado': 'resuelta'}) 
    def action_rechazada(self): 
        self.write({'estado': 'rechazada'})
