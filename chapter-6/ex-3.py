# Encapsulate this code in a function named count, and gen- eralize it so that it accepts the string and the letter as arguments.
text = input('Text: ')
letter = input('Letter: ')

def count(text, letter):
    count = 0
    for i in text:
        if i == letter:
            count += 1
    return count

times = count(text, letter)
print('the letter appears', times, 'time')
