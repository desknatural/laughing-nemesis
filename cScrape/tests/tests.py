from ..parser import pageLoaderProcess as pls
from ..parser import pageParse
import re
import datetime

# Tests whether it's cURL ing correctly using common URLs
def getPage_Test1():
	loader = pls.pageLoadHandler() 
	source = loader.getPage("www.google.com")
	match = re.search("<!DOCTYPE html>", source)
	if not match:
		return False, "Test for whether getPage could load page correctly has failed."
	source = loader.getPage("www.yahoo.com")
	match = re.search("<!DOCTYPE html>", source)
	if not match:
		return False, "Test for whether getPage could load page correctly has failed."
	return True, "Test for whether getPage could load page correctly has passed."

# Tests how long getPage is waiting between subsequent requests and whether it's as expected.
def getPage_Test2():
	loader = pls.pageLoadHandler()
	wait_time = loader.getDelay()
	wait_delta = datetime.timedelta(seconds=wait_time)
	
	timeDiffs = []
	timeDiffs.append(datetime.timedelta())
	
	now = datetime.datetime.now()
	loader.getPage("www.example.org")
	loader.getPage("www.example.net")
	timeDiffs.append(now - datetime.datetime.now())
	loader.getPage("www.example.com")
	timeDiffs.append(now - datetime.datetime.now())
	loader.getPage("www.google.com")
	timeDiffs.append(now - datetime.datetime.now())
	
	#Not entirely sure if the next five lines are proper pythonic idiom
	timeDiffs2 = timeDiffs
	del timeDiffs2[0]  #This can probably be done by a list comprehension more pythonically
	for idx, diff in enumerate(timeDiffs2):
		if diff - timeDiffs2[idx] < wait_delta:
			return False, "Test for whether getPage waited the right amount of seconds (" + str(wait_time) +") has failed."
	return True, ("Test for whether getPage waited the right amount of seconds (" + str(wait_time) + ") has passed!")

def pageParse_Test1():
	loader = pls.pageLoadHandler()
	jobs = pageParse.readJobPage(loader, "newyork.craigslist.org/ofc/")
	print "pageParse_Test1() output"
	print "\n \n \n"
	for job in jobs:
		print job
		print "------------------------------------------------------------------------------\n"
	return True, "Look at printed output.  If correct, then this test has passed."
