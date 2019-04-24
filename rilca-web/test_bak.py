'''
Created on Nov 30, 2018

@author: chayapan
'''
import unittest
import sqlite3
from sqlite3 import Error

import db

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
    
    def testCreateDatabaseFile(self):
        """Create database file using name specified in conf.py"""
        from conf import DATABASE_NAME, DATABASE_FILE
        import sqlite3
        from sqlite3 import Error 
        
        db_file = DATABASE_FILE
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        finally:
            conn.close()
    
    # def testStaff(self):
    #     self.cur.execute('''CREATE TABLE staffs
    #                         (Staff_id text PRIMARY KEY, First_name text, Last_name text, Password text, Email text, Phone text)''')
    #     self.con.commit()
 
    def testUser(self):
        """
            USER(User_id, First_name, Last_name, Password, Email, Phone_number)
        """
        self.cur.execute('''CREATE TABLE users
                            (User_id INTEGER PRIMARY KEY, First_name TEXT, Last_name TEXT, Password TEXT, Email TEXT, Phone_number TEXT''')
        self.con.commit()
    
    def testAcademicStaff(self):
        """
            ACADEMIC_STAFF(User_id, Title, Date_joined, Program_code)
        """
        self.cur.execute('''CREATE TABLE academic_staffs
                            (User_id text, Title text, Date_joined text, Program_code text)''')
        self.con.commit()

    def testAcademicProgram(self):
        """
            ACADEMIC_PROGRAM(Program_code, Name)
        """
        self.cur.execute('''CREATE TABLE academic_programs
                            (Program_code text PRIMARY KEY, Name text)''')
        self.con.commit()
    
    def testSupportingStaff(self):
        """
            SUPPORTING_STAFF(User_id)
        """
        self.cur.execute('''CREATE TABLE supporting_staffs
                            (User_id text)''')
        self.con.commit()
    
    def testExecutive(self):
        """
            EXECUTIVES(User_id, Title)
        """
        self.cur.execute('''CREATE TABLE executives
                            (User_id text, Title text)''')
        self.con.commit()

    def testPerformanceAgreement(self):
        """
            PERFORMANCE_AGREEMENT(Academic_year, Academic_staff_id, Status, Created_at, Created_by, Submitted_at, Reviewed_at, Reviewed_by, Approved_at, Approved_by, Period_start, Period_end)
        """
        self.cur.execute('''CREATE TABLE performance_agreements
                            (Academic_year text, Academic_staff_id text, Status text, Created_at text, Created_by text, Submitted_at, Reviewed_at, Reviewed_by, Approved_at, Approved_by Period_start, Period_end)''')
        self.con.commit()
    
    def testPerformanceReport(self):
        """
            PERFORMANCE_REPORT(Academic_year, Academic_staff_id, Report_date, Report_status, Support_staff_id, Created_at, Created_by, Total_score, Standard_performance_score, Developed_performance_score, Core_values_score)
        """
        self.cur.execute('''CREATE TABLE performance_reports
                            (Academic_year, Academic_staff_id, Report_date, Report_status, Support_staff_id, Created_at, Created_by, Total_score, Standard_performance_score, Developed_performance_score, Core_values_score)
                            ''')
        
        self.con.commit()
    
    def testActivity(self):
        """
            ACTIVITY(Activity_id, Academic_year, Academic_staff_id, Status, Work_code, Name, Description, Created_at, Created_by, Updated_at, Updated_by, Points_earned, Comment)
        """
        self.cur.execute('''CREATE TABLE performance_reports
                            ''')
        self.con.commit()
    
    def testWorkType(self):
        """
            WORK_TYPE(Work_code, Section_number, Question_number, Name, Description, Points)
        """
        
        self.cur.execute('''CREATE TABLE work_types
        WORK_TYPE(Work_code, Section_number, Question_number, Name, Description, Points)

                            ''')
        self.con.commit()
    
    def testChangeLog(self):
        """
            CHANGE_LOG(User_id, Timestamp, Table_name, Column_name, Old_value, New_value)
        """
        self.cur.execute('''CREATE TABLE work_types
        CHANGE_LOG(User_id, Timestamp, Table_name, Column_name, Old_value, New_value)


                            ''')
        self.con.commit()
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()