# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class LeaveBalanceReport(models.Model):
    _name = 'leave.balance.report'
    _description = 'Time Off Utilization Report'

    employee_id = fields.Many2one('hr.employee', string="Employee")
    job_id = fields.Many2one('hr.job', string="Job", related='employee_id.job_id', readonly=True)
    department_id = fields.Many2one('hr.department', string="Department", related='employee_id.department_id', readonly=True, store=True)
    leave_type_id = fields.Many2one('hr.leave.type', string="Time Off Type")
    allocated_days = fields.Float(string="Allocated Days")
    taken_days = fields.Float(string="Taken Days")
    balance_days = fields.Float(string="Balance Days")
    utilization_rate = fields.Float(string="Utilization Rate", compute='_compute_utilization_rate')

    def _compute_utilization_rate(self):
        for rec in self:
            if rec.allocated_days != 0:
                rec.utilization_rate = rec.taken_days / rec.allocated_days 
            else:
                rec.utilization_rate = 0
        
    @api.model
    def action_leave_balance_report(self):

        self._cr.execute(""" 
            DELETE  FROM leave_balance_report
         """)
        self._cr.commit()
        
        employee_ids = self.env['hr.employee'].sudo().search([('active','=',True)])
        for employee_id in employee_ids:
            leave_allocation_ids = self.env['hr.leave.allocation'].sudo().search([('holiday_status_id.active','=',True),('employee_id','=',employee_id.id), ('state', '=', 'validate')])
            leave_ids = self.env['hr.leave'].sudo().search([('holiday_status_id.active','=',True),('employee_id','=',employee_id.id), ('state', '=', 'validate')])
            
            #sample dictionary to collect allocation balances and leaves taken:
            # balances_dict = { 
            #    leave_type_id: { 'allocated': x.x, 'taken': x.x},
            #    1: { 'allocated': 5.5, 'taken': 2.0},
            #    5: { 'allocated': 0.0, 'taken': 4.0},
            # }
            
            balances_dict = {}
            for allocation in leave_allocation_ids:
                if allocation.holiday_status_id.id not in balances_dict:
                    balances_dict[allocation.holiday_status_id.id] = {'allocated': allocation.number_of_days, 'taken': 0.0}
                else:
                    balances_dict[allocation.holiday_status_id.id]['allocated'] =  balances_dict[allocation.holiday_status_id.id]['allocated'] + allocation.number_of_days
            
            for leave in leave_ids:
                if leave.holiday_status_id.id not in balances_dict:
                    balances_dict[leave.holiday_status_id.id] = {'allocated': 0.0, 'taken': leave.number_of_days}
                else:
                    balances_dict[leave.holiday_status_id.id]['taken'] =  balances_dict[leave.holiday_status_id.id]['taken'] + leave.number_of_days
            
            leave_balance_report = self.env['leave.balance.report']
            for leave_type, child_dict in balances_dict.items():
                report_line = leave_balance_report.sudo().create({
                    'employee_id':employee_id.id,
                    'leave_type_id':leave_type,
                    'allocated_days':child_dict['allocated'],
                    'taken_days': child_dict['taken'],
                    'balance_days': child_dict['allocated'] - child_dict['taken'],
                })

        return {
            'name': _('Time Off Utilization'),
            'type': 'ir.actions.act_window',
            'res_model': 'leave.balance.report',
            'view_mode': 'tree,graph,pivot',
            'context': {
               'search_default_group_by_employee': True,
            }
        }
