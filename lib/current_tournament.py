import datetime
import re
import urllib2
from bs4 import BeautifulSoup
from golfer import Golfer

#site to crawl to get data
uri = "https://sports.yahoo.com/golf/pga/stats/bycategory?cat=CUP_POINTS&season=2017"
date = datetime.date.today()


def currentTournament():
	print "tourney"