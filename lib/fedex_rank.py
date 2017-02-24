import datetime
import re
import urllib2
from bs4 import BeautifulSoup
from golfer import Golfer

# using yahoo services to get data
uri = "https://sports.yahoo.com/golf/pga/stats/bycategory?cat=CUP_POINTS&season=2017"
date = datetime.date.today()


def fedexStandings():
	print "FedEx Cup standings as of %s\n" % date
	response = urllib2.urlopen(uri)
	source = BeautifulSoup(response.read(), "html.parser")
	response.close()
	
	if not source:
		print "Error reading source."
		quit()

	data = source.find_all("td", {"class" : "first rank"})
	data += source.find_all("td", {"class" : ["player", "stat"]})

	golfers = process(data) # list containing Golfer objects

	for g in golfers:
		g.string()


def process(data):
	golfers = [] # list for Golfer objects
	c = 0 # counter to keep track of what line is being processed
	rank = "N/A" # current player fedex cup rank
	name = "N/A" # current player name
	points = "N/A" # current player fedex cup points

	for line in data:
		print line
		print ""
		'''
		if c == 0: # strip fedex cup ranking
			match = match_digits(line)
			if not match:
				continue
			rank = match
			c += 1
		elif c == 1: # strip name
			match = match_name(line)
			if not match:
				continue
			name = match
			c += 1
		elif c == 2: # last week's ranking
			# previous ranking, unnecessary stat
			c += 1
		elif c == 3: # strip fedex cup points
			match = match_digits(line)
			if not match:
				continue
			points = match
			# all data for current golfer is collected
			#temp = Golfer(rank, name, points)
			#golfers.append(temp)
			print name
			print rank
			print points
			c = 0
		else:
			print "Error processing source."
			quit()
		'''

	return golfers

def match_digits(line):
	match = re.findall(r'[0-9,]+', str(line))
	if not match:
		return None
	return str(match[0])

def match_name(line):
	match = re.findall(r'[A-Z]{1}\w+\s{1}[A-Z]{1}\w+', str(line))
	if not match:
		return None
	return str(match[0])
