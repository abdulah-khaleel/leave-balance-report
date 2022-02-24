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
    'name': "Time Off Utilization Report",   
    'summary': "A time off utilization report.",   
    'description': """
        A summary time off balance and utilization report for employees. 
    """,   
    'author': "Abdullah Khalil",
    'website': "https://github.com/abdulah-khaleel",
    'category': 'Time Off',
    'version': '15.0.0.0',
     "license": "LGPL-3",
    'depends': ['base','hr_holidays'],
    'data': [
        'security/ir.model.access.csv',
        'views/leave_balance_report.xml',
    ],
    'images': ["static/description/banner-v15.png"],
    'license': 'LGPL-3',
    'application': True,
    'installable': True,
} 
