# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class hospital_management(models.Model):
    _name = 'hospital_management.hospital_management'
    _description = 'Gestión de hospital'

    appointment_date = fields.Datetime(string="Fecha y hora", required=True)
    name = fields.Char(string="Nombre del visitante", required=True)
    pacient_id = fields.Many2one(comodel_name="res.partner", string="Paciente")
    description = fields.Text(string="Motivo de visita")

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
