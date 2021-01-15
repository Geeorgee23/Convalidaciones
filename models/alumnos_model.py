# -*- coding: utf-8 -*-

from odoo import models, fields, api
from random import choice
from odoo.exceptions import ValidationError


class alumnos_model(models.Model):
    _name = 'convalidaciones_app.alumnos_model'
    _description = 'convalidaciones_app.alumnos_model'

    foto = fields.Binary()
    name = fields.Char(string="Nombre",help="Añade el nombre del Alumno",required=True, index=True)
    password = fields.Char(string="Contraseña",help="Añade la contraseña del Alumno", size=10)
    edad = fields.Integer(string="Edad",help="Añade la edad del Alumno", required=True)
    localidad = fields.Char(string="Localidad",help="Añade la Localidad del Alumno", required=True, size=100)
    provincia = fields.Char(string="Provincia",help="Añade la provincia del Alumno", required=True, size=100)
    email = fields.Char(string="Email",help="Añade la email del Alumno", required=False, size=100)
    convalidaciones = fields.One2many("convalidaciones_app.convalidaciones_model", "alumnos_id", string="Convalidaciones")
    profesores = fields.Many2many("convalidaciones_app.profesores_model", relation="profesores2alumnos_rel", string="Profesores")

    def generaContraseña(self):
        self.ensure_one()
        longitud = 10
        valores = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        p = ""
        p = p.join([choice(valores) for i in range(longitud)])
        self.password = p
        return True



    @api.constrains("edad")
    def _checkEdad(self):
        if self.edad<14:
            raise ValidationError("La edad debe ser mayor de 14 años!")
