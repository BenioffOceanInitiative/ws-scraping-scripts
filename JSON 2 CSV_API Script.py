# Title: JSON 2 CSV_API Script
# Author: Ben Gaiarin (bgaiarin@ucsb.edu)

# Purpose: 
# This is a short Python script that extracts data from
# a .php URL as a JSON string and converts those data into 
# a CSV file for visualization and manipulation. 

# The user of this script must input the URL and parameters 
# of their choosing in the command line. 

# The API's JSON data output must be a list of 
# dictionaries with consistent keys; the only exception to this is the 
# hard-coded case where a nested dictionary of 
# {'count':__, 'results':[{__}, {__}, ...]}, where the value of 'results'
# is a list of dictionaries with consistent keys, is the given output. 

# This script was orginally written for scraping whale sighting data 
# for the Benioff Ocean Initiative's Whale Safe project. 

# ------------------------------------------------------------

import sys
import requests as req 
import json 
import csv 
import ast 

### Defines messages shown to the user by the Chatbot. The
### Chatbot exists because it's fun and it helps the user 
### input their arguments correctly. 
class Chatbot: 
	def opener(self):
		return "\nWhat URL would you like to scrape data from?\n\n"
	def URLInvalid(self):
		return "\nWHOOPS! The URL is invalid.\n"
	def somethingFailed(self):
		return "\nWHOOPS! Something failed. Maybe you're missing some required parameters?\n"
	def paramsInvalid(self):
		return "\nWHOOPS! One or more of your parameters is invalid. \nMake sure you're only passing in acceptable parameters with appropriate formatting.\n"
	def inputInitialParams(self):
		s = ("\nAdd a parameter by entering the parameter label and value pair separated by" 
		"\na colon. For example, if your parameter is \"limit\" and the value"
		"\nyou'd like to set for limit is \"5\" you would write \"limit:5\"."
		"\nFor multiple values, write the values in a list, such as: \"10,-500,60\"."
		"\n \nEnter \"n\" if you'd like to move on without adding a parameter.\n \n")
		return s
	def inputMoreParams(self):
		return "\nAdd another parameter using the same method. \nOtherwise, enter \"n\" if you'd like to continue.\n\n"
	def exit(self):
		return "\nWould you like to exit? (Type \"y\" or \"n\".)\n\n"
	def fileSave(self):
		return "\nYour data is almost ready for viewing; we just need to create the CSV file. \nPlease enter a file name: \n\n"
	def IOError(self):
		return "\nWHOOPS! I/O error. Something failed. Couldn't write data to a CSV file.\n"
	def CSVFinished(self):
		return "\n\nCongratulations! Your CSV file has been saved to your directory.\n"
	def JSONEmpty(self):
		return "\nWHOOPS! No relevant data found for the parameters you've selected. Just emptiness.\n"


### Asks the user if they'd like to exit. If user 
### enters something other than "y" or "n", the prompt
### will repeat itself. 
def exit():
	a = input(bot.exit()).strip().lower()
	if (a == "y"):
		sys.exit()
	elif (a == "n"):
		doConversion()
	else: 
		exit()


### Allows the user to add as many parameters into their 
### API request as they please.  
def getParams():
	params = {}
	p = None
	p = input(bot.inputInitialParams()).strip()
	while (p != 'n'):
		k,v = p.split(":")
		params.update({k:v})
		print("\nParameter \"" + p + "\" added.") 
		print("\nYour parameters are: \n")
		print(params)
		p = input(bot.inputMoreParams()).strip()
	return params


### A hard-coded, hacky function that detects dictionaries 
### that have only two keys: "count" and "results".
### If this is the case, the function returns an array which 
### is the value associated with "results". 
### Also checks if JSON has no relevant data (is empty). 
### Returns a boolean to indicate full/empty. 
def stripJSON(j):
	val = j
	is_empty = False
	keys = list(j.keys())
	if (len(keys) == 2):
		if (keys[1] == 'results'):
			val = j['results']
	if (len(val) == 0): is_empty = True
	return val, is_empty


### Writes the CSV file. 
### Inspired by: https://www.tutorialspoint.com/How-to-save-a-Python-Dictionary-to-CSV-file
def convertToCSV(r_json, f_name):
	csv_columns = list(r_json[0].keys())
	try: 
		with open(f_name, 'w') as f: 
			w = csv.DictWriter(f, fieldnames=csv_columns)
			w.writeheader()
			for data in r_json:
				w.writerow(data)
		print(bot.CSVFinished())
	except:
		print(bot.IOError())
		exit()


### Collects data by calling the API and converting 
### the resulting JSON into CSV format. 
def doConversion():
	url = input(bot.opener())
	#Check to see if URL is valid.
	try: 
		r = req.get(url)
	except: 
		print(bot.URLInvalid())
		exit()
	
	#Allow the user to input paramters.
	params_dict = getParams()

	# Fetch the JSON data and convert to CSV.  
	try: 
		r_json = req.get(url, params=params_dict).json()
	except: 
		if (params_dict == {}): print(bot.somethingFailed())
		else: print(bot.paramsInvalid())
		exit()

	# Check for a hard-coded case and for emptiness. 
	r_json, is_empty = stripJSON(r_json)
	
	# If JSON is not empty, convert to CSV. 
	if not (is_empty):	 
		f_name = input(bot.fileSave()) + '.csv'
		convertToCSV(r_json, f_name)
	else:
		print(bot.JSONEmpty())
		exit()
		

### Initializing the program. 
bot = Chatbot()
doConversion()
