# List:Create a list of your 5 favourite foods

print("========task -1======== ")
favourite_foods = ["Pizza", "Burger", "Sushi", "Taco", "Ice Cream"]
print(favourite_foods)

favourite_foods.append("Pasta") # Adding "Pasta" to the list
print(favourite_foods)

favourite_foods.remove("Burger") # Removing "Burger" from the list
print(favourite_foods)

print("========task -2======== ")

# Create a dictionary for YOUR cricket profile:

my_profile = {
    "name"    : "Vishal Chavda",
    "age"     : 18,
    "city"    : "Surat",
    "runs"    : 850,
    "team"    : "MI"
}
print(my_profile)

print(my_profile["name"])
print(my_profile["runs"])

my_profile["runs"] = 1000
print(my_profile)


my_profile["wickets"] = 25
print(my_profile)

for key in my_profile:
    print(f"{key} : {my_profile[key]}")

print("========task -3======== ")
# Task 3 — Combine List + Dictionary! 🔥Create a list of dictionaries — one for each player!

team = [
    {"name": "Vishal", "runs": 85,  "balls": 50},
    {"name": "Rohit",  "runs": 120, "balls": 80},
    {"name": "Dhoni",  "runs": 60,  "balls": 30},
]

for player in team:
    name  = player["name"]
    runs  = player["runs"]
    balls = player["balls"]
    print(f"Player: {name} — Runs: {runs} — Balls: {balls}")