# Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

def chop(l):
    # cuts from first to last
    l = l[1:-1]

def middle(l):
    return l[1:-1]

letters = ['a', 'b', 'c', 'd', 'e']
print(chop(letters))
print(middle(letters))
