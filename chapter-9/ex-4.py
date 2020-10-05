# Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dic- tionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

bigNum = 0
bigSender = None
fname = input('file: ')
if len(fname) == 0:
    fname = 'mbox-short.txt'

fhand = open(fname)
maildict = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        # allocate the email address
        mail = words[1]
        maildict[mail] = maildict.get(mail, 0) + 1


for key, value in maildict.items():
    if value > bigNum:
        bigNum = value
        bigSender = key
print(bigSender, bigNum)
