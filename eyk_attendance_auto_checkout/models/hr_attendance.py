from odoo import models, fields, api
import datetime

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    @api.model
    def auto_checkout(self):
        attendances = self.search([('check_out', '=', False)])
        for attendance in attendances:
            check_in_datetime = fields.Datetime.from_string(attendance.check_in)
            current_datetime = fields.Datetime.now()
            delta = current_datetime - check_in_datetime
            if delta.total_seconds() >= 9 * 3600: # 9 hours in seconds
                attendance.check_out = fields.Datetime.now()

    @api.model
    def run_scheduler(self):
        self.auto_checkout()
