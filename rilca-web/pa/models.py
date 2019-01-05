# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

import xlrd
from pa_items import PAItem
from api.models import PaItems as Item

def sync_pa_items():
    fname = """Physical Design - PA Items.xlsx"""
    sheet_name = "PAItems_v1"
    workbook = xlrd.open_workbook(fname)
    xl_sheet = workbook.sheet_by_name(sheet_name)
    # Print all values, iterating through rows and columns
    #
    num_cols = xl_sheet.ncols   # Number of columns
    for row_idx in range(2, xl_sheet.nrows):    # Iterate through rows
        print ('-'*40)
        print ('Row: %s' % row_idx)   # Print row number
        for col_idx in range(8, num_cols):  # Iterate through columns
            cell_obj = xl_sheet.cell(row_idx, col_idx)  # Get cell object by row, col
            print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))
            print xl_sheet.cell(row_idx, col_idx).value
        
        id = xl_sheet.cell(row_idx, 9).value
        if id == int(id):
            id = int(id)
        else:
            id = id
        
        level = xl_sheet.cell(row_idx, 10).value
        group = xl_sheet.cell(row_idx, 11).value
        parent = xl_sheet.cell(row_idx, 12).value
        display_rank = xl_sheet.cell(row_idx, 13).value
        form_xpath = xl_sheet.cell(row_idx, 14).value
        number = xl_sheet.cell(row_idx, 15).value
        score_points = xl_sheet.cell(row_idx, 16).value
        
        desc_en = xl_sheet.cell(row_idx, 0).value
        desc_th = xl_sheet.cell(row_idx, 4).value
        
        itm = PAItem(id, level, group, parent, display_rank, form_xpath, number, score_points, desc_en, desc_th)
        
        print itm.id, itm.level
        print "Syncing:", id, level
        if Item.objects.filter(item_id=id).count() == 0:
            print "Creating:", id, level, desc_th, desc_en
            # create Item
            Item.objects.create(item_id=id, 
                                level = level,
                                display_rank = display_rank,
                                description_en=desc_en,
                                description_th=desc_th)
        else:
            print "Exist:", id, level, desc_th, desc_en
            itm = Item.objects.filter(item_id=id).all()[0]
            print itm.item_id, itm.level
        
        print "Count:", Item.objects.count()