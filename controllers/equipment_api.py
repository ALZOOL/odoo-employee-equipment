from odoo import http 
from odoo.http import request

class EquipmentApi(http.Controller):

    @http.route(
        '/api/equipment',
        type='http',
        auth='public',
        methods=['GET'],
        csrf=False
    )
    def get_equipment(self):
        equipment = request.env['device.equipment'].sudo().search([])

        data = []

        for record in equipment:
            data.append({
                'id': record.id,
                'name': record.name,
                'serial_number': record.serial_number,
                'purchase_date': record.purchase_date,
                'price': record.price,
                'status': record.status,
                'employee_id': record.employee_id.id if record.employee_id else None,
            })
        return request.make_json_response(data)