# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
h = float(input("Enter Hours: "))
r = float(input("Enter Rate: "))

def computepay(h,r):
    pay = h * r
    if h <= 40:
    	return pay
    else:
        overtime = (h - 40) * (r * 0.5)
        overtimePay = pay + overtime
        return overtimePay

print("Pay", computepay(h, r))
