

'''

1. Please create a function called: add_two_numbers

which takes two parameters, adds them, and returns the sum

'''

def add_two_numbers(a,b):

    return a + b

print(add_two_numbers(1,1))
print(add_two_numbers(2,2))
print(add_two_numbers(3,3))
print(add_two_numbers('a','b'))


'''

2. Please create a function called: multiplier

it takes one required parameter and one optional parameter called "multiplier"

if you do NOT pass a multiplier in it returns double the initial number

If you pass in a multiplier it returns the first parameter multiplied by the second

'''
def multiplier(a,b):
    return a * b

print(multiplier(2,3))
print(multiplier(2,))


'''

3. Please create a function called: divider

It takes in two numbers (not 0 as the divisor until we reach exception handling please!)

divides the first by the second and returns two values, the first is the result and the second is the remainder if it exists.

'''
def divider(a,b)
    return a / b, a % b
result, remainder = divider(2,2)

print(f"result: {result}")
print(f"remainder: {remainder}")


