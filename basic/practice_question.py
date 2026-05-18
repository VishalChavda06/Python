# veriable
# swap the number

a = 10
b = 5

print("Before swap: a =", a, "b =", b)
print("After swap: a =", b, "b =", a)

# User input and name print
name = input("Enter your name:")
print("hello", name)


# Sum the number with user input

num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
sum = num1 + num2
print("The sum is:", sum)

# operations 
numbers1 = 12
numbers2 = 5

addition = numbers1 + numbers2
subtraction = numbers1 - numbers2
multiplication = numbers1 * numbers2
division = numbers1 / numbers2 if numbers2 != 0 else "undefined"

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)


# find remainder 
remainder_number = 10 % 3
print("Remainder:", remainder_number)

# conditional statement
age = int(input("Enter your age:"))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
    
#  even and odd number
number = int(input("Eneter the number :"))
if number % 2 == 0:
    print("The number is even.")
else:    print("The number is odd.")