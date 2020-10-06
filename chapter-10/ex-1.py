# Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

fname = input('file: ')
if len(fname) == 0:
    fname = 'mbox-short.txt'

fhand = open(fname)
maildict = dict()
for line in fhand:
    if line.startswith("From "):
        words = line.split()
        mail = words[1]
        maildict[mail] = maildict.get(mail, 0) + 1

newlist = list()

for key, value in maildict.items():
    newlist.append((value, key))

newlist.sort(reverse=True)

print(newlist)
