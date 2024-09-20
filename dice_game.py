import random

def welcome():
    print("Welcome to Dice Game")
    playerinput = input("Press 'q' to play or any other key to quit: ").upper()

    if playerinput == "Q":
        dicey()
    else:
        print("Hee Hee Ha Ha")
        return

def roll_dice(dice_sides):
    return random.randint(1, dice_sides)

def dicey():
    print("Rolling a D4...")
    roll_d4 = roll_dice(4)
    print(f"D4 roll: {roll_d4}")

    if roll_d4 == 4:
        print("You rolled a 4! Now rolling a D6...")
        roll_d6 = roll_dice(6)
        print(f"D6 roll: {roll_d6}")

        if roll_d6 == 6:
            print("You rolled a 6! Now rolling a D8...")
            roll_d8 = roll_dice(8)
            print(f"D8 roll: {roll_d8}")

            if roll_d8 == 8:
                print("You rolled an 8! Now rolling a D10...")
                roll_d10 = roll_dice(10)
                print(f"D10 roll: {roll_d10}")

                if roll_d10 == 10:
                    print("You rolled a 10! Now rolling a D20...")
                    roll_d20 = roll_dice(20)
                    print(f"D20 roll: {roll_d20}")

                    if roll_d20 == 20:
                        print("YOU WIN!!!!")
                    else:
                        print("Didn't roll a 20 on the D20. Game over. Almost there!")
                        welcome()
                else:
                    print("Didn't roll a 10 on the D10. Game over. Tisk, Tisk.")
                    welcome()
            else:
                print("Didn't roll an 8 on the D8. Game over. You suck.")
                welcome()
        else:
            print("Didn't roll a 6 on the D6. Game over. Be better.")
            welcome()
    else:
        print("Didn't roll a 4 on the D4. Game over. HAHA.")
        welcome()

# Start the game
welcome()

        

    




    