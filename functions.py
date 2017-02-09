
import urllib2


def seasonStatLeaders():
	print "season"

def currentTournament():
	print "tourney"

def fedexStandings():
	print "fx"

def	searchPlayer():
	print "player"

#####
import urllib, urllib2
import zipfile
import re

uri = 'http://www.pythonchallenge.com/pc/def/channel.%s'
ext = 'html'

res = urllib2.urlopen(uri % ext)
html = res.read()
print html

print 'attempting to download...\n'

target = 'channel.zip'
ext = 'zip'
folder = urllib.urlretrieve(uri % ext, target)

print 'download complete. \nstarting extraction.\n'

directory = zipfile.ZipFile('channel.zip')
comments = []
num = '90052'

while True:
	file = '%s.txt' % num 
	data = directory.read(file)
	comment = directory.getinfo(file).comment
	print 'DATA:\n%s\n----------' % data
	print 'COMMENT:\n%s\n----------' % comment
	comments.append(comment)
	new = re.search(r'(\d+)', data)
	if new is None:
		break
	num = new.group(0)
	print '%s\n' % num

print ''.join(comments)

print 'closing connection...'
res.close()
print 'done.'
