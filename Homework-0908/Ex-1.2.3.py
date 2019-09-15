# If you run a 10 kilometer race in 42 minutes and 42 seconds

# Create all variables needed
miles = 10/1.61
seconds = 42*60 + 42
minutes = 42 + 42/60
hours = 42/60 + 42/3600

# what is the average pace in minutes?
paceInMinutes = minutes/miles
print('pace in minutes = ', paceInMinutes)

# what is the average pace in seconds?
paceInSeconds = seconds/miles
print('pace in seconds = ', paceInSeconds)

# what is the average speed?
speed = miles/hours
print('speed = ', speed, 'miles per hour')

