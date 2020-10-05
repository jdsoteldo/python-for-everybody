# Rewrite your pay computation with time-and-a-half for over- time and create a function called computepay which takes two parameters (hours and rate).

try:
    h = float(input("Enter Hours: "))
    r = float(input("Enter Rate: "))
except:
    print("Please enter a number!")
    quit()

def computepay(h,r):
    pay = h * r
    if h <= 40:
    	return pay
    else:
        overtime = (h - 40) * (r * 0.5)
        overtimePay = pay + overtime
        return overtimePay

print("Pay", computepay(h, r))
