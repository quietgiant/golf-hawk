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
	
	player_source = soup.find_all("td", class_="player")

	for line in player_source:
		players = re.search('>(.*?)</a>', str(line))
		if players is None:
			print "No players found."
			break
		print players.group(0)
	
	#for p in players:

	print 'Closing connection...'
	source.close()

def	searchPlayer():
	print "player"
