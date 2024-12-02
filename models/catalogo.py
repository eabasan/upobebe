from odoo import models, fields, api

class Catalogo(models.Model):
    _name = 'upobebe.catalogo'
    _description = 'Catálogo de Productos de UPOBEBÉ'

    tamanyo = fields.Integer(string="Capacidad", help="Capacidad del catálogo", required=True)
    num_prod = fields.Integer(string="Stock Total", help="Stock actual de todos los productos", compute='_compute_num_prod', store=True)
    catalogo_id = fields.Integer(string="Catalogo")
    tipo = fields.Selection([ ('juguete', 'Juguete'), ('ropa', 'Ropa'), ('accesorio', 'Accesorio') ], string="Tipo de Producto", required=True)

    # Relación con Productos (1 catálogo contiene varios productos)
    productos_ids = fields.One2many('upobebe.producto', 'catalogo_id', string='Productos', compute='_compute_productos', store=True)

    # Relación con Administrador (1 catálogo gestionado por 1 administrador)
    administrador_id = fields.Many2one('upobebe.administrador', string='Administrador', required=True)

    @api.depends('tipo')
    def _compute_productos(self):
        # Filtra y asigna los productos al catálogo según el tipo de producto (comportamiento no básico)
        for catalogo in self:
            catalogo.productos_ids = self.env['upobebe.producto'].search([('tipo', '=', catalogo.tipo)])
    @api.depends('productos_ids.stock')
    def _compute_num_prod(self):
        # Calcula el stock total (num_prod) sumando el stock de todos los productos en el catálogo
        for catalogo in self:
            catalogo.num_prod = sum(producto.stock for producto in catalogo.productos_ids)
