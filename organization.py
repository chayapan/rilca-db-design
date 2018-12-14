'''
Created on Dec 14, 2018

@author: chayapan
'''
import unittest
import xlrd

WORKBOOK = """Physical Design - RILCA Organization.xlsx"""

class AcademicProgram:
    def __init__(self, id, program_chair, name_th, name_en):
        self.id = id
        self.program_chair = program_chair
        self.name_th = name_th
        self.name_en = name_en

    @classmethod
    def loadFromWorkbook(cls):
        """Returns dictionay of PAItem objects with ID as key."""
        programs = {}
        fname = WORKBOOK
        sheet_name = "AcademicProgram_v1"
        workbook = xlrd.open_workbook(fname)
        xl_sheet = workbook.sheet_by_name(sheet_name)
        num_cols = xl_sheet.ncols   # Number of columns
        for row_idx in range(2, xl_sheet.nrows):    # Iterate through rows
            for col_idx in range(1, num_cols):  # Iterate through columns
                cell_obj = xl_sheet.cell(row_idx, col_idx)  # Get cell object by row, col
                id = xl_sheet.cell(row_idx, 3).value
                program_chair = xl_sheet.cell(row_idx, 5).value
                name_th = xl_sheet.cell(row_idx, 6).value
                name_en = xl_sheet.cell(row_idx, 7).value                
                p = AcademicProgram(id=id,program_chair=program_chair,name_th=name_th,name_en=name_en)
                programs[id] = p
        return programs

class AcademicStaff:
    def __init__(self, id, program_id, first_name, last_name, rank):
        self.id = id
        self.program_id = program_id
        self.first_name = first_name
        self.last_name = last_name
        self.rank = rank

    @classmethod
    def loadFromWorkbook(cls):
        """Returns dictionay of PAItem objects with ID as key."""
        staffs = {}
        fname = WORKBOOK
        sheet_name = "AcademicStaff_v1"
        workbook = xlrd.open_workbook(fname)
        xl_sheet = workbook.sheet_by_name(sheet_name)
        num_cols = xl_sheet.ncols   # Number of columns
        for row_idx in range(2, xl_sheet.nrows):    # Iterate through rows
            for col_idx in range(1, num_cols):  # Iterate through columns
                cell_obj = xl_sheet.cell(row_idx, col_idx)  # Get cell object by row, col
                # id = xl_sheet.cell(row_idx, 3).value
                program_id = xl_sheet.cell(row_idx, 3).value
                first_name = xl_sheet.cell(row_idx, 4).value
                last_name = xl_sheet.cell(row_idx, 5).value
                rank = xl_sheet.cell(row_idx, 6).value
                
                # override:
                id = first_name + last_name
                s = AcademicStaff(id=id,program_id=program_id,first_name=first_name,last_name=last_name,rank=rank)
                staffs[id] = s
        return staffs

class SupportStaff:
    def __init__(self, id, program_id, first_name, last_name, position):
        self.id = id
        self.program_id = program_id
        self.first_name = first_name
        self.last_name = last_name
        self.position = position

    @classmethod
    def loadFromWorkbook(cls):
        """Returns dictionay of PAItem objects with ID as key."""
        staffs = {}
        fname = WORKBOOK
        sheet_name = "SupportStaff_v1"
        workbook = xlrd.open_workbook(fname)
        xl_sheet = workbook.sheet_by_name(sheet_name)
        num_cols = xl_sheet.ncols   # Number of columns
        for row_idx in range(2, xl_sheet.nrows):    # Iterate through rows
            for col_idx in range(1, num_cols):  # Iterate through columns
                cell_obj = xl_sheet.cell(row_idx, col_idx)  # Get cell object by row, col
                # id = xl_sheet.cell(row_idx, 3).value
                program_id = xl_sheet.cell(row_idx, 3).value
                first_name = xl_sheet.cell(row_idx, 4).value
                last_name = xl_sheet.cell(row_idx, 5).value
                position = xl_sheet.cell(row_idx, 6).value
                
                # override:
                id = first_name + last_name
                s = SupportStaff(id=id,program_id=program_id,first_name=first_name,last_name=last_name,position=position)
                staffs[id] = s
        return staffs

class ExecutiveStaff:
    def __init__(self, id, program_id, first_name, last_name, position):
        self.id = id
        self.program_id = program_id
        self.first_name = first_name
        self.last_name = last_name
        self.position = position

    @classmethod
    def loadFromWorkbook(cls):
        """Returns dictionay of PAItem objects with ID as key."""
        staffs = {}
        fname = WORKBOOK
        sheet_name = "ExecutiveStaff_v1"
        workbook = xlrd.open_workbook(fname)
        xl_sheet = workbook.sheet_by_name(sheet_name)
        num_cols = xl_sheet.ncols   # Number of columns
        for row_idx in range(2, xl_sheet.nrows):    # Iterate through rows
            for col_idx in range(1, num_cols):  # Iterate through columns
                cell_obj = xl_sheet.cell(row_idx, col_idx)  # Get cell object by row, col
                # id = xl_sheet.cell(row_idx, 3).value
                program_id = xl_sheet.cell(row_idx, 3).value
                first_name = xl_sheet.cell(row_idx, 4).value
                last_name = xl_sheet.cell(row_idx, 5).value
                position = xl_sheet.cell(row_idx, 6).value
                
                # override:
                id = first_name + last_name
                s = SupportStaff(id=id,program_id=program_id,first_name=first_name,last_name=last_name,position=position)
                staffs[id] = s
        return staffs

class Test(unittest.TestCase):

    def testExtractAcademicProgram(self):
        programs = AcademicProgram.loadFromWorkbook()
        print programs
    def testExtractAcademicStaff(self):
        staffs = AcademicStaff.loadFromWorkbook()
        print staffs
    def testExtractSupportStaff(self):
        staffs = SupportStaff.loadFromWorkbook()
        print staffs
    def testExtractExecutiveStaff(self):
        staffs = ExecutiveStaff.loadFromWorkbook()
        print staffs

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()