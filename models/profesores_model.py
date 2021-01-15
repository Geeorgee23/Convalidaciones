# -*- coding: utf-8 -*-

from odoo import models, fields, api
from random import choice
from datetime import datetime
from odoo.exceptions import ValidationError


class profesores_model(models.Model):
    _name = 'convalidaciones_app.profesores_model'
    _description = 'convalidaciones_app.profesores_model'

    foto = fields.Binary()
    name = fields.Char(string="Nombre",help="Añade el nombre del Profesor",required=True, index=True, size=50)
    apellidos = fields.Char(string="Apellidos",help="Añade los apellidos del Profesor",required=True, index=True, size=50)
    dni = fields.Char(string="DNI",help="Añade el dni del Alumno",required=True, size=9)
    alumnos = fields.Many2many("convalidaciones_app.alumnos_model", relation="alumnos2profesores_rel", string="Alumnos")
    numAlumnos = fields.Integer(string="Numero Alumnos: ", compute="_calcAlumnos", store=True) 


    @api.depends("alumnos")
    def _calcAlumnos(self):
        self.numAlumnos = len(self.alumnos)

    
    @api.constrains("dni")
    def _validarDni(self):
        letras="TRWAGMYFDPXBNJZSQVHLCKE"

        letra =self.dni[-1]
        num=int(self.dni[:-1])
        if letras[num%23]!=letra:
            raise ValidationError ("DNI Invalido!")