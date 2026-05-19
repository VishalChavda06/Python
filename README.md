# 🐍 Python Learning Journey — Vishal Chavda

![Python](https://img.shields.io/badge/Python-3.9.6-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange?style=for-the-badge)
![Stage](https://img.shields.io/badge/Stage-1%20Basics-green?style=for-the-badge)
![Lessons](https://img.shields.io/badge/Lessons%20Done-6%20of%2016-yellow?style=for-the-badge)

> 🎓 **Taught by:** PyGuru — A friendly AI Python Tutor
> 📅 **Started:** May 18, 2026
> 💻 **Editor:** VS Code + Programiz Online Compiler
> 🖥️ **OS:** macOS

---

## 📊 Overall Progress

| Stage | Topic | Status | Progress |
|-------|-------|--------|----------|
| 🟢 Stage 1 | Python Basics | 🔄 In Progress | 6 / 8 Lessons |
| 🔵 Stage 2 | Object Oriented Programming (OOP) | ⏳ Pending | 0 / 4 Lessons |
| 🟣 Stage 3 | File Handling & APIs | ⏳ Pending | 0 / 4 Lessons |
| 🔴 Stage 4 | Data Structures & Algorithms | ⏳ Pending | 0 / 4 Lessons |

---

## ✅ STAGE 1 — Python Basics

### Lesson 1 — What is Python & `print()` ✅

> 🐍 Python is a programming language used to talk to the computer — like a language, but for machines!

- 🔹 Python is one of the most popular languages in the world
- 🔹 Used in Web Development, AI, Data Science, Automation & more
- 🔹 Very beginner friendly — reads almost like normal English
- 🔹 `print()` is the first function every Python developer learns
- 🔹 Whatever you write inside `print(" ")` gets displayed on the screen

```python
print("Hello, World!")         # Output: Hello, World!
print("I am learning Python!") # Output: I am learning Python!
```

💡 **Pro Tip:** Real developers use `print()` for debugging — checking what is happening inside their code!

---

### Lesson 2 — Variables & Data Types ✅

> 📦 A Variable is like a labeled box — you give it a name and store a value inside it!

#### 🔸 What is a Variable?
- 🔹 A variable stores a value that you can use later in your program
- 🔹 You create a variable by writing: `variable_name = value`
- 🔹 Variable names should be clear and descriptive
- 🔹 Python uses **snake_case** style → `my_name`, `total_runs`, `is_student`

#### 🔸 The 4 Main Data Types

| Data Type | Meaning | Example |
|-----------|---------|---------|
| `int` | Whole number (કોઈ દશાંશ નહીં) | `18`, `100`, `500` |
| `float` | Decimal number (દશાંશ સાથે) | `5.9`, `3.14`, `52.50` |
| `str` | Text / String (અક્ષરો) | `"Vishal"`, `"Surat"` |
| `bool` | True or False only (હા કે ના) | `True`, `False` |

```python
my_name    = "Vishal Chavda"   # str   → text
my_age     = 18                # int   → whole number
my_height  = 5.8               # float → decimal number
is_student = True              # bool  → True or False
```

#### 🔸 f-Strings — Print Variables with Text
- 🔹 f-strings let you mix variables inside text easily
- 🔹 Put `f` before the quotes and wrap variables in `{ }`

```python
print(f"My name is {my_name} and I am {my_age} years old.")
# Output: My name is Vishal Chavda and I am 18 years old.
```

💡 **Pro Tip:** Always use `snake_case` for variable names in Python — it is the official Python style (called PEP 8)!

---

### Lesson 3 — User Input & Type Conversion ✅

> ⌨️ Instead of writing values yourself, `input()` lets the USER type their own value — like a real app!

#### 🔸 What is `input()`?
- 🔹 `input()` pauses the program and waits for the user to type something
- 🔹 It always returns a **String** — even if the user types a number!
- 🔹 Whatever message you write inside `input(" ")` is shown to the user

#### 🔸 What is Type Conversion?
- 🔹 Since `input()` always gives a string, we need to **convert** it when we want to do math
- 🔹 `int()` → converts to whole number
- 🔹 `float()` → converts to decimal number
- 🔹 `str()` → converts to text

```python
name   = input("Enter your name: ")           # already a string ✅
age    = int(input("Enter your age: "))        # convert to int for math ✅
height = float(input("Enter your height: "))   # convert to float ✅

print(f"In 5 years, {name} will be {age + 5} years old!")
```

⚠️ **Warning:** If you forget `int()` and try to do math — Python will give a `TypeError`!

💡 **Pro Tip:** Always ask yourself — *"Do I need to do math with this value?"* If YES → use `int()` or `float()`!

---

### Lesson 4 — Operators ✅

> ➕ Operators are special symbols that tell Python to DO something with your values!

#### 🔸 Math Operators (ગણિત)

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `+` | Add | `10 + 5` | `15` |
| `-` | Subtract | `10 - 5` | `5` |
| `*` | Multiply | `10 * 5` | `50` |
| `/` | Divide | `10 / 3` | `3.333` |
| `//` | Floor Divide (whole number only) | `10 // 3` | `3` |
| `%` | Modulus / Remainder (બાકીનું) | `10 % 3` | `1` |
| `**` | Power / Exponent (ઘાત) | `2 ** 3` | `8` |

#### 🔸 Comparison Operators (સરખામણી) — Always give `True` or `False`

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `10 > 5` | `True` |
| `<` | Less than | `3 < 1` | `False` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `3 <= 5` | `True` |

#### 🔸 Logical Operators (તર્કિક)

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `and` | Both must be True | `True and True` | `True` |
| `or` | At least one True | `True or False` | `True` |
| `not` | Flip True↔False | `not True` | `False` |

```python
score = 85
print(score >= 50 and score < 100)   # True — both conditions met!
print(score % 2 == 0)                # False — 85 is odd!
```

⚠️ **Critical:** `=` stores a value. `==` compares values. NEVER mix them up!

💡 **Pro Tip:** Use `%` to check even/odd → `number % 2 == 0` means even!

---

### Lesson 5 — Conditions (if / elif / else) ✅

> 🧠 Conditions give your program a BRAIN — it can look at a situation and decide what to do!

#### 🔸 How it works
- 🔹 `if` → checks the first condition
- 🔹 `elif` → checks the next condition (if first was False)
- 🔹 `else` → runs when NO condition above was True
- 🔹 Python checks **top to bottom** — first True condition wins, rest are skipped!
- 🔹 **Indentation** (4 spaces) is REQUIRED inside every if/elif/else block

#### 🔸 Structure

```python
if condition:
    # runs if condition is True
elif another_condition:
    # runs if this condition is True
else:
    # runs when nothing above matched
```

#### 🔸 Real Example — IPL Match Result

```python
runs   = int(input("Enter runs: "))
target = int(input("Enter target: "))

if runs > target:
    print("🏆 We WON the match!")
elif runs == target:
    print("🤝 It's a TIE!")
else:
    difference = target - runs
    print(f"😞 We lost by {difference} runs.")
```

#### 🔸 Conditions with `and` / `or`

```python
age    = int(input("Enter age: "))
has_id = input("Have ID? (yes/no): ")

if age >= 18 and has_id == "yes":
    print("✅ Entry allowed!")
elif age >= 18 and has_id == "no":
    print("⚠️ Bring your ID!")
else:
    print("❌ Too young to enter!")
```

⚠️ **Warning:** Forgetting indentation = instant Python ERROR!

💡 **Pro Tip:** Always test your conditions with **edge cases** — like what if the value is 0? Or exactly equal to the limit?

---

### Lesson 6 — Loops (for & while) ✅

> 🔁 A Loop tells Python — "Repeat this again and again until I say stop!"

#### 🔸 The `for` Loop — When you KNOW how many times

- 🔹 Use `for` when the number of repetitions is known
- 🔹 `range(start, stop)` → generates numbers from start to stop-1
- 🔹 `range(1, 11)` → gives 1, 2, 3 ... 10 (11 is NOT included!)
- 🔹 `range(1, 10, 2)` → gives 1, 3, 5, 7, 9 (step of 2)

```python
# Print each over's score
total = 0
for over in range(1, 6):       # over 1 to 5
    total += 8                 # add 8 runs each over
    print(f"Over {over}: Total = {total}")
```

#### 🔸 The `while` Loop — When condition controls the repeat

- 🔹 Use `while` when you don't know exactly how many times
- 🔹 Keeps repeating as long as the condition is `True`
- 🔹 Always make sure the condition eventually becomes `False` — or use `break`!
- 🔹 **Infinite loop** = loop that never stops → press `Ctrl + C` to force stop!

```python
# Number guessing game
secret = 7
while True:                              # keep going forever...
    guess = int(input("Guess: "))
    if guess == secret:
        print("🎉 Correct!")
        break                            # ...until we break out!
    else:
        print("❌ Try again!")
```

#### 🔸 for vs while — Quick Guide

| Situation | Use |
|-----------|-----|
| Know exactly how many times | `for` loop |
| Keep going until something changes | `while` loop |
| Going through a list | `for` loop |
| Waiting for correct user input | `while` loop |

#### 🔸 Loop + Condition Combo (Very Powerful! 🔥)

```python
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is even ✅")
    else:
        print(f"{i} is odd ❌")
```

💡 **Pro Tip:** Use `total += value` instead of `total = total + value` — same result, cleaner code! Real developers always use `+=`!

---

## ⏳ PENDING LESSONS

### 🟢 Stage 1 — Still to Complete

#### Lesson 7 — Functions ⏳
> A Function is a reusable block of code that does one specific job!
- 🔹 Write code once — use it 100 times
- 🔹 Uses `def` keyword to define a function
- 🔹 Can take **parameters** (inputs) and **return** values (outputs)
- 🔹 Keeps code clean, organised, and non-repetitive

#### Lesson 8 — Lists, Tuples, Dictionaries & Sets ⏳
> Data Structures that store multiple values in one variable!
- 🔹 **List** → ordered, changeable collection → `[1, 2, 3]`
- 🔹 **Tuple** → ordered, unchangeable collection → `(1, 2, 3)`
- 🔹 **Dictionary** → key-value pairs → `{"name": "Vishal", "age": 18}`
- 🔹 **Set** → unique values only, no duplicates → `{1, 2, 3}`

---

### 🔵 Stage 2 — OOP (Object Oriented Programming) ⏳

#### What's Coming:
- 🔹 **Classes & Objects** → Blueprint and real things made from it
- 🔹 **`__init__` method & `self`** → How objects are created
- 🔹 **Inheritance** → One class getting properties of another
- 🔹 **Encapsulation** → Hiding data inside a class
- 🔹 **Polymorphism** → Same method, different behaviour
- 🔹 **Magic Methods** → `__str__`, `__len__`, and more

---

### 🟣 Stage 3 — File Handling & APIs ⏳

#### What's Coming:
- 🔹 **Reading & Writing Files** → `.txt`, `.csv`, `.json`
- 🔹 **Exception Handling** → `try` / `except` to handle errors gracefully
- 🔹 **Working with APIs** → Using `requests` library to get live data
- 🔹 **Parsing JSON** → Reading API responses

---

### 🔴 Stage 4 — Data Structures & Algorithms ⏳

#### What's Coming:
- 🔹 **Stacks & Queues** → Special ways to organise data
- 🔹 **Linked Lists** → Chain of connected data nodes
- 🔹 **Searching** → Linear search & Binary search
- 🔹 **Sorting** → Bubble sort, Merge sort, Quick sort
- 🔹 **Recursion** → Functions that call themselves!

---

## 🗂️ File Structure

```
📁 PYTHON/
│
├── 📁 basic/
│   ├── 🐍 main.py                  # First programs & examples
│   ├── 🐍 practice_question.py     # All practice exercises (139+ lines!)
│   ├── 🐍 condition_practice.py    # Lesson 5 — if/elif/else practice
│   ├── 🐍 Loops_for_while.py       # Lesson 6 — for & while loops
│   ├── 🐍 mid_level_practice.py    # Intermediate level practice
│   └── 📄 README.md                # This file!
```

---

## 🛠️ Tools & Setup

- 💻 **Editor:** VS Code (Visual Studio Code)
- 🌐 **Online Compiler:** [Programiz Python Compiler](https://www.programiz.com/python-programming/online-compiler/)
- 🐍 **Python Version:** 3.9.6 (xcode)
- 🖥️ **Terminal:** zsh — macOS
- 📦 **No extra libraries needed** for Stage 1!

---

## 🏆 Key Concepts Learned So Far

```python
# ✅ print()
print("Hello World!")

# ✅ Variables & Data Types
name = "Vishal"       # str
age  = 18             # int
gpa  = 9.2            # float
active = True         # bool

# ✅ User Input & Type Conversion
age = int(input("Enter age: "))

# ✅ Operators
result = (runs / balls) * 100    # math
is_win = score >= target         # comparison → True/False
valid  = age >= 18 and has_id    # logical

# ✅ Conditions
if score > target:
    print("Won!")
elif score == target:
    print("Tie!")
else:
    print("Lost!")

# ✅ Loops
for i in range(1, 6):       # for loop
    print(i)

while True:                  # while loop
    guess = int(input())
    if guess == 7:
        break
```

---

## 📈 Progress Tracker

```
Stage 1 — Basics        ████████████░░░░  6/8  Lessons ✅
Stage 2 — OOP           ░░░░░░░░░░░░░░░░  0/4  Lessons ⏳
Stage 3 — Files & APIs  ░░░░░░░░░░░░░░░░  0/4  Lessons ⏳
Stage 4 — DSA           ░░░░░░░░░░░░░░░░  0/4  Lessons ⏳

Overall: ████░░░░░░░░░░░░  6/20  Lessons Complete (30%)
```

---

## 💬 About This Journey

> *"Every expert was once a beginner. Vishal started with zero coding experience and is now writing real Python programs in VS Code, running them in terminal, and organising code like a professional developer — all within the first 2 days!"*
>
> — PyGuru 🐍

---

*📅 Last Updated: May 19, 2026*
*🐍 Keep Coding, Keep Growing — Jai Python! 🙏*