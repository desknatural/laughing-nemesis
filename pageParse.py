import re
import datetime
import pageLoaderProcess as pls

MAXDATE = 28  # the maximum amount of days in the past any search will ever go

class craigJob:
	def __init__(self, PID=-1, title='',location='', date=datetime.date(1989, 6, 8) field ='', URL='', compensation='', body=''):
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



def readJobPage(pls.loader, baseURL, index=0):
	list_URL = baseURL	
	if index != 0:
			list_URL += "index" + index + ".html"
	source = loader.getPage(list_URL)

	entryStart_pattern = '<p class="row"'
	entryEnd_pattern = '</span> *</span> *</span> *</span> *</span> *</p>'
	PID_pattern = 'data-pid="([0-9]{10})"'
	# date_pattern = '<span class="date">([a-zA-Z0-9 ]{5-6})</span>'
	URLtitle_pattern = '<a href="([a-z0-9\./])+" class="i">([^<]+)</a>'
	loc_pattern = '<span class="pnr"> <small> \([^)]+)\)</small>'

	# can't do any more patterns, I'd need to open the individual pages in order to be able to do that!
	jobList = []
	# split the HTML into job chunks
	jobhtmls = re.split(entryStart_pattern, source)
	# extract relevant information
	for entry in jobhtmls:
		entry = (re.split(entryEnd_pattern, entry))[0]
		#We can't neccesarily assume that .groups() exists, because search can return a None object.
		PID = re.search(PID_pattern, entry).groups()[0] 
		URL, title = re.search(URLtitle_pattern, entry).groups()
		location = re.search(loc_pattern, entry).groups()[0]

		newJob = craigJob(date=date, PID=PID, URL=URL, location=location, title=title)
		jobList.append(newJob)
	
		# All that's left to do now is to extract the compensation, date and body of every job entry page
		entrySource = loader.getPage(URL)
		
		date_pattern = '<time datetime="([^"]+)">'
		bodyStart_pattern = '<section id="postingbody">'
		bodyEnd_pattern = '</section>'
		
		body = re.split(bodyStart_pattern, entrySource)[1]
		body = re.split(bodyEnd_pattern, body)[0]
		jobList[-1].body = body
		
		date_string = re.search(date_pattern, entrySource).groups()[0]
		#Currently script can only decipher dates for eastern standard time, will be fixed.
		jobList[-1].date = datetime.strptime(date_string, "%FT%H%:M%:S-0400")

		#The compensation is sort of difficult to do so I'll leave that for the future

	if len(jobList) == 0:
		return None
	else:
		return jobList
