# 5. Login Screen

password = input("Input Password: ")
CorrectPassword = "CSAEA2026"
FailsLeft = 3
PasswordWrong = False
PasswordWrong2 = False


if password == CorrectPassword:
    print("access granted")
if password == "skip":
    print("Skipping...")
else:
    print("access denied")
    FailsLeft -= 1
    print(f"{FailsLeft} attempts remaining")
    PasswordWrong = True
if PasswordWrong == True:
    password2 = input("Input Password: ")
if password2 == CorrectPassword:
    print("access granted")
else:
    print("access denied")
    FailsLeft -= 1
    print(f"{FailsLeft} attempts remaining")
    PasswordWrong2 = True
if PasswordWrong2 == True:
    password3 = input("Input Password: ")
if password3 == CorrectPassword:
    print("access granted")
else:
    print("access denied, try again")

# 8. Name Tag Generator

FirstName = input("Fist Name: ")
LastName = input("Last Name: ")
School = input("Your School: ")
print(f"Hello, my name is {FirstName} {LastName}, from {School}")

# 6. Even/Odd Parking

plate = 4827

SideNumber = plate % 2
print(SideNumber)
if SideNumber == 1:
    print("Park on the WEST side.")
else:
    print("Park on the EAST side.")

# 20. Speed Trap
speed_limit = 55
speed = 71

if speed <= speed_limit:
    print("Nice!")
elif speed <= speed_limit + 11:
    print("100$ fine...")

# 8. HIGH SCORE (gameshow)

PlayerScore = 0
scores = [340, 1250, 980, 1510, 720]
QuestionRepo1 = ["Is the square root of 225 16?", "Is 12 * 10 130?", "Is pythagrean's theorum a^2/b^2=c^2?"]
QuestionRepo2 = ["Is the capitol of france Paris?", "Is a mountain a tectonic plate meeting another?", "Is the US established in 1776?"]
QuestionRepo3 = ["Does rain consist of not only water, but also uranium?", "Is an Isotope the number of protons in an atom", "is a molecule secretly a mango?"]

import time
import random
question1 = random.choice(QuestionRepo1)
question2 = random.choice(QuestionRepo2)
question3 = random.choice(QuestionRepo3)

print("Welcome to TRIVIA!")
time.sleep(0.2)
print("Answer these THREE questions")
time.sleep(0.2)
print("answer either T (true) or F (false)")
time.sleep(0.2)
Answer1 = input(f"Question 1: {question1}: ")

if Answer1 == "F":
    print("YAY YOU GOT IT RIGHT +200 SCORE!!!")
    PlayerScore += 200
else:
    print("You got it wrong D=")
time.sleep(0.2)
print("Next question...")
Answer2 = input(f"Question 2: {question2}: ")

if Answer2 == "T":
    print("CORRECT +300 SCORE")
    PlayerScore += 300
else:
    print("WRONG WOMP WOMP")

time.sleep(0.2)
print("Final question...")
time.sleep(0.5)
print("DOUBLE POINTS!")
time.sleep(0.5)
Answer3 = input(f"FINAL QUESTION!: {question3}: ")

if Answer3 == "F":
    print("CORRECT YESS! +650 score!")
    PlayerScore += 650
else:
    print("you are a failure.")

time.wait(0.7)
print(f"Other peoples scores: {scores}")
time.wait(0.5)
print(f"your score was: {PlayerScore}")


 # 15. Pass rate

grades = [88, 65, 72, 91, 54, 70]
passing = 70

if grades[0] >=70:
    print("#0 passed")
else:
    print("#0 failed")
if grades[1] >=70:
    print("#1 passed")
else:
    print("#1 failed")
if grades[2] >=70:
    print("#2 passed")
else:
    print("#2 failed")
if grades[3] >=70:
    print("#3 passed")
else:
    print("#3 failed")
if grades[4] >=70:
    print("#4 passed")
else:
    print("#4 failed")
if grades[5] >=70:
    print("#5 passed")
else:
    print("#5 failed")
