{
    'name':"Employee Equipment",
    'author':'Ayman Jammaa',
    'category':'',
    'version':'18.0.0.1',
    'depends':['base',
               'hr',
              ],
    'data':[
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/equipment_view.xml',
        'views/hr_employee_view.xml',
        
    ],

    'assets': {
        
    },


    'installable': True,
    'application': True,

}