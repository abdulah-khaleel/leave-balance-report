# -*- coding: utf-8 -*-
################################################################################# 
#
#    Author: Abdullah Khalil. Copyrights (C) 2021-TODAY reserved. 
#
#    You may use this app as per the rules outlined in the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3. 
#    See <http://www.gnu.org/licenses/> for more detials.
#
################################################################################# 

{
    'name': "Time Off Balance Report",   
    'summary': "A time off balance report for employees.",   
    'description': """
        A detailed time off balance report for employees. 
    """,   
    'author': "Abdullah Khalil",
    'website': "https://github.com/abdulah-khaleel",
    'category': 'Time Off',
    'version': '15.0.0.0',
    'depends': ['base','hr_holidays'],
    'data': [
        'security/ir.model.access.csv',
        'views/leave_balance_report.xml',
    ],
    # 'images': ["static/description/banner.png"],
    'license': 'LGPL-3',
    'application': True,
    'installable': True,
} 
