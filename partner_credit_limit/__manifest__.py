# See LICENSE file for full copyright and licensing details.

{
    'name': 'Partner Credit Limit',
    'version': '12.0.1.0.0',
    'category': 'Partner',
    'license': 'AGPL-3',
    'author': 'Tiny, Serpent Consulting Services Pvt. Ltd.',
    'website': 'http://www.serpentcs.com',
    'maintainer': 'Serpent Consulting Services Pvt. Ltd.',
    'summary': 'Set credit limit warning',
    'depends': [
<<<<<<< HEAD
        'sale_management',
    ],
    'data': [
        'views/partner_view.xml',
=======
        'sale_management','stock'
    ],

    'data': [
	'data/picking_state_data.xml',
	'security/stock_security.xml',
        'views/partner_view.xml',
	'views/stock_picking_view.xml'
>>>>>>> cc8feee8d2d449dee45ac4235615e81f2ccc59e9
    ],
    'installable': True,
    'auto_install': False,
}
