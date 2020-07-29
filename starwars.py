#Star wars trivia game

import random

def get_tof_statements(): #
    statements = []
    statements.append(["Darth vader is lukes father", "T"])
    statements.append(["Obi wan built C3-PO", "F"])
    statements.append(["Padme is Queen Amidala", "T"])
    statements.append(["Mace Windu is killed by Darth Maul", "F"])
    statements.append(["Luke kissed his sister", "T"])
    statements.append(["Luke was born on Hoth", "F"])
    statements.append(["Han solo shot first", "T"])
    statements.append(["Bobo Fett is Jango Fetts father", "F"])
    statements.append(["R2 and C3PO are the droids you are looking for", "F"])
    statements.append(["The Millennium Falcon completed the Kessle Run in less than 10 parsecs", "F"])
    return statements

def play_tof_quiz():

    tof_statements = get_tof_statements()
    # Randomise tof statements
    random.shuffle(tof_statements)
    # Set player score to 0
    score = 0

    # Show tof statements using a loop
    for s in tof_statements:
         # present statement
        print("True or False:" + s[0])
        # user enter guess
        guess = input("Enter T or F: ")
        # check if guess is correct
        if guess == s[1]:
            print("The force is strong with this one!")
            # update score
            score = score + 1
        else:
            print("I got a bad feeling about this")
    # Show final score
    print(f' {score} out of 10')
    if score == 10:
        print("You are a Jedi Master")
    else:
        print("You do not advance to the rank of Master")
play_tof_quiz()
