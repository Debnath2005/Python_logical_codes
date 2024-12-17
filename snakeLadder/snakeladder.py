import random

def roll_dice():
    return random.randint(1, 6)

def play_snake_and_ladder():
    position = 0
    dice_rolls = 0

    while position < 100:
        dice_rolls += 1
        dice = roll_dice()
        move = random.choice(["No Play", "Ladder", "Snake"])

        if move == "No Play":
            pass 
        elif move == "Ladder":
            position += dice
        elif move == "Snake":
            position -= dice
        
        
        if position < 0:
            position = 0
        elif position > 100:
            position -= dice

        print(f"Roll {dice_rolls}: Dice = {dice}, Move = {move}, Position = {position}")

    print(f"Game over! you won in {dice_rolls} rolls.")

play_snake_and_ladder()