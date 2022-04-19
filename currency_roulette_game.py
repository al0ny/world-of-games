import requests
import urllib3
import random
import json
import numpy as np

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
api_key = "47fc2060-92a0-11ec-a7ae-75dd9f87b434"


def get_money_interval(d):
    try:
        d = float(d)  # converting difficulty to float type
        random_number = random.randint(1, 100)
        r = requests.get(url="https://freecurrencyapi.net/api/v2/latest?apikey="+api_key, verify=False)
        usd_ils = float(json.loads(r.text)['data']['ILS'])
        t = random_number * usd_ils  # The value of USDs amount I have in ILS
        interval = np.arange(t - (float(5) - d), t + (float(5) - d))
        # returns the amount of USDs and their range value.
        return interval, random_number
    except Exception as e:
        print(e)


def get_guess_from_user(n):
    # prompt a guess from the user to enter a guess of value to a given amount of USD
    while True:
        try:
            guess = float(input(f"Guess an estimated value of {n} USDs in ILS: \n"))  # Verify & converts input to float
            return guess
        except ValueError:
            print(f"Invalid Option, please enter the value of USD in ILS: \n")
            continue


def play(difficulty):
    try:
        value_range, amount = get_money_interval(difficulty)
        guess = get_guess_from_user(amount)
        if value_range[0] <= guess <= value_range[-1]:
            print("You Won! your guess is in the acceptable range")
            return True
        else:
            print("Try harder next time...")
            return False
    except Exception as e:
        print(e)


