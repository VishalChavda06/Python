# 📘 CONCEPT — What is a Loop?
# A Loop (loop = faaro — going around again and again) tells Python —
# "Aa kaam baar baar kar — jyaa sudhi huu kahu tyaa sudhi!"
# (Do this work again and again — until I say stop!)

# 🏏 Real-life analogy:
# Think of cricket practice. Your coach says —
# "Vishal — 50 vaaar ball fek!" (Vishal — throw the ball 50 times!)
# You don't throw once and stop. You keep throwing — again and again — 50 times total.
# That repeating action = a LOOP in Python!


# 📘 TYPE 1 — The for Loop
# A for loop is used when you know exactly how many times you want to repeat!
# pythonfor variable in range(start, stop):
#     # aa code repeat thase (this code will repeat)

# ⚠️ Important about range():

# range(1, 11) → gives numbers 1, 2, 3... 10 (11 nai aave — stop value aavti nathi!)
# range(5) → gives 0, 1, 2, 3, 4 (always starts from 0 if no start given)
# range(1, 10, 2) → gives 1, 3, 5, 7, 9 (step of 2 — ek chhodi ne ek!)

# simple for loop example:
for i in range(1,6):
    print(f"number : {i}")
    
# Loop with Maths!
for over in range(1,7):
    runs = over * 6
    print(f"Over {over}: Runs scored = {runs}")
    
#  Loop with if inside! (Powerful combo! 🔥)

for i in range(1,11):
    if i % 2 == 0:
        print(f"{i} is even. ✅")
    else:
        print(f"{i} is odd. ❌")
        
# 📘 TYPE 2 — The while Loop
# A while loop is used when you DON'T know exactly how many times —
# you just want to keep going while a condition is True!
# pythonwhile condition:          # jyaa sudhi condition True chhe, chaltu raho
#     # repeat this code   # aa code repeat thase

# 🚦 Real-life analogy:
# Think of a traffic signal.
# While the light is red → you stay stopped.
# The moment it turns green → you go!
# You don't know exactly HOW LONG you will wait — you just wait while it's red!

# Basic while Loop

count =1
while count <=5:
  print(f"count : {count}")
  count +=1

# while with User Input (Real App feel! 🎮)

password = "vishal123"
attempt = ''

while attempt != password:
  attempt = input("Enter the password:")
  if attempt == password:
    print("Login successful! 🎉")
  else:
    print("Incorrect password. Try again! ❌")
    
#  Loop with Running Total

total = 0
for i in range(1,6):
  total = total + i
  print(f"After adding {i}, total is: {total}")
print(f"Final total: {total}")




# for loop:Build an "IPL Score Card!"

played_overs = int(input("Enter the number of overs played: "))
per_over_runs = int(input("Enter the runs scored per over: "))
total_runs = 0

for i in range(1, played_overs + 1):
		total_runs += per_over_runs
		print(f"After over {i}: Total runs = {total_runs}")
print(f"Final Score after {played_overs} overs: {total_runs} runs")

# while loop: Build a "Number Guessing Game!"
secret_number = 7
while True:
    guess_number = int(input("Guess a number between 1 and 10: "))
    if guess_number == secret_number:
        print("Congratulations! You guessed the correct number! 🎉")
        break
    else:
        print("Sorry, that's not the correct number. Try again! 😞")

vishal = "Amazing Student"
lesson_tomorrow = "Functions"

print(f"Good night {vishal}!")
print(f"Tomorrow → Lesson 7: {lesson_tomorrow}!")
print("Rest well. Code better tomorrow! 💪")