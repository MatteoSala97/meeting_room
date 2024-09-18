{
    'name': 'Meeting Room Booking Menu',
    'version': '1.0',
    'summary': 'A module to book the meeting room',
    'description': 'This module allows the user to book the meeting room allowing also to select the duration',
    'author': 'Matteo',
    'depends': ['base'],
    'data': [
        'views/meeting_room_view.xml',
        'security/ir.model.access.csv'        
        ],
    'images': ['static/description/multiuser.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
