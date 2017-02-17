import datetime
import functions

date = datetime.date.today()
time = datetime.datetime.time(datetime.datetime.now())

print "CURRENT DATE: %s" % date
print "CURRENT TIME: %s\n" % time

print "MENU:"
print "1. Retrieve this week's tournament leaderboard"
print "2. Retrieve current FedEx Cup standings"
print "3. Search stats for a player"
print "4. Exit\n"

#option = int(raw_input("Enter option > "))
option = 2
if (option < 1) or (option > 4):
	print "Invalid menu option....quitting."
	quit()

if (option == 1):
	functions.currentTournament()
elif (option == 2):
	functions.fedexStandings()
elif (option == 3):
	functions.searchPlayer()
else:
	print "Quitting..."
	quit()

