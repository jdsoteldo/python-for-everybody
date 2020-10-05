# Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters “done”. Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.
list = []

while True:
    inp = input('enter a number (type done to quit): ')
    if inp == 'done':
        break

    try:
        finp = float(inp)
        list.append(finp)
    except:
        print('invalid input')
        continue

print('max:', max(list), 'min:', min(list))
