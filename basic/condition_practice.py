# if condition:          # shart tapo (check the condition)
#     # do this         # jો shart sachi hoy to (if condition is True)

# elif another_condition:   # biji shart tapo (check another condition)
#     # do this            # jો biji shart sachi hoy to

# else:                  # baaki badha case maate (for all remaining cases)
#     # do this          # jyare koi shart sachi na hoy to (when no condition is True)


    # 🌧️ Real-life analogy:
    # Every morning you think:

    # If it is raining → take umbrella ☂️
    # Else if it is cloudy → maybe take umbrella 🤔
    # Else → go freely, no umbrella! ☀️

    # Python does EXACTLY this — with if, elif, and else!

# simple example:
runs = int(input("Enter your runs :"))
target = int(input("enter your target :"))

if runs >= target:
    print("Target achieved! 🎉")
else:
    print("Target not achieved. Keep trying! 💪")
    
    
# if-elif-else example:
runs = int(input("Enter your runs: "))
target = int(input("Enter the target: "))

if runs > target:                               # runs target thi vadhu chhe?
    print("🏆 We WON the match!")

elif runs == target:                            # runs target barabar chhe?
    print("🤝 It's a TIE!")

else:                                           # baaki badhu — matlab runs < target
    difference = target - runs
    print(f"😞 We lost by {difference} runs.")
    

# Multiple elif example:

marks = int(input("Enter your marks :"))
if marks >= 90:
    print("Grade : A+")
elif marks >= 80:
    print("Grade : A")
elif marks >= 70:
    print("Grade : B")
elif marks >= 60:
    print("Grade : C")
else:
    print("Grade : F and you need to work hard")
    

# Conditions with and / or
age = int(input("Enter your age: "))
has_id = input("do you have an ID? (yes/no): ")

if age >= 18 and has_id == "yes":
    print("✅ You can enter the club!")
elif age >= 18 and has_id == "no":
    print("⚠️ You are old enough but need an ID to enter.")
else:
    print("⛔ You are not old enough to enter the club.")


# taks : IPL Batting Performance Checker!

name = input("Enter the player's name: ")
runs = int(input("Enter the runs scored: "))
balls_played = int(input("Enter the balls played: "))

strike_rate = round((runs / balls_played) * 100 , 2)
if strike_rate >= 150:
    print(f"{name} 🔥 World Class innings and strike rate is {strike_rate}!")
elif strike_rate >= 120:
    print(f"{name} 💪 Good innings and strike rate is {strike_rate}!")
elif strike_rate >= 100:
    print(f"{name} 👍 Decent innings and strike rate is {strike_rate}.")
else:
    print(f"{name} 😞 Needs improvement and strike rate is {strike_rate}.")