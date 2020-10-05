# Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

fname = input('file: ')
if len(fname) == 0:
    fname = 'mbox-short.txt'

fhand = open(fname)
maildict = dict()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    # position of the day
    day_position = words[2]
    # keeps count
    maildict[day_position] = maildict.get(day_position, 0) + 1

print(maildict)
