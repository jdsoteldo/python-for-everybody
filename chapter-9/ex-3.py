# Write a program to read through a mail log, build a his- togram using a dictionary to count how many messages have come from each email address, and print the dictionary.

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


for key in maildict:
    print(key, maildict[key])
