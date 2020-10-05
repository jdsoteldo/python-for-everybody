count = 0

fname = input("enter file: ")
if fname == 'na na boo boo':
    print("NA NA BOO BOO - You've been punked")
    quit()
elif len(fname) == 0:
    fname = 'mbox.txt'

fhand = open(fname)
for line in fhand:
    if line.startswith('Subject'):
        count += 1

print('there were', count, 'subjects in', fname)
