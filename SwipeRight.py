# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
# defining amount of time between actions
SleepInteger = 1.5
# x is our starting integer
x = 0
# num is our ending integer
num = 250
# printing something to make it look cool
print 'Swiping motion started - %s sec between swipes, going for %s Swipes\n' % (SleepInteger, num,),
print '. . .waiting for connection'
# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection(4)
# while loop to send instructions to phone
while x < num :
	# device.drag sets coordinates for start -> stop swiping motion
	device.drag((330,600),(660,500),0.02,50)
	# some sleep to let the phone keep pulling up data
	MonkeyRunner.sleep(SleepInteger)
	# this print clears the screen
	print "\033c"
	# add value to starting integer to keep count
	x = x+1
	# Print informational warning
	print '## This is now a bananas terminal. terminate with StopSwipe from another pty ##'
	print 'Swiping motion started - %s sec between swipes, going for %s Swipes\n' % (SleepInteger, num,),
	# print our counter
	print 'Swipes = %s\n' % (x,),
	# Check if while loop is done
	# dont know if necessary
	if x == num:
		print 'Swiping done, reached %s actions' % (x,),
		break	# break stopes the loop if x == num
