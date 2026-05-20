# Basic Function Write a function called
print("========task -1======== ")
def player_name(name):
    print(f"Player name is: {name}")
player_name("vishal") # calling function with argument "vishal"
player_name("sneha") # calling function with argument "sneha"
player_name("rahul") # calling function with argument "rahul"

print("========task -2======== ")
# Task 2 — Function with Return: Write a function called 

def add_numbers(runs , overs):
    run_rate =  runs / overs
    return run_rate
result = add_numbers(10, 5)
print(f"The run rate is: {result}")

# Full Program with Functions: Build a "Cricket Report Generator!" Write 2 functions:
# print("========task -3======== ")

# def player(name , runs):
#     return f"Player: {name} — Runs: {runs}"

# def player_report(name, runs, balls):
#     rate = round((runs / balls) * 100 , 2)

#     if rate >= 100:
#         print(f"🏆 Century! Legend!")
#     elif rate >= 50:
#         print(f"⭐ Half Century! Well played!")
#     elif rate >= 30:
#         print(f"👍 Good knock!")
#     else:
#         print(f"💪 Keep practicing!")

#     return f"Player: {name} — Runs: {runs} — Strike Rate: {rate}"

# print(player_report("vishal", 60, 30)) # calling function with name, runs and balls
# print(player_report("sneha", 45, 50)) # calling function with name
# print(player_report("rahul", 20, 40)) # calling function with name

# What you wrote — everything inside one function
def player_report(name, runs, balls):
    rate = round((runs / balls) * 100, 2)
    if rate >= 100:          # grade logic here
        print("...")
    return f"Player: {name}..."

# What task asked — TWO separate functions!
def get_grade(runs):              # Function 1 — only grade
    if runs >= 100:
        return "🏆 Century! Legend!"
    elif runs >= 50:
        return "⭐ Half Century! Well played!"
    elif runs >= 30:
        return "👍 Good knock!"
    else:
        return "😐 Keep practicing!"

def print_report(name, runs, balls):    # Function 2 — full report
    rate  = round((runs / balls) * 100, 2)
    grade = get_grade(runs)             # calling Function 1 inside Function 2!
    print(f"""
═══════════════════════════
🏏 CRICKET REPORT
═══════════════════════════
Player  : {name}
Runs    : {runs}
Balls   : {balls}
SR      : {rate}
Grade   : {grade}
═══════════════════════════""")

print_report("Vishal", 60, 30)
print_report("Sneha", 45, 50)
print_report("Rahul", 20, 40)
    

    

