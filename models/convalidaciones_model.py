# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class convalidaciones_model(models.Model):
    _name = 'convalidaciones_app.convalidaciones_model'
    _description = 'convalidaciones_app.convalidaciones_model'

    fecha = fields.Date(string="Fecha", help="Añade la fecha de la convalidacion",required=True, default=datetime.today())
    modulos_id = fields.Many2one("convalidaciones_app.modulos_model", string="Modulo")
    alumnos_id = fields.Many2one("convalidaciones_app.alumnos_model", string="Alumno")