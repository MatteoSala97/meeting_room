from odoo import models, fields

class MeetingRoomModel(models.Model):
    _name = 'meeting.room'
    _description = 'Modulo di test per prenotazione sala riunioni'
    
    name = fields.Char(string='Name', required=True)
    date = fields.Date(string='Data', required=True)
    start_time = fields.Float(string='Ora di inizio', required=True)
    end_time = fields.Float(string='Ora di fine', required=True)
    comments = fields.Char(string="Commenti", placeholder="Lascia qui un commento...")
    meeting_type = fields.Selection([
        ('interview', 'Colloquio'),
        ('meeting', 'Riunione')
    ], string="Destinazione di utilizzo", required=True, default='meeting')
    