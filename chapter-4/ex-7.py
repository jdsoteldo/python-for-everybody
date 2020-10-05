# Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.
try:
    score = float(input("Add score: "))
except:
    print("Bad score!")
    quit()

def computepay(score):
    if score > 1 or score < 0:
        print("Bad score")
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")

computepay(score)
