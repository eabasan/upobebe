from odoo import models, fields

class Administrador(models.Model):
    _name = 'upobebe.administrador'
    _description = 'Administrador'

    id_admin = fields.Char(string='ID Admin', required=True)
    nombre = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Email', required=True)

    # Relación con Reclamaciones
    reclamacion_ids = fields.One2many('upobebe.reclamacion', 'administrador_id', string='Reclamaciones')

    # Relación con Catálogos (1 administrador puede gestionar varios catálogos)
    catalogo_ids = fields.One2many('upobebe.catalogo', 'administrador_id', string='Catálogos')
