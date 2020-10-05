number = 0
total = 0.0

while True:
    value = input("Enter a number (type done to quit): ")
    if value == 'done':
        break

    try:
        floatvalue = float(value)
    except:
        print("Invalid input")
        continue

    number = number + 1
    total = total + floatvalue
    average = total/number

print('Sum:', total, 'Count:', number, 'Average:', average)
