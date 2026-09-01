from odoo import models,fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee' 

    equipment_count = fields.Integer(
        compute = '_compute_equipment_count'
    )

    def _compute_equipment_count(self):
        for employee in self:
            employee.equipment_count = self.env['device.equipment'].search_count([('employee_id','=',employee.id),('status','=','assigned')])

    def action_view_equipment(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Employee Equipment',
            'res_model': 'device.equipment',
            'view_mode': 'list,form',
            'domain': [('employee_id', '=', self.id),('status','=','assigned')],
        }