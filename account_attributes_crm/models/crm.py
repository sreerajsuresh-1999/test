# -*- coding: utf-8 -*-

from odoo import models, fields


class CRMAttribute(models.Model):
    _name = "crm.lead"
    _inherit = ["crm.lead", "account.attribute.mixin"]

    def write(self, vals):
        res = super(CRMAttribute, self).write(vals)
        self.crm_revenue_spreads.write(
            {
                "attribute1": self.attribute1.id,
                "attribute2": self.attribute2.id,
                "attribute3": self.attribute3.id,
            })
        return res


class CRMRevenueSpread(models.Model):
    _name = "crm.revenue.spread"
    _inherit = ["crm.revenue.spread", "account.attribute.mixin"]


