import re
import datetime
import pageLoaderProcess as pls

MAXDATE = 28  # the maximum amount of days in the past any search will ever go
DEFAULT_DATE = datetime.date(1989, 6, 8)

class craigJob:
	def __init__(self, PID=-1, title='',location='', date=DEFAULT_DATE, field ='', URL='', compensation='', body=''):
		self.PID = PID
		self.title = title
		self.date = date
		self.location = location
		self.field = field
		self.URL = URL
		self.compensation = compensation
		self.body = body
	def __str__(self):
		string = "PID:" + PID + "\nURL:" + URL + "\nDate:" + date.stroftime("%a %d, %b %Y") + "\nLocation:" + location 
		string += "\nField:" + field + "\nCompensation:" + compensation + "\nBody:" + body
		return string

def splitIntoEntries(source):
	""" Takes the HTML source code input (source) for an entire page of Craigslist listings and splits them up into a list of individual 
	chunks of HTML corresponding to individual entries to later be processed """
	entryStart_pattern = '<p class="row" '
	entryEnd_pattern = '(?:</span> *){3}'
	jobHTMLs = re.split(entryStart_pattern, source)
	# The first entry will consist of unneeded header HTML before the first entry
	jobHTMLs.pop(0)
	for i, entry in enumerate(jobHTMLs):
		jobHTMLs[i] = (re.split(entryEnd_pattern, entry))[0]  #slices off from the end to ensure only the entry itself is left
	return jobHTMLs

def extractPID(source):
	""" Takes the HTML source code input (source) for an individual listing in a Craigslist listing page and extracts its PID """
	PID_pattern = 'data-pid="([0-9]{10})"'  
	results = re.search(PID_pattern, source)
	if results:
		return int((results.groups())[0])
	else:
		return -1

def extractLocation(source):
	""" Extracts the location information from the listings HTML chunk corresponding to one advertisement """
	loc_pattern = '<span class="pnr"> <small> \(([^\)]+)\)</small>'
	results = re.search(loc_pattern, source)
	if results:
		return results.groups()[0]
	else:
		return ''

def extractURLandTitle(source):
	""" Takes the source code for an ad listing returned by splitIntoEntries and itself returns the URL of the individual
	ad page and also the title of the advertisement itself """
	URLtitle_pattern = '<a href="([^"]+)">([^<]+)</a>'
	results = re.search(URLtitle_pattern, source)
	if results:
		return results.groups()[:2]

def extractBody(source):
	""" Given the HTML source for an individual advertisement page, extracts its body """
	bodyStart_pattern = '<section id="postingbody">'
	bodyEnd_pattern = '</section>'
	body = re.split(bodyStart_pattern, source)[1]
	body = re.split(bodyEnd_pattern, body)[0]
	return body

def extractDate(source):
	""" Strips the date and time from an individual advertisement page, turning it into a python datetime object and returning it """
	date_pattern = '<time datetime="([T0-9:\-]+)">'		
	search = re.search(date_pattern, source)
	if search:
		return datetime.strptime(search.groups()[0], '%FT%T%z')
	else:
		return DEFAULT_DATE

def readJobPage(loader, baseURL, index=0):
	list_URL = baseURL	
	if index != 0:
			list_URL += "index" + index + ".html"
	source = loader.getPage(list_URL)
	jobhtmls = splitIntoEntries(source)

	for entry in jobhtml:	
		newJob = craigJob()

		craigJob.PID = extractPID(entry)
		craigJob.location = extractLocation(entry)
		craigJob.URL , craigJob.title = extractURLandTitle(entry)
		jobList.append(newJob)
	
		# All that's left to do now is to extract the compensation, date and body of every job entry page
		entrySource = loader.getPage(URL)
		jobList[-1].body = extractBody(entrySource)
		jobList[-1].extractDate(entrySource)
		#The compensation is somewhat difficult so it'll be left for the future

	if len(jobList) == 0:
		return None
	else:
		return jobList
