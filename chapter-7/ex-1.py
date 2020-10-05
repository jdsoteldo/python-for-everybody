fname = input("Open file: ")
if len(fname) == 0:
    fname = 'mbox-short.txt'
fhand = open(fname)

for line in fhand:
    line = line.rstrip()
    line = line.upper()
    print(line)
