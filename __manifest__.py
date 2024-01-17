# -*- coding: utf-8 -*- 


{
    'name': 'Link Prepress management,Sales and Warehouse Management',
    'author': 'Soft-integration',
    'application': True,
    'installable': True,
    'auto_install': False,
    'qweb': [],
    'description': False,
    'images': [],
    'version': '1.0.1.7',
    'category': 'Hidden',
    'demo': [],
    'depends': ['sale_stock','sale_prepress_management'],
    'data': [
        'views/stock_picking_views.xml',
        'report/report_deliveryslip.xml',
    ],
    'license': 'LGPL-3',
}
