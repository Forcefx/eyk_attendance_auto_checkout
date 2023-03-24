from datetime import datetime, timedelta
from odoo import api, exceptions, fields, models, _

class LogoutService(models.AbstractModel):
    _name = 'logout.service'

    @api.model
    def logout_employees(self):
        now = datetime.now()
        limit_time = now - timedelta(hours=9)
        employees = self.env['res.users'].search([('checkin_time', '<', limit_time.strftime("%Y-%m-%d %H:%M:%S"))])
        for employee in employees:
            employee.logout()
            subject = _("Automatic Logout from Odoo")
            message = _("You have been automatically logged out from Odoo after 9 hours of inactivity. Please log in again if you need to continue working.")
            employee.message_post(body=message, subject=subject)
            self.env['mail.thread'].message_post(body=message, subject=subject, partner_ids=self.env.user.partner_id.ids)
