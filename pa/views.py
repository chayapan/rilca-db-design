# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Sum
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from decimal import Decimal

from pa_items import PAItem, PAForm

class Form(TemplateView):
    template_name = "pa-form.html"
    def get(self, request):
        items = PAItem.loadFromWorkbook()
        form = PAForm(items)
        data = {"items": form.view_items}
        return render(request, self.template_name, data)