import unittest
from ..parser import pageParse
from ..parser import pageLoaderProcess as pls
import re
import os.path

res_dir = os.path.join( os.path.dirname(__file__) , "testSampleFiles" )

class SplitIntoEntries_tests(unittest.TestCase):

	def setUp(self):
		self.jobsListingSource = open( os.path.join(res_dir,"craigsListingSource.htm"), 'r')
		self.firstJobEntry = open( os.path.join(res_dir, "firstEntry.txt"), 'r')
		self.secondJobEntry = open( os.path.join(res_dir, "secondEntry.txt"), 'r')
		self.lastJobEntry = open( os.path.join(res_dir, "lastEntry.txt"), 'r')
		
		self.entriesList = pageParse.splitIntoEntries(self.jobsListingSource.read())

	def test_firstEntry(self):
		job = self.firstJobEntry.read()
		errorString = "Actual result: " + self.entriesList[0]
		errorString += "\n"
		errorString += "Desired result: " + job
		errorString += "\n"
		self.assertTrue(job==self.entriesList[0], errorString) 

	def test_secondEntry(self):
		job = self.secondJobEntry.read()	
		errorString = "Actual result: " + self.entriesList[1]
		errorString += "\n"
		errorString += "Desired result: " + job
		errorString += "\n"
		self.assertTrue(job==self.entriesList[1], errorString) 

	def test_lastEntry(self):
		job = self.lastJobEntry.read()
		errorString = "Actual result: " + self.entriesList[-1]
		errorString += "\n"
		errorString += "Desired result: " + job
		errorString += "\n"
		self.assertTrue(job==self.entriesList[-1], errorString) 
		
	def tearDown(self):
		self.jobsListingSource.close()
		self.firstJobEntry.close()
		self.secondJobEntry.close()
		self.lastJobEntry.close()

class extractPID_tests(unittest.TestCase):
	
	def setUp(self):
		self.firstJobEntry = open( os.path.join(res_dir, "firstEntry.txt"), 'r')	
		self.secondJobEntry = open( os.path.join(res_dir, "secondEntry.txt"), 'r')
		self.lastJobEntry = open( os.path.join(res_dir, "lastEntry.txt"), 'r')
		
	def test_extractPID_noExtractionErrors(self):
		self.assertIsNot(pageParse.extractPID(self.firstJobEntry.read()), -1, "Error in extractPID extraction algorithm")
		self.assertIsNot(pageParse.extractPID(self.secondJobEntry.read()), -1, "Error in extractPID extraction algorithm")	
		self.assertIsNot(pageParse.extractPID(self.lastJobEntry.read()), -1, "Error in extractPID extraction algorithm")

	def test_extractPID_correctPIDExtracted(self):
		firstPID = 4496353905
		secondPID = 4496348548
		lastPID = 4492280745
		
		PID = pageParse.extractPID(self.firstJobEntry.read())
		self.assertEqual(PID, firstPID, "Evaluated PID: {}  Actual PID: {}".format(PID, firstPID))

		PID = pageParse.extractPID(self.secondJobEntry.read())
		self.assertEqual(PID, secondPID, "Evaluated PID: {}  Actual PID: {}".format(PID, secondPID))

		PID = pageParse.extractPID(self.lastJobEntry.read())
		self.assertEqual(PID, lastPID, "Evaluated PID: {}  Actual PID: {}".format(PID, lastPID))

	def tearDown(self):
		self.firstJobEntry.close()
		self.secondJobEntry.close()
		self.lastJobEntry.close()

if __name__ == "__main__":
	unittest.main()
