print("welcom to quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play:)")
Score = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    Score += 1
else:
    print('Incorrect!')

answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    Score += 1
else:
    print('Incorrect!')

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    Score += 1
else:
    print('Incorrect!')

answer = input("What does ROM stands for? ")
if answer.lower() == "read only memory":
    print('Correct!')
    Score += 1
else:
    print('Incorrect!')

answer = input("What does PSU stands for? ")
if answer.lower() == "power supply":
    print('Correct!')
    Score += 1
else:
    print('Incorrect!')

print("You got " + str(Score) + "questions correct!")
print("You got " + str((Score / 5) * 100) + "%.")
print("well play!")