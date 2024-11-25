# -*- coding: utf-8 -*-
from odoo import models, fields

class Valoracion(models.Model):
    _name = 'upobebe.valoracion'
    _description = 'Valoración del Producto'

    id_valoracion = fields.Integer(string="ID Valoración", required=True)
    puntuacion = fields.Integer(string="Puntuación", required=True)
    comentario = fields.Text(string="Comentario")

    producto_id = fields.Many2one('upobebe.producto', string="Producto", required=True)
    usuario_id = fields.Many2one('upobebe.usuario', string='Usuario')
