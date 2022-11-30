# -*- coding: utf-8 -*-
from odoo.tests import common
from odoo.tests.common import tagged


@tagged("-standard", "common")
class TestCRMAttribute(common.TransactionCase):

    def setUp(self):
        super(TestCRMAttribute, self).setUp()
        self.crm_lead = self.env.ref("account_attributes_crm.crm_lead_test_demo")

    def test_write(self):
        """
        Test if the write function in crm_lead works
        """
        self.env["crm.lead"].write({
            "name": "CRM Leadss",
        })


