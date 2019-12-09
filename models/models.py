# -*- coding: utf-8 -*-

from odoo import models, fields, api


class vit_report_balance(models.Model):
    _name = "vit_report_balance.vit_report_balance"

    name = fields.Char("Name")
    date_start = fields.Date()
    date_end = fields.Date()
    company_id = fields.Many2one(comodel_name="res.company")
    report_details_ids = fields.One2many(
        comodel_name="vit_report_balance_so", inverse_name="report_id"
    )


class report_balance_so(models.Model):
    _name = "vit_report_balance_so"

    report_id = fields.Many2one(comodel_name="vit_report_balance.vit_report_balance")
    product_id = fields.Many2one(comodel_name="product.product")
    product_code = fields.Char()
    total_so_bln_lalu = fields.Float()
    total_so_bln_ini = fields.Float()
