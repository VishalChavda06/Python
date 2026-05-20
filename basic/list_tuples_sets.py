# 📘 CONCEPT — Why Do We Need These?
# Right now you store ONE value in ONE variable:
# pythonplayer1 = "Vishal"
# player2 = "Rohit"
# player3 = "Dhoni"
# player4 = "Kohli"
# player5 = "Bumrah"
# But what if you have 100 players? 😱
# 100 variables?! That is madness!
# Solution → Store ALL values in ONE variable using Data Structures!
# (Data Structure = ek container jema multiple values ek sathe rakho —
# a container that holds multiple values together!)
# python# All 5 players in ONE variable!
# players = ["Vishal", "Rohit", "Dhoni", "Kohli", "Bumrah"]
# Clean, smart, professional! 😎


# 📘 PART 1 — List
# A List (list = yadi — an ordered collection of items) is:

# ✅ Ordered — items stay in the order you put them
# ✅ Changeable — you can add, remove, update items
# ✅ Allows duplicates — same value can appear twice
# ✅ Written with square brackets [ ]


# 🏏 Real-life analogy:
# Think of a cricket team batting order —
# Position 1, 2, 3... stays in order!
# You can change who bats where!
# That ordered, changeable list = a Python List!


# simple example of a list

# Creating a list
players = ["Vishal", "Rohit", "Dhoni", "Kohli", "Bumrah"]

# Accessing items — INDEX starts from 0!
# Index:              0        1       2        3         4
print(players[0])    # Vishal  — pehlo item (first item)
print(players[1])    # Rohit
print(players[-1])   # Bumrah  — chhello item (last item) — negative index!

# Length of list
print(len(players))  # 5 — ketla items chhe (how many items)
print("===================================")
# 💻 CODE EXAMPLE 2 — Modifying a List
players = ["Vishal", "Rohit", "Dhoni"]

# ADD item at end
players.append("Kohli")
print(players)    # ['Vishal', 'Rohit', 'Dhoni', 'Kohli']

# ADD item at specific position
players.insert(1, "Bumrah")
print(players)    # ['Vishal', 'Bumrah', 'Rohit', 'Dhoni', 'Kohli']

# UPDATE item
players[0] = "Hardik"
print(players)    # ['Hardik', 'Bumrah', 'Rohit', 'Dhoni', 'Kohli']

# REMOVE item
players.remove("Bumrah")
print(players)    # ['Hardik', 'Rohit', 'Dhoni', 'Kohli']

# REMOVE last item
players.pop()
print(players)    # ['Hardik', 'Rohit', 'Dhoni']
print("===================================")

# 💻 CODE EXAMPLE 3 — Loop Through a List

players = ["Vishal", "Rohit", "Dhoni", "Kohli", "Bumrah"]

# print every player in the list
for i in range(len(players)):
    print(f"position {i+1}: {players[i]}")
  
# simpler way - direct loop
for player in players:
    print(f"Player: {player} is playing well!")


# 📘 PART 2 — Tuple
# A Tuple (tuple = pakku yadi — a FIXED ordered collection) is:

# ✅ Ordered — items stay in order
# ❌ Unchangeable — cannot add, remove or update!
# ✅ Written with round brackets ( )


# 🏟️ Real-life analogy:
# Think of cricket ground dimensions —
# The pitch length is ALWAYS 22 yards!
# You CANNOT change it!
# Fixed, permanent data = Tuple

# Tuple — fixed data that should NEVER change!
ipl_teams  = ("MI", "CSK", "RCB", "KKR", "SRH")
pitch_size = (22, 10)          # length, width in yards

print(ipl_teams[0])            # MI
print(ipl_teams[-1])           # SRH
print(len(ipl_teams))          # 5

# Try to change — ERROR! ❌
# ipl_teams[0] = "DC"            # TypeError! Tuples cannot change!
print("===================================")

# 📘 PART 3 — Dictionary
# A Dictionary (dictionary = shabdkosh — key-value pairs, like a real dictionary!) is:

# ✅ Stores data as key: value pairs
# ✅ Access value using its KEY — not index number!
# ✅ Changeable — add, remove, update
# ✅ Written with curly brackets { } and colons :


# 📖 Real-life analogy:
# Think of a real dictionary —
# You look up a WORD (key) → get its MEANING (value)
# "Python" → "A programming language"
# That word:meaning pair = Dictionary in Python!

players ={
    "name" :"vishal",
    "runs" : 60,
    "city": "Ahmedabad",
    "runs" : 70,  
    "active": True
}

# access using key name
print(players["name"])   # vishal
print(players["runs"])   # 70 — last value for duplicate key is used!
print(players["city"])   # Ahmedabad

# update a value
players["runs"] = 80
print(players["runs"])   # 80

# Add a new key-value pair
players["team"] = "MI"
print(players)

# Remove a key-value pair
del players["active"]
print(players)

# check all keys and values
print(players.keys())    # dict_keys(['name', 'runs', 'city', 'team'])
print(players.values())  # dict_values(['vishal', 80, 'Ahmedabad


# 📘 PART 4 — Set
# A Set (set = alag alag items no samuho — a group of UNIQUE items) is:

# ✅ Stores UNIQUE values only — no duplicates!
# ❌ Not ordered — no index!
# ✅ Written with curly brackets { }


# 🏏 Real-life analogy:
# Think of a list of countries that have won the Cricket World Cup —
# Each country appears ONCE — no matter how many times they won!
# That unique collection = a Set!

# Set — duplicates automatically removed!
countries = {"India", "Australia", "England", "India", "Australia"}
print(countries)    # {'India', 'Australia', 'England'} — duplicates gone!

# Add item
countries.add("West Indies")
print(countries)

# Remove item
countries.remove("England")
print(countries)

# Check if item exists
print("India" in countries)    # True
print("Pakistan" in countries) # False