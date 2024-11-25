from odoo import models, fields

class Usuario(models.Model):
    _name = 'upobebe.usuario'
    _description = 'Usuario UPOBEBÉ'

    id_usuario = fields.Integer(string="ID Usuario", required=True, help="Identificador único del usuario")
    nombre = fields.Char(string="Nombre", required=True, help="Nombre del usuario")
    apellido = fields.Char(string="Apellido", required=True, help="Apellido del usuario")
    email = fields.Char(string="Email", required=True, help="Correo electrónico del usuario")
    contrasena = fields.Char(string="Contraseña", required=True, help="Contraseña de acceso del usuario")

    # Relación con Reclamaciones (n reclamaciones por usuario)
    reclamacion_ids = fields.One2many('upobebe.reclamacion', 'usuario_id', string="Reclamaciones")

    # Relación con Valoraciones (n valoraciones por usuario)
    valoracion_ids = fields.One2many('upobebe.valoracion', 'usuario_id', string="Valoraciones")

    # Relación con Compras (n compras por usuario)
    compra_ids = fields.One2many('upobebe.compra', 'usuario_id', string="Compras")

    # Relación con Devoluciones (n devoluciones por usuario)
    devolucion_ids = fields.One2many('upobebe.devolucion', 'usuario_id', string="Devoluciones") 

    
