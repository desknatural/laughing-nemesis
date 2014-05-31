import unittest
import ..parser pageParse
import ..parser pageLoaderProcess as pls
import re
import os.path

class SplitIntoEntries_tests(unittest.TestCase):

	def setUp(self):
		self.jobsListingSource = open( os.path.join("testSampleFiles","craigsListingSource.htm"), 'r')
		self.firstJobEntry = open( os.path.join("testSampleFiles", "firstEntry.txt"), 'r')
		self.secondJobEntry = open( os.path.join("testSampleFiles", "secondEntry.txt"), 'r')
		self.lastJobEntry = open( os.path.join("testSampleFiles", "lastEntry.txt"), 'r')
		
		self.entriesList = splitIntoEntries(jobsListingSource.read())

	def test_firstEntry(self):
		job = self.firstJobEntry.read()
		errorString = "Actual result: " + self.entriesList[0]
		errorString += "\n"
		errorString += "Desired result: " + job
		errorString += "\n"
		self.assertTrue(Job==self.entriesList[0], errorString) 

	def test_secondEntry(self):
		job = self.secondJobEntry.read()	
		errorString = "Actual result: " + self.entriesList[1]
		errorString += "\n"
		errorString += "Desired result: " + job
		errorString += "\n"
		self.assertTrue(Job==self.entriesList[1], errorString) 

	def test_lastEntry(self):
		job = self.lastJobEntry.read()
		errorString = "Actual result: " + self.entriesList[-1]
		errorString += "\n"
		errorString += "Desired result: " + job
		errorString += "\n"
		self.assertTrue(Job==self.entriesList[-1], errorString) 
		
	def tearDown(self):
		jobsListingSource.close()
		firstJobEntry.close()
		secondJobEntry.close()
		lastJobEntry.close()

class extractPID_tests(unittest.TestCase):
	
	def setUp(self):
		self.firstJobEntry = open( os.path.join("testSampleFiles", "firstEntry.txt"), 'r')	
		self.secondJobEntry = open( os.path.join("testSampleFiles", "secondEntry.txt"), 'r')
		self.lastJobEntry = open( os.path.join("testSampleFiles", "lastEntry.txt"), 'r')
		
	def test_extractPID_noExtractionErrors(self):
		self.assertIsNot(extractPID(self.firstJobEntry.read()), -1, "Error in extractPID extraction algorithm")
		self.assertIsNot(extractPID(self.secondJobEntry.read()), -1, "Error in extractPID extraction algorithm")	
		self.assertIsNot(extractPID(self.lastJobEntry.read()), -1, "Error in extractPID extraction algorithm")

	def test_extractPID_correctPIDExtracted(self):
		firstPID = 4496353905
		secondPID = 4496348548
		lastPID = 4492280745
		
		PID = extractPID(self.firstJobEntry.read())
		self.assertEqual(PID, firstPID, "Evaluated PID: {}  Actual PID: {}".format(PID, firstPID))

		PID = extractPID(self.secondJobEntry.read())
		self.assertEqual(PID, secondPID, "Evaluated PID: {}  Actual PID: {}".format(PID, secondPID))

		PID = extractPID(self.lastJobEntry.read())
		self.assertEqual(PID, lastPID, "Evaluated PID: {}  Actual PID: {}".format(PID, lastPID))

	def tearDown(self):
		firstJobEntry.close()
		secondJobEntry.close()
		lastJobEntry.close()

