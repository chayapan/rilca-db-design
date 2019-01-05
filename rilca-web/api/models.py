# -*- coding: utf-8 -*-# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AcademicProgram(models.Model):
    program = models.ForeignKey('AcademicStaff', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'academic_program'


class AcademicStaff(models.Model):
    staff = models.ForeignKey('Staffs', models.DO_NOTHING, primary_key=True)
    program_id = models.CharField(max_length=45, blank=True, null=True)
    rank = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'academic_staff'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Executive(models.Model):
    staff = models.ForeignKey('Staffs', models.DO_NOTHING, primary_key=True)
    position = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'executive'


class PaApprovals(models.Model):
    approve_id = models.IntegerField(primary_key=True)
    document = models.ForeignKey('PaDocuments', models.DO_NOTHING, blank=True, null=True)
    executive = models.ForeignKey(Executive, models.DO_NOTHING, blank=True, null=True)
    approve_date = models.DateField(blank=True, null=True)
    update_by = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pa_approvals'


class PaDocuments(models.Model):
    document_id = models.IntegerField(primary_key=True)
    staff = models.ForeignKey('Staffs', models.DO_NOTHING, blank=True, null=True)
    program = models.ForeignKey(AcademicProgram, models.DO_NOTHING, blank=True, null=True)
    document_number = models.CharField(max_length=45, blank=True, null=True)
    fiscal_year = models.CharField(max_length=45, blank=True, null=True)
    submit_date = models.DateTimeField(blank=True, null=True)
    approve_date = models.DateTimeField(blank=True, null=True)
    period_start = models.DateField(blank=True, null=True)
    period_end = models.DateField(blank=True, null=True)
    review_date = models.DateTimeField(blank=True, null=True)
    score_date = models.DateTimeField(blank=True, null=True)
    accept_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pa_documents'


class PaItems(models.Model):
    item_id = models.IntegerField(primary_key=True)
    level = models.CharField(max_length=45)
    parent = models.IntegerField(blank=True, null=True)
    display_rank = models.IntegerField(blank=True, null=True)
    item_number = models.CharField(max_length=45, blank=True, null=True)
    score_points = models.CharField(max_length=45, blank=True, null=True)
    section_number = models.CharField(max_length=45, blank=True, null=True)
    description_th = models.CharField(max_length=500, blank=True, null=True)
    description_en = models.CharField(max_length=500, blank=True, null=True)
    hint_th = models.CharField(max_length=500, blank=True, null=True)
    hint_en = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pa_items'


class PaLines(models.Model):
    line_id = models.IntegerField(primary_key=True)
    program = models.ForeignKey(AcademicProgram, models.DO_NOTHING, blank=True, null=True)
    document = models.ForeignKey(PaDocuments, models.DO_NOTHING, blank=True, null=True)
    line_number = models.CharField(max_length=45, blank=True, null=True)
    item = models.ForeignKey(PaItems, models.DO_NOTHING, blank=True, null=True)
    description_th = models.CharField(max_length=500, blank=True, null=True)
    description_en = models.CharField(max_length=500, blank=True, null=True)
    specific_details = models.CharField(max_length=500, blank=True, null=True)
    score_plan = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    score_actual = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    score_deadline = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pa_lines'


class Staffs(models.Model):
    staff_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staffs'


class SupportStaff(models.Model):
    staff = models.ForeignKey(Staffs, models.DO_NOTHING, primary_key=True)
    position = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'support_staff'
