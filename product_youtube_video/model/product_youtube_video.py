# -*- coding: utf-8 -*-
from openerp import models, fields

class product_product(models.Model):
	_inherit = "product.template"
	_name = "product.template"
	youtube_id = fields.Char(string='Youtube ID')
