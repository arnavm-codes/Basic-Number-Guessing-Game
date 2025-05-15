import random
import yaml
import getpass

with open("game_config.yaml", "r") as f:
    config = yaml.safe_load(f)
    
range_min = config['range']['min']
range_max = config['range']['max']    
guesses_allowed = config['guesses']
mode = config['mode']

solved = False

if mode == "single":
    correct_number = random.randint(range_min, range_max)
elif mode == "multi":
    correct_number = int(getpass.getpass("Player2. please enter the numebr to guess: "))
else:
    print("Invalid Config")    
    exit()
    
for i in range(guesses_allowed):
    guess = int(input("Enter your guess: "))
    
    if guess == correct_number:
        print(f"Correct guess! you needed {i+1} tries") 
        solved = True
        break
    elif guess < correct_number:
        print("Too low")
    elif guess > correct_number:
        print("Too high")      
        
if not solved:
    print(f"You failed! The number was: {correct_number}")          