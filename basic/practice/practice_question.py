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



# Create simple login system.

userName = input("enter your username :")
password = input("enter your password :")

if userName == "admin" and password =="vishal123":
    print("Login Successfull! 🎉")
else:
    print("Login Failed! ❌ Please check your username and password.")
    

# Take 3 numbers and print largest number.

num1 = float(input("enter the first number :"))
num2 = float(input("enter the second number :"))
num3 = float(input("enter the third number :"))

if num1 >= num2 and num1 >= num3:
    print("The largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)
    
    
# Build mini calculator using conditions.
number1 =int(input("Enter the first number:"))
number2 =int(input("Enter the second number:"))
operator = input("Enter the operator (+, -, *, /):")

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    result = number1 / number2 if number2 != 0 else "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operator."

print("Result:", result)

# ATM Withdrawal System

account_balance = int(input("Enter your account balance: "))
withdrawal_amount = int(input("Enter the withdrawal amount: "))

if withdrawal_amount <= account_balance:
    print("Withdrawal successful! Please take your cash.")
else:
    print("Insufficient funds! Withdrawal failed.")
    
# Simple Number Guessing Game

guess_number = int(input("Guess a number between 1 and 10: "))
secret_number = 7
if guess_number == secret_number:
    print("Congratulations! You guessed the correct number! 🎉")
else:
    print("Sorry, that's not the correct number. Try again! 😞")
    
# for and while loops

for i in range(10):
    print("sorry we not did it yet")

# Print even numbers from 1 to 20.
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Find sum of numbers from 1 to 10.
total = 0
for i in range(1, 11):
    total += i
print("Sum of numbers from 1 to 10:", total)

# Print multiplication table of 5.
number = 5
while number <= 50:
    print(number)
    number += 5

# print the star pattern
rows = 5
for i in range(1, rows + 1):
    print("* " * i)

# reverse star pattern
rows = 5
for i in range(rows, 0, -1):
    print("* " * i)

# Countdown Program
count = 10
while count > 0:
    print(count)
    count -= 1
print("Liftoff! 🚀")