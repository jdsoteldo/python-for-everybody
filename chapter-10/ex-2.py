# This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

fname = input('file: ')
if len(fname) == 0:
    fname = 'mbox-short.txt'

fhand = open(fname)

hourdict = dict()

for line in fhand:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        hour = words[5]
        hoursplit = hour.split(':')
        hourcount = hoursplit[0]
        hourdict[hourcount] = hourdict.get(hourcount, 0) + 1

newhour = list()

for key, value in hourdict.items():
    newhour.append((value, key))

newhour.sort(reverse = True)

for printhour in newhour:
    print(printhour[0], printhour[1])
