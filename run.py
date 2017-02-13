import datetime
import functions

date = datetime.date.today()
time = datetime.datetime.time(datetime.datetime.now())

print "CURRENT DATE: %s" % date
print "CURRENT TIME: %s\n" % time

print "MENU:"
print "1. Display PGA Tour stats leaders"
print "2. Retrieve this week's tournament leaderboard"
print "3. Retrieve current FedEx Cup standings"
print "4. Search stats for player"
print "5. Exit\n"

#option = int(raw_input("Enter option > "))
option = 3
if (option < 1) or (option > 5):
	print "Invalid menu option....quitting."
	quit()

if (option == 1):
	functions.seasonStatLeaders()
elif (option == 2):
	functions.currentTournament()
elif (option == 3):
	functions.fedexStandings()
elif (option == 4):
	functions.searchPlayer()
else:
	print "Quitting..."
	quit()
	
