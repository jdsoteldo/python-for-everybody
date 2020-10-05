# Write a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split function. For each word, check to see if the word is already in a list. If the word is not in the list, add it to the list. When the program completes, sort and print the resulting words in alphabetical order.


fname = input('file: ')
if len(fname) == 0:
    fname = 'romeo.txt'

fhand = open(fname)

list = []

for line in fhand:
    line = line.split()
    for word in line:
        if word in list:
            continue
        list.append(word)

print(sorted(list))
