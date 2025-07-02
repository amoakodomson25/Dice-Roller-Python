import random


def dice_roller():
    while True:
        try:
            print()

            print("Dice Roller")
            print('-----------')
            print("<1> 1 dice")
            print("<2> 2 dice")
            print("<5> Any number of dice")
            print("<99> quit")
            dice_1 = random.randint(1, 6)
            dice_2 = random.randint(1, 6)
            print()
            dice_number = int(input("How many dice do you want to roll?: "))
            if dice_number == 99:
                print()
                quit_game = input("do you want to quit (Y/N):  ").lower()
                if quit_game == "y":
                    print("Thanks for playing")
                    break
                elif quit_game == "n":
                    continue
                    dice_roller()
                else:
                    print("Type Y for Yes and N for No")
            elif dice_number == 1:
                print()
                print(f"The outcome was; {dice_1}")
                continue
                dice_roller()

            elif dice_number == 2:
                print()
                print(f"The outcome was; {dice_1} & {dice_2}")
                continue
                dice_roller()
            elif dice_number == 5:
                dice_number_2 = int(input("How many dice: "))
                rolls = [random.randint(1, 6) for _ in range(dice_number_2)]
                outcome = ' & '.join(str(roll) for roll in rolls)
                print(f"The outcome was; {outcome}")
                continue
                dice_roller()
            else:
                print()
                print("Select one of the options")
                continue
                dice_roller()
        except ValueError:
            print()
            print("Input a valid number")
            continue
            dice_roller()


dice_roller()
