import requests
import random

def get_rate(amount):
    me_key = "f000f24acb9240bda5a3467ae7233bcd"  
    amount_usd = amount  
    response = requests.get(f"https://openexchangerates.org/api/latest.json?app_id={me_key}")
    data = response.json()
    conv_rate = data["rates"]["ILS"]
    return conv_rate
    
def generate_rand():
    rand_number = random.randint(1, 100)
    return rand_number

def get_money_interval(total, difficulty ):
    _interval=(total - (5 - difficulty), total +(5 - difficulty))
    return _interval



