'''
Created on Dec 14, 2018

@author: chayapan
'''
import unittest
import json
import os

class PADocument:
    def __init__(self, filename, json_data):
        self.folder, self.filename = os.path.split(filename)
        self._json = json_data
        # Construct the line items
        if "lines" in json_data:
            self.lines = json_data["lines"]
        else:
            self.lines = {}
    @property
    def year(self):
        return self.filename.split("_")[0]
    @property
    def staff_id(self):
        return self.filename.split("_")[1][:-len(".json")]
    @property
    def next_line_number(self):
        line_number = len(self.lines) + 1 # line number for this item
        return line_number
    
    def add_item(self, pa_id, pa_desc_th, pa_desc_en, detail, score):
        print "Adding", pa_id, pa_desc_th, pa_desc_en, detail, score
        line_number = self.next_line_number
        # Add to instance
        self.lines[line_number] = {"id": pa_id, "desc_th": pa_desc_th, "desc_en": pa_desc_en, "detail": detail, "score": score}
        # Add to store
        self._json["lines"] = self.lines
        return True
    def remove_line(self, line_number):
        new_lines = {}
        c = 1
        for k, line in self.lines.items():
            if not int(line_number) == int(k): # Both are integer
                new_lines[c] = line
                c += 1
        self.lines = new_lines
        # Add to store
        self._json["lines"] = self.lines
        print "Removing", line_number
        return True
    def save(self):
        pa_file = os.path.join(self.folder, self.filename)
        with open(pa_file, "w") as f:
            json_data = json.dumps(self._json, sort_keys=True, indent=4)
            f.write(json_data)
            # print json_data
            print self.filename
        return True
    def asJSON(self):
        json_data = json.dumps(self._json, sort_keys=True, indent=4)
        return json_data
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