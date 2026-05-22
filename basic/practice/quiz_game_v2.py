# ================================================
# 🎮 QUIZ GAME — BEAST MODE
# Built by: Vishal Chavda
# Uses: Lists, Dicts, Functions, Loops, Conditions
# ================================================

# ---- QUESTIONS — stored as List of Dictionaries!

questions = [
    {
        "question:":"what is 2 + 2?",
        "options":" a) 3\nb) 4\nc) 5\nd) 6",
        "answer":"b"
    },
    {
        "question":"what is the capital of France?",
        "options":" a) Berlin\nb) Madrid\nc) Paris\nd) Rome",
        "answer":"c"
    },
    {
        "question":"what is the largest planet in our solar system?",
        "options":" a) Earth\nb) Mars\nc) Jupiter\nd) Saturn",
        "answer":"c"
    },{
        "question":"what is the chemical symbol for water?",
        "options":" a) H2O\nb) CO2\nc) O2\nd) NaCl",
        "answer":"a"
    }
]

# ---- function 1 ask the question
def ask_question(number , q_data):
    print(f"\n={'='*40}")
    print(f"❓ Question {number} : {q_data['question']}")
    print(f"   Topic: {q_data['topic']}")
    print(f"{'='*40}")

    for options in q_data['options']:
        print(f"options: {options}")
    
        answer = input("Your answer (a/b/c/d): ").lower()
        
        if answer == q_data['answer']:
          print("✅ Correct!")
          return 1
        else:
          print("❌ Wrong! The correct answer was:", q_data['answer'])
          return 0

# ---- function 2 get final grade
def get_grade(score , total):
    percentage = (score / total) * 100
    if percentage == 100:
        return "🏆 PERFECT SCORE! You are a GENIUS!"
    elif percentage >= 80:
        return "⭐ Excellent! Outstanding performance!"
    elif percentage >= 60:
        return "👍 Good job! Keep learning!"
    elif percentage >= 40:
        return "🙂 Not bad! Practice more!"
    else:
        return "💪 Keep going! You'll get better!"

#  function 3  show final report

def final_result(name , score , total ,wrong_list):

    percentage = round((score / total)* 100 , 1)
    grade = get_grade(score , total)

    print(f"\n{'='*40}")
    print(f"🎮  GAME OVER — FINAL REPORT")
    print(f"{'='*40}")
    print(f"👤  Player    : {name}")
    print(f"✅  Correct   : {score}/{total}")
    print(f"❌  Wrong     : {total - score}/{total}")
    print(f"📊  Score     : {percentage}%")
    print(f"🏅  Grade     : {grade}")

    if wrong_list:
        print(f"\n📝 Questions you got wrong:")
        for q in wrong_list:
            print(f"   ❌ {q}")

    print(f"{'='*40}")


# ---- MAIN GAME LOGIC

def play_game():
    print(f"{'='*40}")
    print(" 🎮 WELCOME TO THE QUIZ GAME — BEAST MODE! 🎮 ")
    print(f"{'='*40}")

    name = input("Enter your name: ")
    score = 0
    wrong_list = []
