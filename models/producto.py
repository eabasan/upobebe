from odoo import models, fields, api

class Producto(models.Model):
    _name = 'upobebe.producto'
    _description = 'Producto'

    id_producto = fields.Integer(string="ID Producto", required=True)
    nombre = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripción")
    tipo = fields.Selection([
        ('juguete', 'Juguete'),
        ('ropa', 'Ropa'),
        ('accesorio', 'Accesorio')
    ], string="Tipo", required=True)
    precio = fields.Float(string="Precio", required=True)
    stock = fields.Integer(string="Stock", required=True)
    edad_recomendada = fields.Integer(string="Edad Recomendada")

    # Relación con Proveedor (n productos distribuidos por 1 proveedor)
    proveedor_id = fields.Many2one('upobebe.proveedor', string="Proveedor")

    # Relación con Catálogo (1 catálogo contiene varios productos)
    catalogo_id = fields.Many2one('upobebe.catalogo', string="Catálogo")

    # Relación con Pedido (1 producto pertenece a un pedido)
    pedido_id = fields.Many2one('upobebe.pedido', string='Pedido', ondelete='cascade')

    # Relación con Valoraciones (1 producto tiene muchas valoraciones)
    valoracion_ids = fields.One2many('upobebe.valoracion', 'producto_id', string="Valoraciones")

    promedio_valoracion = fields.Float(string="Promedio de Valoración", compute="calcular_promedio_valoracion")

    def calcular_promedio_valoracion(self):
        for producto in self:
            valoraciones = producto.valoracion_ids.filtered(lambda v: v.puntuacion > 0)
            if valoraciones:
                producto.promedio_valoracion = sum(v.puntuacion for v in valoraciones) / len(valoraciones)
            else:
                producto.promedio_valoracion = 0
    @api.model
    def create(self, vals):
        """Asigna un catálogo automáticamente al crear un producto si no se especifica."""
        if 'tipo' in vals and not vals.get('catalogo_id'):
            catalogo = self.env['upobebe.catalogo'].search([('tipo', '=', vals['tipo'])], limit=1)
            if catalogo:
                vals['catalogo_id'] = catalogo.id
        return super(Producto, self).create(vals)
