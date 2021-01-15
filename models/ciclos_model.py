# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ciclos_model(models.Model):
    _name = 'convalidaciones_app.ciclos_model'
    _description = 'convalidaciones_app.ciclos_model'
    _sql_constraints = [("ciclos_name_uniq","UNIQUE(name)","No puede haber 2 ciclos con el mismo nombre!"),]

    name = fields.Char(string="Ciclo", help="Añade el nombre del ciclo", required="True", index="True", size=10)
    descripcion = fields.Html(string="Descrpición del Ciclo", help="Descripcion ciclo", required="True")
    modulo = fields.One2many("convalidaciones_app.modulos_model","ciclo", string="Modulo")