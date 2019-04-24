'''
Created on Nov 30, 2018

@author: chayapan
'''
import unittest
import sqlite3
from sqlite3 import Error

import db
from pa_items import PAItem

class Test(unittest.TestCase):

    def setUp(self):
        conn = sqlite3.connect(":memory:")
        self.con = conn
        self.cur = conn.cursor()

    def tearDown(self):
        print "DUMP SQL...\n"

        for line in self.con.iterdump():
            print line + "\n"
        print "END."

    def testName(self):
        assert(isinstance(db.FILE, str))
    
    # def testStaff(self):
    #     self.cur.execute('''CREATE TABLE staffs
    #                         (Staff_id text PRIMARY KEY, First_name text, Last_name text, Password text, Email text, Phone text)''')
    #     self.con.commit()
 
    def testUser(self):
        """
            USER(User_id, First_name, Last_name, Password, Email, Phone_number)
        """
        self.cur.execute('''CREATE TABLE users (User_id INTEGER PRIMARY KEY, First_name TEXT, Last_name TEXT, Password TEXT, Email TEXT, Phone_number TEXT)''')
        self.con.commit()
    
    def testAcademicStaff(self):
        """
            ACADEMIC_STAFF(User_id, Title, Date_joined, Program_code)
        """
        self.cur.execute('''CREATE TABLE academic_staffs (User_id INTEGER, Title text, Date_joined text, Program_code text)''')
        self.con.commit()

    def testAcademicProgram(self):
        """
            ACADEMIC_PROGRAM(Program_code, Name)
        """
        self.cur.execute('''CREATE TABLE academic_programs (Program_code text PRIMARY KEY, Name text)''')
        self.con.commit()
    
    def testSupportingStaff(self):
        """
            SUPPORTING_STAFF(User_id)
        """
        self.cur.execute('''CREATE TABLE supporting_staffs (User_id INTEGER)''')
        self.con.commit()
    
    def testExecutive(self):
        """
            EXECUTIVES(User_id, Title)
        """
        self.cur.execute('''CREATE TABLE executives (User_id INTEGER, Title text)''')
        self.con.commit()

    def testPerformanceAgreement(self):
        """
            PERFORMANCE_AGREEMENT(Academic_year, Academic_staff_id, Status, Created_at, Created_by, Submitted_at, Reviewed_at, Reviewed_by, Approved_at, Approved_by, Period_start, Period_end)
        """
        self.cur.execute('''CREATE TABLE performance_agreements
                            (Academic_year INTEGER, Academic_staff_id INTEGER, Status TEXT, Created_at TEXT, Created_by INTEGER, Submitted_at TEXT, Reviewed_at, Reviewed_by INTEGER, Approved_at TEXT, Approved_by INTEGER, Period_start TEXT, Period_end TEXT)''')
        self.con.commit()
    
    def testPerformanceReport(self):
        """
            PERFORMANCE_REPORT(Academic_year, Academic_staff_id, Report_date, Report_status, Support_staff_id, Created_at, Created_by, Total_score, Standard_performance_score, Developed_performance_score, Core_values_score)
        """
        self.cur.execute('''CREATE TABLE performance_reports
                            (Academic_year INTEGER, Academic_staff_id INTEGER, Report_date TEXT, Report_status TEXT, Support_staff_id INTEGER, Created_at TEXT, Created_by INTEGER, Total_score REAL, Standard_performance_score REAL, Developed_performance_score REAL, Core_values_score REAL)
                            ''')
        
        self.con.commit()
    
    def testActivity(self):
        """
            ACTIVITY(Activity_id, Academic_year, Academic_staff_id, Status, Work_code, Name, Description, Created_at, Created_by, Updated_at, Updated_by, Points_earned, Comment)
        """
        self.cur.execute('''CREATE TABLE activities
                            (Activity_id INTEGER PRIMARY KEY, Academic_year INTEGER, Academic_staff_id INTEGER, Status TEXT, Work_code, Name, Description, Created_at, Created_by, Updated_at, Updated_by, Points_earned, Comment)
                            ''')
        self.con.commit()
    
    def testWorkType(self):
        """
            WORK_TYPE(Work_code, Section_number, Question_number, Name, Description, Points)
        """
        
        self.cur.execute('''CREATE TABLE work_types
                                (Work_code INTEGER PRIMARY KEY, Section_number TEXT, Question_number TEXT, Name TEXT, Description TEXT, Points INTEGER)
                                ''')
        self.con.commit()
    
    def testChangeLog(self):
        """
            CHANGE_LOG(User_id, Timestamp, Table_name, Column_name, Old_value, New_value)
        """
        self.cur.execute('''CREATE TABLE change_logs
                                (User_id INTEGER, Timestamp INTEGER, Table_name TEXT, Column_name TEXT, Old_value TEXT, New_value TEXT)
                                ''')
        self.con.commit()
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()