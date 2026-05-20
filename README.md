# 🐍 Python Learning Journey — Vishal Chavda

![Python](https://img.shields.io/badge/Python-3.9.6-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Stage%201%20Complete!-brightgreen?style=for-the-badge)
![Stage](https://img.shields.io/badge/Current-Stage%202%20OOP-blue?style=for-the-badge)
![Lessons](https://img.shields.io/badge/Lessons%20Done-8%20of%2020-yellow?style=for-the-badge)

> 🎓 **Taught by:** PyGuru — A friendly AI Python Tutor
> 📅 **Started:** May 18, 2026
> 🏆 **Stage 1 Completed:** May 20, 2026
> 💻 **Editor:** VS Code
> 🖥️ **OS:** macOS
> 🐍 **Python Version:** 3.9.6

---

## 📊 Overall Progress

| Stage | Topic | Status | Progress |
|-------|-------|--------|----------|
| 🟢 Stage 1 | Python Basics | ✅ COMPLETE! | 8 / 8 Lessons |
| 🔵 Stage 2 | Object Oriented Programming (OOP) | 🔄 Up Next | 0 / 4 Lessons |
| 🟣 Stage 3 | File Handling & APIs | ⏳ Pending | 0 / 4 Lessons |
| 🔴 Stage 4 | Data Structures & Algorithms | ⏳ Pending | 0 / 4 Lessons |

---

## 📈 Progress Tracker

```
Stage 1 — Basics        ████████████████  8/8  Lessons ✅ COMPLETE!
Stage 2 — OOP           ░░░░░░░░░░░░░░░░  0/4  Lessons ⏳ Up Next
Stage 3 — Files & APIs  ░░░░░░░░░░░░░░░░  0/4  Lessons ⏳ Pending
Stage 4 — DSA           ░░░░░░░░░░░░░░░░  0/4  Lessons ⏳ Pending

Overall: ████░░░░░░░░░░░░░░░░  8/20  Lessons Complete (40%)
```

---

# ✅ STAGE 1 — Python Basics (COMPLETE! 🏆)

---

## Lesson 1 — What is Python & `print()` ✅

> 🐍 Python is a programming language used to talk to the computer — like a language, but for machines!

- 🔹 Python is one of the most popular languages in the world
- 🔹 Used in Web Development, AI, Data Science, Automation & more
- 🔹 Very beginner friendly — reads almost like normal English
- 🔹 `print()` is the first function every Python developer learns
- 🔹 Whatever you write inside `print(" ")` gets displayed on screen
- 🔹 Text inside `" "` is called a **String**

```python
print("Hello, World!")          # Output: Hello, World!
print("I am learning Python!")  # Output: I am learning Python!
```

> 💡 **Pro Tip:** Real developers use `print()` for debugging —
> checking what is happening inside their code at any point!

---

## Lesson 2 — Variables & Data Types ✅

> 📦 A Variable is like a labeled box — you give it a name and store a value inside it!

- 🔹 A variable stores a value that you can use later in your program
- 🔹 You create a variable by writing: `variable_name = value`
- 🔹 Python uses **snake_case** style → `my_name`, `total_runs`, `is_student`
- 🔹 Variable names should be clear and descriptive

#### 🔸 The 4 Main Data Types

| Data Type | Meaning | Example |
|-----------|---------|---------|
| `int` | Whole number | `18`, `100`, `500` |
| `float` | Decimal number | `5.9`, `3.14`, `52.50` |
| `str` | Text / String | `"Vishal"`, `"Surat"` |
| `bool` | True or False only | `True`, `False` |

```python
my_name    = "Vishal Chavda"   # str
my_age     = 18                # int
my_height  = 5.8               # float
is_student = True              # bool

# f-string — mix variables with text
print(f"My name is {my_name} and I am {my_age} years old.")
```

> 💡 **Pro Tip:** Always use `snake_case` for variable names —
> it is the official Python style guide called **PEP 8**!

---

## Lesson 3 — User Input & Type Conversion ✅

> ⌨️ `input()` lets the USER type their own value — making programs interactive!

- 🔹 `input()` always returns a **String** — even if the user types a number!
- 🔹 Need to do math? Convert using `int()` or `float()`
- 🔹 `int()` → converts to whole number
- 🔹 `float()` → converts to decimal number
- 🔹 `str()` → converts to text

```python
name   = input("Enter your name: ")           # already a string ✅
age    = int(input("Enter your age: "))        # convert to int ✅
height = float(input("Enter your height: "))   # convert to float ✅

print(f"In 5 years, {name} will be {age + 5} years old!")
```

> ⚠️ **Warning:** Forgetting `int()` and doing math = `TypeError`!
> 💡 **Pro Tip:** Always ask — *"Do I need math with this value?"*
> If YES → use `int()` or `float()`!

---

## Lesson 4 — Operators ✅

> ➕ Operators are symbols that tell Python to DO something with values!

#### 🔸 Math Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `+` | Add | `10 + 5` | `15` |
| `-` | Subtract | `10 - 5` | `5` |
| `*` | Multiply | `10 * 5` | `50` |
| `/` | Divide | `10 / 3` | `3.333` |
| `//` | Floor Divide | `10 // 3` | `3` |
| `%` | Remainder | `10 % 3` | `1` |
| `**` | Power | `2 ** 3` | `8` |

#### 🔸 Comparison Operators — Always give `True` or `False`

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal | `5 != 3` | `True` |
| `>` | Greater than | `10 > 5` | `True` |
| `<` | Less than | `3 < 1` | `False` |
| `>=` | Greater or equal | `5 >= 5` | `True` |
| `<=` | Less or equal | `3 <= 5` | `True` |

#### 🔸 Logical Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `and` | Both True | `True and True` | `True` |
| `or` | One True | `True or False` | `True` |
| `not` | Flip | `not True` | `False` |

```python
score = 85
print(score >= 50 and score < 100)   # True
print(score % 2 == 0)                # False — 85 is odd!
```

> ⚠️ **Critical:** `=` stores a value. `==` compares. NEVER mix them!
> 💡 **Pro Tip:** Use `%` to check even/odd → `number % 2 == 0` means even!

---

## Lesson 5 — Conditions (if / elif / else) ✅

> 🧠 Conditions give your program a BRAIN — it can make decisions!

- 🔹 `if` → checks first condition
- 🔹 `elif` → checks next condition if first was False
- 🔹 `else` → runs when NO condition above was True
- 🔹 Python checks **top to bottom** — first True wins, rest skip!
- 🔹 **Indentation** (4 spaces) is REQUIRED — forgetting = ERROR!

```python
runs   = int(input("Enter runs: "))
target = int(input("Enter target: "))

if runs > target:
    print("🏆 We WON!")
elif runs == target:
    print("🤝 It's a TIE!")
else:
    difference = target - runs
    print(f"😞 Lost by {difference} runs.")
```

> 💡 **Pro Tip:** Always test **edge cases** — what if value is 0?
> Or exactly equal to the limit? Good developers always think this way!

---

## Lesson 6 — Loops (for & while) ✅

> 🔁 Loops tell Python — "Repeat this again and again until I say stop!"

#### 🔸 The `for` Loop — When you KNOW how many times

- 🔹 Use when repetitions are known in advance
- 🔹 `range(start, stop)` → stop value is NOT included!
- 🔹 `range(1, 11)` → gives 1 to 10
- 🔹 `range(1, 10, 2)` → gives 1, 3, 5, 7, 9 (step of 2)

```python
total = 0
for over in range(1, 6):       # over 1 to 5
    total += 8
    print(f"Over {over}: Total = {total}")
```

#### 🔸 The `while` Loop — When condition controls repeat

- 🔹 Keeps repeating as long as condition is `True`
- 🔹 Always make condition False eventually — or use `break`!
- 🔹 Infinite loop → press `Ctrl + C` to force stop!
- 🔹 `while True + break` → most used pattern in real apps!

```python
secret = 7
while True:
    guess = int(input("Guess: "))
    if guess == secret:
        print("🎉 Correct!")
        break
    else:
        print("❌ Try again!")
```

#### 🔸 for vs while

| Situation | Use |
|-----------|-----|
| Know exactly how many times | `for` |
| Keep going until something changes | `while` |
| Going through a list | `for` |
| Waiting for correct user input | `while` |

> 💡 **Pro Tip:** Use `total += value` instead of `total = total + value` —
> same result, cleaner code. Real developers always use `+=`!

---

## Lesson 7 — Functions ✅

> 🔧 A Function is a reusable block of code — write once, use forever!

- 🔹 `def` keyword creates a function
- 🔹 **Parameters** → inputs given to the function `(name, runs)`
- 🔹 **Return** → sends result back so you can use it later
- 🔹 **Call** → use the function by writing its name + `()`
- 🔹 **Default parameters** → value used when nothing is passed
- 🔹 Functions can call other functions — this is how real apps work!
- 🔹 One function = One job only! (**Single Responsibility**)

```python
# Basic function
def greet(name, city="Surat"):         # city has default value
    print(f"Hello {name} from {city}!")

# Function with return
def calc_run_rate(runs, overs):
    rate = round(runs / overs, 2)
    return rate                         # send result back!

# Functions calling each other
def get_grade(runs):
    if runs >= 100:
        return "🏆 Century! Legend!"
    elif runs >= 50:
        return "⭐ Half Century!"
    elif runs >= 30:
        return "👍 Good knock!"
    else:
        return "😐 Keep practicing!"

def print_report(name, runs, balls):
    rate  = calc_run_rate(runs, balls)  # calling another function!
    grade = get_grade(runs)             # calling another function!
    print(f"""
═══════════════════════════
🏏 CRICKET REPORT
Player  : {name}
Runs    : {runs}
SR      : {rate}
Grade   : {grade}
═══════════════════════════""")

print_report("Vishal", 85, 50)
```

> 💡 **Pro Tip:** Function name should tell you EXACTLY what it does —
> just by reading it! This is called **self-documenting code**!

---

## Lesson 8 — Lists, Tuples, Dictionaries & Sets ✅

> 📦 Data Structures store MULTIPLE values in ONE variable!

#### 🔸 Quick Memory Trick — Pizza Party! 🍕

```
LIST   → Guest list   — ordered, add/remove anytime      [ ]
TUPLE  → Pizza recipe — fixed steps, NEVER change        ( )
DICT   → Guest orders — each person's specific order    { : }
SET    → Unique toppings — no repeats, ever!             { }
```

#### 🔸 LIST `[ ]` — Ordered & Changeable

- 🔹 Items stay in the order you put them
- 🔹 Can add, remove, update items
- 🔹 Allows duplicate values
- 🔹 **Index starts from 0** — not 1! ⚠️
- 🔹 Negative index → `-1` = last item

```python
players = ["Vishal", "Rohit", "Dhoni", "Kohli"]

print(players[0])         # Vishal  — first item
print(players[-1])        # Kohli   — last item
print(len(players))       # 4

players.append("Bumrah")  # add at end
players.insert(1, "SKY")  # add at position
players.remove("Rohit")   # remove by value
players.pop()             # remove last item

# Loop through list
for i, player in enumerate(players, 1):
    print(f"{i}. {player}")
```

#### 🔸 TUPLE `( )` — Ordered & FIXED

- 🔹 Cannot add, remove or update once created
- 🔹 Use for data that should NEVER change
- 🔹 Faster than lists for fixed data

```python
ipl_teams = ("MI", "CSK", "RCB", "KKR", "SRH")
print(ipl_teams[0])    # MI
print(len(ipl_teams))  # 5
# ipl_teams[0] = "DC"  ← ERROR! Cannot change tuple!
```

#### 🔸 DICTIONARY `{ key: value }` — Key-Value Pairs

- 🔹 Access values using KEY name — not index number
- 🔹 Keys must be unique
- 🔹 Can add, update, remove key-value pairs
- 🔹 Best for structured data like profiles

```python
player = {
    "name"   : "Vishal Chavda",
    "age"    : 18,
    "city"   : "Surat",
    "runs"   : 850,
    "team"   : "MI"
}

print(player["name"])       # Vishal Chavda
player["runs"] = 1000       # update value
player["wickets"] = 25      # add new key
del player["age"]           # remove key

# Loop through dictionary
for key, value in player.items():
    print(f"{key} : {value}")
```

#### 🔸 SET `{ }` — Unique Values Only

- 🔹 Automatically removes duplicates
- 🔹 No order — no index access
- 🔹 Best for checking membership and unique collections

```python
countries = {"India", "Australia", "England", "India"}
print(countries)              # {'India', 'Australia', 'England'}

countries.add("West Indies")
countries.remove("England")
print("India" in countries)   # True
```

#### 🔸 Combine List + Dictionary (Most Powerful! 🔥)

```python
team = [
    {"name": "Vishal", "runs": 85,  "balls": 50},
    {"name": "Rohit",  "runs": 120, "balls": 80},
    {"name": "Dhoni",  "runs": 60,  "balls": 30},
]

for player in team:
    sr = round((player["runs"] / player["balls"]) * 100, 2)
    print(f"🏏 {player['name']} → Runs: {player['runs']} | SR: {sr}")
```

#### 🔸 All 4 Compared

| Feature | List `[]` | Tuple `()` | Dict `{}` | Set `{}` |
|---------|-----------|------------|-----------|---------|
| Ordered | ✅ | ✅ | ✅ | ❌ |
| Changeable | ✅ | ❌ | ✅ | ✅ |
| Duplicates | ✅ | ✅ | ❌ keys | ❌ |
| Access by | Index | Index | Key | — |

> 💡 **Pro Tip:** List of Dictionaries is the most used pattern in
> real Python — APIs, databases, and JSON data all look exactly like this!

---

# 🎮 PROJECT — Quiz Game (Built from Scratch!)

> Vishal built a fully working Quiz Game using ONLY Lessons 1-6!
> No tutorials. No help. Pure self-learning! 🏆

#### Features built:
- 🔹 Multiple questions with options
- 🔹 User input for answers
- 🔹 Score tracking with `score += 1`
- 🔹 Correct / Wrong feedback with emojis
- 🔹 Final score display

```python
print("Welcome to the Quiz Game! 🎉")
score = 0

# Question 1
print("\nQuestion 1: What is 2+2?")
print("a) 3  b) 4  c) 5")
answer = input("Enter your answer: ")
if answer == "b":
    print("Correct! ✅")
    score += 1
else:
    print("Wrong! ❌")

print(f"\nYour final score: {score}/3 🎮")
```

> 🚀 **Next Version — Quiz Game BEAST MODE** coming soon!
> Will use: Lists + Dictionaries + Functions + Score grades!

---

# ⏳ STAGE 2 — OOP (Object Oriented Programming) — UP NEXT!

> 🔵 The biggest concept jump in Python — thinking in objects!

#### What's Coming:

- 🔹 **Classes & Objects** → Blueprint and real things made from it
  - Class = blueprint (design) of a car 🚗
  - Object = actual car made from that blueprint!
- 🔹 **`__init__` method** → runs automatically when object is created
- 🔹 **`self` keyword** → refers to the object itself
- 🔹 **Inheritance** → one class getting all properties of another
- 🔹 **Encapsulation** → hiding data safely inside a class
- 🔹 **Polymorphism** → same method, different behaviour
- 🔹 **Magic Methods** → `__str__`, `__len__`, `__repr__` and more

---

# ⏳ STAGE 3 — File Handling & APIs — PENDING

#### What's Coming:
- 🔹 **Reading & Writing Files** → `.txt`, `.csv`, `.json`
- 🔹 **Exception Handling** → `try` / `except` — handle errors gracefully
- 🔹 **Working with APIs** → `requests` library — get live data!
- 🔹 **Parsing JSON** → reading real API responses

---

# ⏳ STAGE 4 — Data Structures & Algorithms — PENDING

#### What's Coming:
- 🔹 **Stacks & Queues** → special ways to organise data
- 🔹 **Linked Lists** → chain of connected data nodes
- 🔹 **Searching** → Linear search & Binary search
- 🔹 **Sorting** → Bubble sort, Merge sort, Quick sort
- 🔹 **Recursion** → functions that call themselves!

---

## 🗂️ File Structure

```
📁 PYTHON/
│
├── 📁 basic/
│   │
│   └── 📁 practice/
│       ├── 🐍 functions_practice.py    # Lesson 7 — Functions
│       ├── 🐍 list_tuples_sets.py      # Lesson 8 — Data Structures
│       ├── 🐍 mid_level_practice.py    # Intermediate practice
│       ├── 🐍 practice_question.py     # All exercises (139+ lines!)
│       ├── 🐍 quiz_game.py             # 🎮 Self-built Quiz Game!
│       ├── 🐍 condition_practice.py    # Lesson 5 — Conditions
│       ├── 🐍 function.py              # Function experiments
│       ├── 🐍 Loops_for_while.py       # Lesson 6 — Loops
│       ├── 🐍 main.py                  # First programs
│       └── 📄 README.md               # This file!
```

---

## 🛠️ Tools & Setup

- 💻 **Editor:** VS Code (Visual Studio Code)
- 🌐 **Online Compiler:** [Programiz](https://www.programiz.com/python-programming/online-compiler/)
- 🐍 **Python Version:** 3.9.6 (xcode)
- 🖥️ **Terminal:** zsh — macOS
- 📦 **Libraries used so far:** None — pure Python!

---

## 🏆 Key Milestones

| Date | Achievement |
|------|-------------|
| May 18, 2026 | Started Python — first `print()` |
| May 18, 2026 | Installed VS Code — ran first terminal command |
| May 19, 2026 | Built Quiz Game from scratch — self taught! |
| May 19, 2026 | Used `while True + break` without being taught! |
| May 20, 2026 | ✅ **Stage 1 COMPLETE — 8/8 Lessons!** |
| May 20, 2026 | Built Cricket Report Generator with Functions |

---

## 💬 About This Journey

> *"Vishal started with zero coding experience on May 18, 2026.
> By May 20 — just 3 days later — he had completed all 8 lessons
> of Stage 1, built multiple real programs, installed VS Code,
> run code in terminal, and self-built a Quiz Game without being asked.
> That is not beginner behaviour. That is developer DNA."*
>
> — PyGuru 🐍

---

*📅 Last Updated: May 20, 2026*
*🐍 Stage 1 Complete — Stage 2 OOP Loading... 🔵*