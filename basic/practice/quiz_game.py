print("Welcome to the Quiz Game! 🎉")

score = 0

print("/nQuestion 1:")
print("what is 2+2?")
print("a) 3")
print("b) 4")
print("c) 5")
answer = input("Enter your answer : ")

if answer == "b":
    print("Correct! ✅")
    score += 1
else:    print("Wrong! ❌")

print("/nQuestion 2:")
print("What is the capital of France?")
print("a) Berlin")
print("b) Madrid")
print("c) Paris")
answer = input("Enter your answer : ") 
if answer == "c":
    print("Correct! ✅")
    score += 1
else:    print("Wrong! ❌")

print("/nQuestion 3:")
print("Which planet is known as the Red Planet?")
print("a) Earth")
print("b) Mars")   
print("c) Jupiter")
answer = input("Enter your answer : ")
if answer == "b":
    print("Correct! ✅")
    score += 1
else:    print("Wrong! ❌")

print("game over! 🏁")
print(f"/nYour final score is: {score}/3")