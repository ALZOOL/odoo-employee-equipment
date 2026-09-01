from odoo import models, fields
from odoo.exceptions import UserError


class DeviceManagement(models.Model):
    _name = 'device.equipment'
    _description = 'Device Management' 
    
    name = fields.Char(String = 'Equipment Name', required = True)
    serial_number = fields.Integer(String = 'Serial Number')
    purchase_date = fields.Date(String = 'Purchase Date')
    price = fields.Float(String = 'Price')
    active = fields.Boolean(String = 'Active', default = True)


    status = fields.Selection(
        [
            ('available', 'Available'),
            ('assigned', 'Assigned'),
            ('maintenance', 'Maintenance'),
            ('damaged', 'Damaged'),
        ],
        default = 'available',
    )

    employee_id = fields.Many2one('hr.employee', string='Assign to')

    #SQL
    #we added sql constraints instaed of api.constraints bcz it dosenot require any logic, 
    _sql_constraints ={
        (
            'unique_serial_number',
            'UNIQUE(serial_number)',
            'The serial number exists already. Please enter a unique serial number.'
        )
    }

    def action_status_assigend(self):
        if not self.employee_id:
            raise UserError("يجب تحديد الموظف قبل تعيين الحالة الى مسجل ")
        self.status = 'assigned'
        self.purchase_date = fields.Date.context_today(self)

    def action_status_available(self):
        self.status = 'available'
        self.employee_id = False

    def action_return(self):
            self.status = 'available'
            self.employee_id = False
            self.purchase_date = False
            self.price = False
            self.active = True