import random
import time

def create_list(level):
    deificulty=level*2
    res =[random.randint(1, 101) for _ in range(deificulty)]
    print(res)
    time.sleep(0.7)
    # Clear 
    print('\033[H\033[J')
    return res
    
def get_list_from_user():
    user_list = input("Enter a list of numbers, separated by spaces: ")
    return  [int(num) for num in user_list.split()]
   
def compare(user_list,system_list):
    if set(user_list) == set(system_list):  
        print("good guess!!!")
    else:
        print("go python yourself")