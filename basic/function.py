# 📘 CONCEPT — What is a Function?A Function (function = ek kaam kartu dabbu — a box that does one specific job) is a reusable block of code that you write ONCE and use as many times as you want!
# 🍵 Real-life analogy — Chai Recipe!
# Roz savar tame chai banao chho — same steps every time:
# (Every morning you make chai — same steps every time:)

# Boil water
# Add tea leaves
# Add milk
# Add sugar
# Serve! ☕

# Tame drek vaar 5 steps yaad nathi karta —
# tame bas kaho "Chai banao!" — ane kaam thay jaay!
# (You don't remember 5 steps every time —
# you just say "Make chai!" — and the job gets done!)
# That "Chai banao!" command = calling a Function in Python!



# 📘 Why Do We Need Functions?
# Without functions — bad code 😫:
# python# Calculating area — again and again manually!
# area1 = 5 * 3
# print(f"Area: {area1}")

# area2 = 8 * 4
# print(f"Area: {area2}")

# area3 = 10 * 6
# print(f"Area: {area3}")

# With functions — clean and smart code 😎:
# python# Write ONCE — use forever!
# def calculate_area(length, width):
#     area = length * width
#     print(f"Area: {area}")

# calculate_area(5, 3)    # use 1
# calculate_area(8, 4)    # use 2
# calculate_area(10, 6)   # use 3
# Same result — but SO much cleaner! 🔥


# def function_name(parameters):     # 1. DEFINE  — function banavo
#     # code here                    # 2. BODY    — kaam karo
#     return value                   # 3. RETURN  — result paachho apo
                                   
# function_name(arguments)           # 4. CALL    — function vapro



# simple function example:

def greet():
    print("hello, welcome to python functions!")
    print("have nice day! 😊")

greet() # one time calling functin
greet() # calling function second time, we can call as many times as we want!
greet() # calling function third time, we can call as many times as we want!

print("--------------------------------------------------")
# 💻 CODE EXAMPLE 2 — Function with Parameters

def greet_player(name):
    print(f"hello {name}, welcome to the game! 🎮")
    print("have fun playing! 😊")

greet_player("vishal") # calling function with argument "vishal"
greet_player("sneha") # calling function with argument "sneha"
greet_player("rahul") # calling function with argument "rahul"

print("--------------------------------------------------")
# CODE EXAMPLE 3 — Function with Return

def add_numbers(num1, num2):
    result = num1 + num2
    return result

total = add_numbers(5,7)
print(f"The total number is: {total}")

print("--------------------------------------------------")
# CODE EXAMPLE 4 — Function with Multiple Parameters

# Cricket strike rate calculator function
def strike_rate(runs, balls):
    rate = round((runs / balls) * 100 , 2)
    return rate

def batting_grade(runs , balls):
    rate = strike_rate(runs , balls)

    if rate >= 150:
        grade  = "🔥 excellent"
    elif rate >= 100:
        grade = "👍 good"
    else:
        grade = "💪 keep practicing"

    return f"Strike Rate: {rate} — Grade: {grade}"

print(batting_grade(60, 30)) # calling function with runs and balls
print(batting_grade(45, 50)) # calling function with runs and balls


print("--------------------------------------------------")
# CODE EXAMPLE 5 — Function with Default Parameter

def introduce(name , city="surat"):
    print(f"Hello, my name is {name} and I am from {city}.")

introduce("vishal") # calling function with only name, city will use default value "surat"
introduce("sneha", "ahmedabad") # calling function with name and city
introduce("rahul", "vadodara") # calling function with name and city


print("--------------------------------------------------")
# 💻 CODE EXAMPLE 6 — Function inside a Loop! (Super Powerful! 🔥)

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
for i in range(1,11):
    if is_even(i):
        print(f"{i} is even. ✅")
    else:
        print(f"{i} is odd. ❌")