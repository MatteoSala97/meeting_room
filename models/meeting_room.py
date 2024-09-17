from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MeetingRoomModel(models.Model):
    _name = 'meeting.room'
    _description = 'Modulo di test per prenotazione sala riunioni'
    
    name = fields.Char(string='Name', required=True)
    date = fields.Date(string='Data', required=True)
    start_time = fields.Float(string='Ora di inizio', required=True)
    end_time = fields.Float(string='Ora di fine', required=True)
    comments = fields.Char(string="Commenti", placeholder="Lascia qui un commento...")
    # Radio button per la selezione
    meeting_type = fields.Selection([
        ('interview', 'Colloquio'),
        ('meeting', 'Riunione')
    ], string="Destinazione di utilizzo", required=True, default='meeting')


    # Questo è un controller dell'orario. Se la prenotazione è precedente o successiva all'orario di lavoro non permette all'utente di salvarla.
     
    @api.constrains('start_time', 'end_time')
    def _check_time(self):
        for record in self:
            if not (8 <= record.start_time <= 20):
                raise ValidationError("L'orario di inizio deve essere compreso tra le 8:00 e le 20:00.")
            if not (8 <= record.end_time <= 20):
                raise ValidationError("L'orario di fine deve essere compreso tra le 8:00 e le 20:00.")
            if record.start_time >= record.end_time:
                raise ValidationError("L'orario di fine deve essere successivo all'orario di inizio.")


 # Controller per la prenotazione multipla allo stesso orario o stesso giorno 
 
            # overlapping_bookings = self.search([
            #     ('date', '=', record.date),
            #     ('id', '!=', record.id),
            #     '|', '&', ('start_time', '<', record.end_time), ('end_time', '>', record.start_time)
            # ])
            # if overlapping_bookings:
            #     raise ValidationError("Esiste già una prenotazione sovrapposta per questa data e ora.")
