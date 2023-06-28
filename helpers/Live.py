import games.GuessGame
import games.MemoryGame
import games.CurrencyRouletteGame


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
    if type(level)!= int:
        print ('invalid selection')
        level = int(input("Enter a game level: "))
    if level>5 or level <1:
        print ('invalid selection , pls select between 1 and 5')
        level = int(input("Enter a game level: "))
        
    if selection==1:
        print ("now playing "+game_a)
        _systen_list=games.MemoryGame.create_list(level)
        print (f"you have to guess {level*2} numbers")
        _user_list=games.MemoryGame.get_list_from_user()
        games.MemoryGame.compare(_user_list,_systen_list)
        
    
    if selection==2:
        print ("now playing "+game_b)
        genererated=games.GuessGame.generate_number(level)
        user_number=games.GuessGame.get_guess_from_user()
        games.GuessGame.compare_results(genererated,user_number)
        
    if selection==3:
        print ("now playing "+game_c)
        _rand =games.CurrencyRouletteGame.generate_rand()
        print (f"this is in ILS:{_rand} NIS ")
        selection = int(input(f"Your Guess :"))
        _rate=games.CurrencyRouletteGame.get_rate(_rand)
        _interval=games.CurrencyRouletteGame.get_money_interval(_rand*_rate,level)
        _systemNumber=_rand*_rate
       
        _userAnswer=selection
        if _userAnswer<_interval[0] and _userAnswer>_interval[1] :
            print (f"WRONG!!! the answer is : {_systemNumber} USD")
        else:
             print (f"nice!!!!")
        
        
        
        
     
        