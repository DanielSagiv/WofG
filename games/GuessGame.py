import random
  
def generate_number(Difficulty):
    _difficulty=5*Difficulty
    return random.randint(1, _difficulty)
    
def get_guess_from_user():
    guess = int(input("Enter your guess: "))
    return guess
def compare_results(generated, guess):
    if generated==guess:
        print ("Nicceeee")
    else:
        print ("go python yourself")
        