import datetime
import re
import urllib2
from bs4 import BeautifulSoup
from golfer import Golfer

#site to search for input
uri = "https://sports.yahoo.com/golf/pga/players?q=%s"
date = datetime.date.today()


def	searchPlayer():
	term = str(raw_input("Enter player to search > "))

	if not term:
		print "Input error."
		searchPlayer()

	response = urllib2.urlopen(uri % term)
	source = BeautifulSoup(response.read(), "html.parser")
	response.close()
	
	if not source:
		print "Error reading source."
		quit()

	data = source.find_all("td", {"class" : "last"})

	golfers = process(data)

	if not golfers:
		print "No golfers found"
		searchPlayer()
	elif len(golfers) == 1:
		jump(match_url(data[0]))
	elif len(golfers) > 1:
		print_golfers(golfers)
		searchPlayer()

def process(data):
	golfers = []

	for line in data:
		name = match_name(line)
		if not name:
			continue
		golfers.append(name)

	return golfers

def jump(url):
	response = urllib2.urlopen(uri % url)
	source = BeautifulSoup.(response.read(), "html.parser")
	response.close()




def print_golfers(golfers):
	print "Ambigious search. Results...\n"
	for g in golfers:
		print g
	print "\nSpecify golfer and try search again.\n"

def match_name(line):
	match = re.findall(r'[A-Z]{1}\w+\s{1}[A-Z]{1}\w+', str(line))
	if not match:
		return None
	return str(match[0])

def match_url(line):
	match = re.findall(r'/golf/pga/players/\w+\+\w+/\d+', str(line))
	if not match:
		return None
	return str(match[0])