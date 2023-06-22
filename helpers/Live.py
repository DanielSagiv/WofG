def welcome(name):
    print (f'hello {name} and welcome to the World of Games (WoG).Here you can find many cool games to play.')
    
def load_game():
    game_a='Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back'
    game_b='Guess Game - guess a number and see if you chose like the computer'
    game_c='Currency Roulette - try and guess the value of a random amount of USD in ILS'
    
    print('Please choose a game to play:')
    print(f'1.{game_a}')
    print(f'2.{game_b}')
    print(f'3.{game_c}')
    selection = int(input("Enter a game number: "))
    if selection==1:
        print(f'you choose : {game_a}')
    if selection==2:
        print(f'you choose : {game_b}')
    if selection==3:
        print(f'you choose : {game_c}')
    
    
    print ('Please choose game difficulty from 1 to 5:')
    level = int(input("Enter a game level: "))
    if level(type)!= int:
        print ('invalid selection')
        level = int(input("Enter a game level: "))
    if level>5 or level <1:
        print ('invalid selection , pls select between 1 and 5')
        level = int(input("Enter a game level: "))
        