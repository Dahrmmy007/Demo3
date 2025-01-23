# requesting for name input with a welcoming message.
name = input("whats your name? ")
print("welcome!", name)

#
print("hello \nworld")

# calculating the length of strings "damilola".
name = "damilola"
length = len(name)
print(length)

"""slicing with damini string and as well
printing the outcome all the way to the end."""

damini = "Welcome"
damini[0]
print(damini[0])
print(damini[2:])

# converting "hello world" to uppercase using the x.upper format.
x = "hello world"
x = x.upper()
print(x)

# printing formartting with strings and inserting the in diff position.
"""grabing the string and placing it into those crully braces"""
print('this is ogidan {}'.format("IDAN"))
print('I {2} {1} {0}'.format("want", "to", "pray"))

# rounding up the total floating num into 3 decimal point
ok = 100/99
print('the result is {r}'.format(r = ok))
print('the result is {r:1.3f}'.format(r = ok))
r = ok
print(f'the result is {r:1.3f}')

name = 'amina'
age = 30
print(f'{name} is {age} years old')
