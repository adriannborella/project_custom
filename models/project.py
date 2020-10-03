# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProjectProject(models.Model):
    _inherit = 'project.project'

    def action_view_list_tasks(self):
        tree_view = self.env.ref('project_custom.view_tree_task_list_ui')
        
        return {
            'type': 'ir.actions.act_window',
            'name': 'Tasks List',
            'res_model': 'project.task',
            'view_mode': 'tree',
            'view_id' : tree_view.id,
            'target': 'current',    
            'context' : { 'search_default_project_id': self.id }        
        }

class ProjectTask(models.Model):
    _inherit = 'project.task'

    def edit_task(self):
        view = self.env.ref('project.view_task_form2')
        
        return {
            'type': 'ir.actions.act_window',
            'name': 'Tasks Form',
            'res_model': 'project.task',
            'view_mode': 'form',
            'view_id' : view.id,
            'target': 'new',    
            'res_id' : self.id
        }
    
