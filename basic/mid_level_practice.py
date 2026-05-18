# Take user's birth year and calculate current age.

birth_year = int(input("Enter your birth year:"))
current_year = 2026

age = current_year - birth_year
print(f"Your current age is: {age}")

# Create a simple calculator.

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2   
division = num1 / num2 if num2 != 0 else "undefined"
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)


# Take user's salary and calculate yearly salary.

monthly_salary = float(input("Enter your monthly salary:"))
yearly_salary = monthly_salary * 12
print(f"Your yearly salary is: {yearly_salary}")


#  Rectangle Area

length = float(input("Enter the length of the rectangle:"))
width = float(input("Enter the width of the rectangle:"))   
print(f"The area of the rectangle is: {length * width}")