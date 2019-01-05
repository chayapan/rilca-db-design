# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

class Test(TestCase):

    def testItemsLoadAndIncludeInForm(self):
        from pa_items import PAForm, PAItem
        items = PAItem.loadFromWorkbook()
        form = PAForm(items)
        form.print_items()

    def testViewItems(self):
        from pa_items import PAForm, PAItem
        items = PAItem.loadFromWorkbook()
        form = PAForm(items)
        print form.view_items