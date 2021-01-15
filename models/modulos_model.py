# -*- coding: utf-8 -*-

from odoo import models, fields, api


class modulos_model(models.Model):
    _name = 'convalidaciones_app.modulos_model'
    _description = 'convalidaciones_app.modulos_model'

    name = fields.Char(string="Nombre", help="Añade el nombre del Modulo", required=True, size=10)
    descripcion = fields.Html(string="Descripción", help="Añade la descripcion del Modulo", required=True)
    horas = fields.Integer(string="Carga horaria (Horas)", help="Añade las horas del Modulo", required=True)
    ciclo = fields.Many2one("convalidaciones_app.ciclos_model", string="Ciclo")