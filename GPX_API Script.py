# Title: GPX_API Script
# Author: Ben Gaiarin (bgaiarin@ucsb.edu)

# Purpose: 
# This is a shorft Python script that extracts data from
# a .php URL as a GPX file. 

# The user of this script must input the URL and trip_id parameters 
# of their choosing in the command line. 

# This script was orginally written for scraping whale GPX data 
# for the Benioff Ocean Initiative's Whale Safe project. It is 
# only coded for that specific use case. 

# ------------------------------------------------------------

import sys
import csv 
import requests as req


### Defines messages shown to the user by the Chatbot. The
### Chatbot exists because it's fun and it helps the user 
### input their arguments correctly. 
class Chatbot: 
	def opener(self):
		return "\nWhat URL would you like to scrape data from?\n\n"
	def URLInvalid(self):
		return "\nWHOOPS! The URL is invalid.\n"
	def somethingFailed(self):
		return "\nWHOOPS! Something failed. Maybe you're missing a trip_id?\n"
	def paramsInvalid(self):
		return "\nWHOOPS! The trip_id you entered is invalid."
	def inputParam(self):
		return "\nPlease enter a trip_id number below. If entering multiple, separate by a comma.\n"
	def exit(self):
		return "\nWould you like to exit? (Type \"y\" or \"n\".)\n\n"


### Asks the user if they'd like to exit. If user 
### enters something other than "y" or "n", the prompt
### will repeat itself. 
def exit():
	a = input(bot.exit()).strip().lower()
	if (a == "y"):
		sys.exit()
	elif (a == "n"):
		main()
	else: 
		exit()


def main(): 
	url = input(bot.opener())
	#Check to see if URL is valid.
	try: 
		r = req.get(url)
	except: 
		print(bot.URLInvalid())
		exit()
	
	# Get trip_id parameter
	trip_id = input(bot.inputParam()).strip()
	if ("," not in trip_id):
		p = [trip_id]
	else:
		p = trip_id.split(",")

	for trip in p:
		p = {'trip_id':trip}
		# Get relevant GPX data from API
		try: 
			r = req.get(url, params=p)
		except: 
			if (params_dict == {}): print(bot.somethingFailed())
			else: print(bot.paramsInvalid())
			exit()

		# Write the GPX file
		s = trip + ".gpx"
		f = open(s, 'wb')
		f.write(r.content)
		f.close()



## Initializing the program. 
bot = Chatbot()
main()
