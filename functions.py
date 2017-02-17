import datetime
import re
import urllib2
from bs4 import BeautifulSoup

#site to crawl to get data
uri = "https://sports.yahoo.com/golf/pga/stats/bycategory?cat=CUP_POINTS&season=2017"
date = datetime.date.today()



def seasonStatLeaders():
	print "season leaders"

def currentTournament():
	print "tourney"

def fedexStandings():
	print "FedEx Cup standings as of %s" % date
	source = urllib2.urlopen(uri)
	soup = BeautifulSoup(source.read(), "lxml")

	golfers = []
	points = []
	
	player_source = soup.find_all("td", class_="player")
	points_source = soup.find_all("td", class_="stat")

	for line in player_source:
		match = re.findall(r'[A-Z]{1}\w+\s{1}[A-Z]{1}\w+', str(line))
		if not match:
			continue 
		golfers.append(str(match[0]))

	flag = 0 # to process every other line for stat class

	for line in points_source:
		if flag == 0:
			flag = 1
			continue
		else:
			match = re.findall(r'[0-9,]+', str(line))
			if not match:
				continue
			points.append(str(match[0]))
			flag = 0


	source.close()

def	searchPlayer():
	print "player"
