# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Sum
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.http import HttpResponseServerError
from decimal import Decimal
import os, os.path

from pa_items import PAItem, PAForm, WORKBOOK1
from pa_document import PADocument
from organization import AcademicStaff, AcademicProgram, SupportStaff, ExecutiveStaff, WORKBOOK

class Form(TemplateView):
    template_name = "pa-form.html"
    def get(self, request):
        items = PAItem.loadFromWorkbook()
        form = PAForm(items)
        data = {"items": form.view_items}
        return render(request, self.template_name, data)

class ItemList(TemplateView):
    """Show list of PAItems in the system ina  simple HTML page."""
    template_name = "list-items.html"
    def get(self, request):
        items = PAItem.loadFromWorkbook()
        form = PAForm(items)
        data = {"items": form.view_items}
        data["workbook1"] = WORKBOOK1
        return render(request, self.template_name, data)

class Organization(TemplateView):
    """Show list of Academic Program, Academic Staff, Support Staff, Executive Staff in the system."""
    template_name = "organization.html"
    def get(self, request):
        programs= AcademicProgram.loadFromWorkbook()
        academic_staffs= AcademicStaff.loadFromWorkbook()
        support_staffs= SupportStaff.loadFromWorkbook()
        executive_staffs= ExecutiveStaff.loadFromWorkbook()
        data = {}
        data['programs'] = programs
        data['academic_staffs'] = academic_staffs
        data['support_staffs'] = support_staffs
        data['executive_staffs'] = executive_staffs
        data["workbook"] = WORKBOOK
        return render(request, self.template_name, data)

class NewDocument(TemplateView):
    """Display HTML page for creating new Performance Agreement."""
    template_name = "create-document.html"
    def get(self, request):
        items = PAItem.loadFromWorkbook()
        academic_staffs = AcademicStaff.loadFromWorkbook()
        support_staffs = SupportStaff.loadFromWorkbook()
        programs = AcademicProgram.loadFromWorkbook()
        form = PAForm(items)
        data = {"items": form.view_items}
        data['academic_staffs'] = academic_staffs
        data['support_staffs'] = support_staffs
        data['programs'] = programs
        return render(request, self.template_name, data)
    def post(self, request):
        print request.POST
        support_staff_id = request.POST.get('support-staff')
        academic_staff_id = request.POST.get('academic-staff')
        fiscal_year = request.POST.get('fiscal-year')
        padoc_filename = """%s_%s.json""" % (fiscal_year, academic_staff_id)
        pa_file = os.path.join(settings.DOCUMENT_FOLDER, padoc_filename)
        if os.path.exists(pa_file):
            return HttpResponseServerError("Active Document Already Exists")
        else:
            with open(pa_file,"w") as f:
                f.write("{}") # Touch open file.
        print pa_file
        data = {}
        return HttpResponseRedirect(reverse("fill-document",kwargs={"year": fiscal_year,"staff_id": academic_staff_id}))
        
class FillDocument(TemplateView):
    """Display HTML page for creating new Performance Agreement."""
    template_name = "fill-document.html"
    def get(self, request, year, staff_id):
        academic_staff_id = staff_id
        fiscal_year = year
        padoc_filename = """%s_%s.json""" % (fiscal_year, academic_staff_id)
        pa_file = os.path.join(settings.DOCUMENT_FOLDER, padoc_filename)
        if not os.path.exists(pa_file):
            return HttpResponseServerError("Document Does Not Exists")
        
        # Load document file from JSON
        document = PADocument.fromFile(pa_file)
        
        # Load data from database
        staffs = AcademicStaff.loadFromWorkbook() 
        staff = staffs[academic_staff_id]
        data = {"year": fiscal_year,"staff_id": academic_staff_id}
        data['academic_staff'] = staff
        data['document'] = document

        # Load PAItems for use        
        pa_items = PAItem.loadFromWorkbook()
        data["items"] = PAForm(pa_items).view_items

        return render(request, self.template_name, data)

class DocumentList(TemplateView):
    template_name = "list-documents.html"
    def get(self, request):
        files = PADocument.listFolder()
        documents = []
        for f in files:
            pa_file = os.path.join(settings.DOCUMENT_FOLDER, f)
            if os.path.exists(pa_file):
                document = PADocument.fromFile(pa_file)
                documents.append(document)
        data = {}
        data["files"] = files
        data["documents"] = documents
        print documents
        return render(request, self.template_name, data)
    