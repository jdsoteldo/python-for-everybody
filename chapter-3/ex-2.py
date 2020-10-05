# Rewrite your pay program using try and except so that
# your program handles non-numeric input gracefully by
# printing a message and exiting the program.
# The following shows two executions of the program:

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    h = float(hours)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

if h <= 40:
    pay = h * r
else:
    overtime = (h - 40) * (r * 0.5)
    pay = h * r + overtime

print("Pay:", pay)
