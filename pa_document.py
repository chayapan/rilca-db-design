'''
Created on Dec 14, 2018

@author: chayapan
'''
import unittest
import json
import os

class PADocument:
    def __init__(self, filename, json_data):
        self.filename = os.path.split(filename)[1]
        self._json = json_data
    @property
    def year(self):
        return self.filename.split("_")[0]
    @property
    def staff_id(self):
        return self.filename.split("_")[1][:-len(".json")]
    @classmethod 
    def fromFile(cls, filename):
        with open(filename, "r") as f:
            json_data = json.loads(f.read())
        return cls(filename, json_data)
    @classmethod
    def listFolder(cls):
        from django.conf import settings
        pa_folder = settings.DOCUMENT_FOLDER
        return os.listdir(pa_folder)

class Test(unittest.TestCase):


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()