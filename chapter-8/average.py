numlist = []

while True:
    inp = input('enter a number (type done to quit): ')
    if inp == 'done':
        break

    try:
        finp = float(inp)
        numlist.append(finp)
    except:
        print('Invalid input')
        continue

average = sum(numlist) / len(numlist)
print("Average:", average)
