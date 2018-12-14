'''
Created on Dec 12, 2018

@author: chayapan
'''
import unittest
import xlrd
from collections import OrderedDict

WORKBOOK1 = """Physical Design - PA Items.xlsx"""

class PAItem:
    def __init__(self, id, level, group, parent, display_rank, form_xpath, number, score_points, desc_en, desc_th):
        self.id = id
        self.level = level
        self.group = group 
        self.parent = parent
        self.display_rank = display_rank
        self.form_xpath = form_xpath
        self.number = number
        self.score_points = score_points
        self.desc_en = desc_en
        self.desc_th = desc_th
        
        self.parent_id = None
    def findParent(self, items):
        if self.parent == 'NULL' or not self.parent:
            return None
        else:
            if self.parent == int(self.parent):
                id = int(self.parent)
            else:
                id = self.parent
            self.parent_id = id
            return items[id]
    def findChildren(self, items):
        children = []
        for i, pa in items.iteritems():
            if pa.parent_id == self.id:
                children.append(pa)
        return children
        
    @classmethod
    def loadFromWorkbook(cls):
        """Returns dictionay of PAItem objects with ID as key."""
        pa_items = {}
        fname = WORKBOOK1
        sheet_name = "PAItems_v1"
        workbook = xlrd.open_workbook(fname)
        xl_sheet = workbook.sheet_by_name(sheet_name)
        # Print all values, iterating through rows and columns
        #
        num_cols = xl_sheet.ncols   # Number of columns
        for row_idx in range(2, xl_sheet.nrows):    # Iterate through rows
            # ID
            id = xl_sheet.cell(row_idx, 9).value
            if id == int(id):
                id = int(id)
            else:
                id = id
            
            level = xl_sheet.cell(row_idx, 10).value
            group = xl_sheet.cell(row_idx, 11).value
            parent = xl_sheet.cell(row_idx, 12).value
            # print id, parent
            
            display_rank = xl_sheet.cell(row_idx, 13).value
            form_xpath = xl_sheet.cell(row_idx, 14).value
            number = xl_sheet.cell(row_idx, 15).value
            score_points = xl_sheet.cell(row_idx, 16).value
            
            desc_en = xl_sheet.cell(row_idx, 0).value
            desc_th = xl_sheet.cell(row_idx, 4).value
            
            pa_item = PAItem(id, level, group, parent, display_rank, form_xpath, number, 
                                score_points, desc_en, desc_th)
            pa_items[id] = pa_item
        
        # Locate parent node for all.
        for i, pa in pa_items.iteritems():
            pa.findParent(pa_items)
        return pa_items

class PAGroup:
    def __init__(self, item, hierarchy):
        self._item = item
        self._items = hierarchy
    @classmethod
    def fromDictionary(cls, items):
        item_groups = []
        for i, pa in items.iteritems():
            if pa.level == '1:itemGroup':
                g = PAGroup(pa, items)
                item_groups.append(g)
        return item_groups
        
class PACategory:
    def __init__(self, item, hierarchy):
        self._item = item
        self._items = hierarchy
    @classmethod
    def fromDictionary(cls, items):
        categories = []
        for i, pa in items.iteritems():
            if pa.level == '2:itemCategory':
                c = PACategory(pa, items)
                categories.append(c)
        return categories

class PAClass:
    def __init__(self, item, hierarchy):
        self._item = item
        self._items = hierarchy
    
    @property
    def hierarchy(self):
        """Ordered list of PAItem in hierarchy."""
        
        traverse = lambda this, hierarchy: hierarchy[this.parent_id]
        stop = False #
        current = self._item
        tree = [current]
        while not stop:
            if current.parent == 'NULL': # Root reached
                stop = True
                break
            parent = traverse(current, self._items)
            tree.append(parent)
            current = parent
        tree.reverse()
        return tree
    
    @property
    def hierarchy_summary(self):
        summary = """"""
        for p in self.hierarchy:
            summary += """ / """ + p.desc_th # + """(%s)""" % p.desc_en
        return summary

    @property
    def hierarchy_summary_en(self):
        summary = """"""
        for p in self.hierarchy:
            summary += """ / """ + p.desc_en # + """(%s)""" % p.desc_en
        return summary
        
    @classmethod
    def fromDictionary(cls, items):
        selectable = []
        for i, pa in items.iteritems():
            if pa.level == '3:itemClass':
                c = PAClass(pa, items)
                selectable.append(c)
        return selectable

class PAPart:
    def __init__(self, item, hierarchy):
        self._item = item
        self._items = hierarchy
    @classmethod
    def fromDictionary(cls, items):
        sections = []
        for i, pa in items.iteritems():
            if pa.level == '0:scorePart':
                p = PAPart(pa, items)
                sections.append(p)
        return sections

class PAForm:
    """Represents form object in the view that render as HTML."""
    def __init__(self, items):
        self.items = items
        self.categories = PACategory.fromDictionary(items)
        self.groups = PAGroup.fromDictionary(items)
        self.classes = PAClass.fromDictionary(items)
        self.sections = PAPart.fromDictionary(items)
        
        # Roots
        self.roots = [p for i, p in self.items.iteritems() if p.parent == 'NULL' ]
        
        # Ordered items for view rendering
        self.view_items = {}
        for i, pa in self.items.iteritems():
            if pa.level == "3:itemClass":
                # print "//", PAClass(child,self.items).hierarchy_summary
                self.view_items[pa] = PAClass(pa,self.items)
        self.view_items = OrderedDict(sorted(self.view_items.items(), key=lambda t: t[1]._item.id)) # Use PAClass instance attr for sorting
        
    def print_items(self):
        for r in self.roots:
            print r.desc_en
            self.print_children(r)
            
    def print_children(self, r):
        for child in r.findChildren(self.items):
            print child.number, child.desc_en, child.desc_th, child.score_points, child.id
            if child.level == "3:itemClass":
                print "//", PAClass(child,self.items).hierarchy_summary
            if child.findChildren(self.items):
                self.print_children(child)
        
class Test(unittest.TestCase):

    def testName(self):
        print "Import Excel"
        fname = """Physical Design - PA Items.xlsx"""
        sheet_name = "PAItems_v1"
        workbook = xlrd.open_workbook(fname)
        sheet = workbook.sheet_by_name(sheet_name)
        print sheet
        
    def testLoadFromWorkbook(self):
        pa_items = PAItem.loadFromWorkbook()
        print pa_items.keys()
    
    def testPrintRows(self):
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
            
            pa_item = PAItem(id, level, group, parent, display_rank, form_xpath, number, score_points, desc_en, desc_th)
            print pa_item

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()