# -*- coding: utf-8 -*-
# Part of AHT. See LICENSE file for full copyright and licensing details.

from odoo import models, fields

class Booking(models.Model):

    _name = 'room_booking.booking'
    _description = 'Meeting Room Booking'
    code = fields.Char(string='Booking Code')
    room_id = fields.Many2one('room_booking.room', string='Room')
    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user)
    date = fields.Date(string='Date', required=True, default=lambda self: fields.Date.today())
    # start = fields.Datetime('Start', required=True)
    # end = fields.Datetime('End', required=True)
    start = fields.Float('Start', required=True)
    end = fields.Float('End', required=True)
    note = fields.Text('Notes')
    hc_note = fields.Text('HC Notes')
    status = fields.Selection([('1', 'active'),
                               ('0', 'cancelled')], default='1')
