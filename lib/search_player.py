import datetime
import re
import urllib2
from bs4 import BeautifulSoup
from golfer import Golfer

#site to crawl to get data
uri = "https://sports.yahoo.com/golf/pga/players?q=%s"
date = datetime.date.today()


def	searchPlayer():

	term = str(raw_input("Enter player to search > "))

	if not term:
		print "Input error."
		quit()

	response = urllib2.urlopen(uri % term)
	source = BeautifulSoup(response.read(), "html.parser")
	response.close()
	
	if not source:
		print "Error reading source."
		quit()

	data = source.find_all("div", {"id" : "playerResult"})
	
	golfers = []


	for line in data:
		name = match_name(line)
		if not name:
			continue
		golfers.append(name)

	if not golfers:
		print "No golfers found"
	elif len(golfers) == 1:
		jump()
	elif len(golfers) > 1:
		display()
		searchPlayer()

def display(golfers):

	print "Ambigious search. Results..."
	for g in golfers:
		print g
	print "Try search again."

def match_name(line):
	match = re.findall(r'[A-Z]{1}\w+\s{1}[A-Z]{1}\w+', str(line))
	if not match:
		return None
	return str(match[0])

def match_url(line):
	return None