from odoo import http 
from odoo.http import request

class EquipmentApi(http.Controller):

    @http.route(
        '/api/equipment',
        type='http',
        auth='puplic',
        methods=['GET'],
        csrf=False
    )
    def get_equipment(self):
        equipment = request.env['devices.management'].sudo().search([])

        data = []

        for record in equipment:
            data.append({
                'id': equipment.id,
                'name': equipment.name,
                'serial_number': equipment.serial_number,
                'purchase_date': equipment.purchase_date,
                'price': equipment.price,
                'status': equipment.status,
                'employee_id': equipment.employee_id.id if equipment.employee_id else None,
            })
        return request.make_json_response(data)