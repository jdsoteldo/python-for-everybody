# Write a program to prompt for a file name, and then read through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.
count = 0
total = 0

fname = input("enter file: ")
# do this so u dont have to type the file name each time
if len(fname) == 0:
    fname = 'mbox-short.txt'

fhand = open(fname)

for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    numbers = float(line[21 : -1])
    total = numbers + total

average = total / count
print("Average spame confidence:", average)
