from odoo import http 
from odoo.http import request

class EquipmentApi(http.Controller):
    #get all equipment records
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

    @http.route(
        '/api/equipment/<int:equipment_id>',
        type='http',
        auth='public',
        methods=['GET'],
        csrf=False
    )
    def get_equipment_by_id(self, equipment_id):
        equipment = request.env['device.equipment'].sudo().browse(equipment_id)
        if not equipment.exists():
            return request.make_json_response({'error': 'Equipment not found'}, status=404)
        data = {
            'id': equipment.id,
            'name': equipment.name,
            'serial_number': equipment.serial_number,
            'purchase_date': equipment.purchase_date,
            'price': equipment.price,
            'status': equipment.status,
            'employee_id': equipment.employee_id.id if equipment.employee_id else None,
            }
        return request.make_json_response(data)