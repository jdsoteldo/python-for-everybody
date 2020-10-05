# Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.
min = 0
max = 0
bigNum = None
smallNum = None

while True:
    value = input("Enter a number (type done to quit): ")
    if value == 'done':
        break

    try:
        floatvalue = float(value)
    except:
        print('Invalid input')
        continue

    if bigNum is None or floatvalue > bigNum:
        bigNum = floatvalue
    elif smallNum is None or floatvalue < smallNum:
        smallNum = floatvalue

print("max:", int(bigNum))
print("min:", int(smallNum))
