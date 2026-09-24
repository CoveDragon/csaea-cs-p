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






