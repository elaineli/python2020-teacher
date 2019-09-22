# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
# tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

# Transform the original problem into a simpler one dimensional problem

# Convert the 6:52 into seconds relative to 00:00:00
leaveAtInSeconds = 6 * 3600 + 52 * 60

# Time used for my running
minsRun = 8 + 7 * 3 + 8
secsRun = 15 + 12 * 3 + 15

# Time I get home in seconds relative to 00:00:00
getHomeInSeconds = leaveAtInSeconds + minsRun * 60 + secsRun

# Transform homeAtInSeconds into hour:minute:second format
h = getHomeInSeconds // 3600
m = (getHomeInSeconds % 3600) // 60
s = (getHomeInSeconds % 3600) % 60

print('i get home at', h, ':', m, ':', s, 'AM')