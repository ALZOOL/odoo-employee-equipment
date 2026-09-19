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

    @http.route(
        '/api/equipment',
        type='http',
        auth='public',
        methods=['POST'],
        csrf=False
    )
    def create_equipment(self):

        data = request.get_json_data()

        equipment_record = request.env['device.equipment'].sudo().create({
            'name': data.get('name'),
            'serial_number': data.get('serial_number'),
            'purchase_date': data.get('purchase_date'),
            'price': data.get('price'),
            'active': data.get('active', True),
            'status': data.get('status'),
        })

        return request.make_json_response({
            'message': 'Equipment created successfully',
            'id': equipment_record.id,
            'name': equipment_record.name,
        }, status=201)


    @http.route(
    '/api/equipment/<int:equipment_id>',
    type='http',
    auth='public',
    methods=['PUT'],
    csrf=False
    )
    def update_equipment(self, equipment_id):

        equipment_record = request.env['device.equipment'].sudo().browse(equipment_id)

        if not equipment_record.exists():
            return request.make_json_response({
                'error': 'Equipment not found'
            }, status=404)

        data = request.get_json_data()

        equipment_record.write({
            'name': data.get('name', equipment_record.name),
            'serial_number': data.get('serial_number', equipment_record.serial_number),
            'price': data.get('price', equipment_record.price),
            'status': data.get('status', equipment_record.status),
            'active': data.get('active', equipment_record.active),
        })

        return request.make_json_response({
            'message': 'Equipment updated successfully',
            'id': equipment_record.id
        })
    @http.route(
    '/api/equipment/<int:equipment_id>',
    type='http',
    auth='public',
    methods=['DELETE'],
    csrf=False
    )
    def delete_equipment(self, equipment_id):

        equipment_record = request.env['device.equipment'].sudo().browse(equipment_id)

        if not equipment_record.exists():
            return request.make_json_response({
                'error': 'Equipment not found'
            }, status=404)

        equipment_record.unlink()

        return request.make_json_response({
            'message': 'Equipment deleted successfully'
        })