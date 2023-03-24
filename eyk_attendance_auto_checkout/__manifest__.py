
{
    "name": "eyk attendance auto checkout",
    'author': 'Forcefx at Github',
    'website': 'https://github.com/Forcefx/eyk_attendance_auto_checkout',
    "version": "15.0.1.0.0",
    'category': 'Attendances',
    'summary': """Automatically check out the employee based on
                  maximum hours set in the code file""",            
    'depends': ['hr_attendance'],
    'data': [
        'data/scheduler.xml',
    ],
    'license': 'MIT',
    'installable': True,
    'application': True,
    'auto_install': False,
}
