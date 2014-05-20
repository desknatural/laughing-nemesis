import datetime
import subprocess
import time

#possible error when changing between timezones while program is running, consider preemptive fix

CL_REQUERY_WAIT_TIME = datetime.timedelta(seconds=2)
ZERO_TIME = datetime.timedelta()

class pageLoadHandler:
	def __init__(self):
		self.lastRequestTime = datetime.datetime.now() # Initialize our current time

	def getPage(self, url):
		requestTimeDifference = self.lastRequestTime - datetime.datetime.now()
		timeUntilLoad = CL_REQUERY_WAIT_TIME - requestTimeDifference
		if timeUntilLoad > ZERO_TIME:
			time.sleep( timeUntilLoad.total_seconds() )
		self.lastRequestTime = datetime.datetime.now()
		source = subprocess.check_output(["curl", url])
		return source 
	def getDelay(self):
		return CL_REQUERY_WAIT_TIME.total_seconds()
	
