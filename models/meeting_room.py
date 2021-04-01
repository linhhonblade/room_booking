# -*- coding: utf-8 -*-
# Part of AHT. See LICENSE file for full copyright and licensing details.

from odoo import models, fields

class MeetingRoom(models.Model):

    _name = 'room_booking.room'
    _description = 'Meeting Room'

    code = fields.Char(string='Room Code', size=3)
    name = fields.Char(string='Room Name')
    capacity = fields.Integer(string='Room Capacity', help='Maximum number of people')
    description = fields.Text('Description')
    active = fields.Boolean(default=True)
    status = fields.Selection([('1', 'active'),
                               ('0', 'inactive'),
                               ('2', 'deleted')], default='1')
