{
    'name':"Employee Equipment",
    'author':'Ayman Jammaa',
    'category':'1',
    'version':'18.0.0.1',
    'depends':['base',
               'hr',
              ],
    'data':[
        'security/equipment_security.xml',
        'security/ir.model.access.csv',
        
        'views/equipment_view.xml',
        'views/hr_employee_view.xml',
        'views/base_menu.xml',
        
    ],

    'assets': {
        
    },


    'installable': True,
    'application': True,

}