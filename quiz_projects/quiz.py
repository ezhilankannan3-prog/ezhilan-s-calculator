import json
import os 
import random 
import time 

HIGH_SCORE_FILE="highscore.json"

QUESTIONS={
    "python":[
        ("which keyword defines as function",["func","def","key","dff"],2),
        ("Which data type is immutable",["list","dict","tuple","set"],3),
        ("What does len('Python') return?", ["5", "6", "7", "Error"], 2),
        ("Which symbol starts a comment?", ["//", "/*", "#", "--"], 3),
        ("What is 2 ** 3?", ["6", "8", "9", "5"], 2),
    ],
    "General": [
        ("What is the capital of India?", ["Mumbai", "Delhi", "Chennai", "Kolkata"], 2),
        ("How many days are in a leap year?", ["365", "366", "364", "360"], 2),
        ("Which planet is known as the Red Planet?", ["Venus", "Jupiter", "Mars", "Saturn"], 3),
        ("Who wrote the Indian national anthem?", ["Tagore", "Gandhi", "Nehru", "Bose"], 1),
        ("What is H2O commonly called?", ["Salt", "Water", "Acid", "Oxygen"], 2),
    ],
}

def high_load_score():
    if os.path.exists(HIGH_SCORE_FILE):
        try:
            with open(HIGH_SCORE_FILE,"r") as f:
                return json.load(f)
        except(json.JSONDecodeError,OSError):
                pass
    return {"name":"-","score":0}   


def high_score(name,score):
     with open(HIGH_SCORE_FILE,"w") as f:
        json.dump({"name":name,"score":score},f)

 
def choose_cateorgy():
     categories=list(QUESTIONS.keys())
     for i ,cat in enumerate(categories,start=1):
          print(f"{i}. {cat}") 
     while True:
          choice=input("Enter your Choice: ").strip() 
          if choice.isdigit() and 1<=int(choice)<=len(categories):
            return categories [int(choice)-1] 
          print("invalid choice try again")


def ask_questions(number,question,options,correct):
    print(f"\nQ{number}.{question}")
    for i , opt in enumerate(options,start=1):
        print(f"{i}.{opt}")          
    while True:
        answer=input("Enter your answer(1-4):").strip()
        if answer in ("1","2","3","4"):
            return int(answer)==correct
        print("please enter the valid answer (1 to 4)")


def run_quiz():
    print("====QUIZ GAME===")        
    name=input("Enter your name:").strip() or "player"
    category=choose_cateorgy()

    questions=QUESTIONS[category]
    random.shuffle(questions)
    score=0
    start=time.time()


    for number,(q,options,correct) in enumerate(questions,start=1):
        if ask_questions(number,q,options,correct):
            print("correct")
            score+= 1
        else:
            print(f"wrong!! correct is {options[correct -1]}")

    elapsed=time.time()-start
    total=len(questions)    


    print("===RESULT===")
    print(f"{name},your score is {score}/{total} ({score/total*100:.0f})%")
    print(f"Time Taken {elapsed:.1f}seconds")


    best=high_load_score()
    if score >best["score"]:
      print("New high score")
      high_score(name,score)
    else:
        print(f"High Score: {best['score']} by {best['name']}")

def main():
    while True:
      run_quiz()
      again=input("\n do you want play again y/n: ").strip().lower() 
      if again != "y":
        print("===Thanks for playing===")
        break

if __name__=="__main__":
    main()