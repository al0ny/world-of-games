import random
from os import system
import time


def generate_sequence(n):
    generated_numbers_list = []
    for num in range(0, n):
        num = random.randint(2, 100)
        generated_numbers_list.append(num)
    return generated_numbers_list


def get_list_from_user(n):
    while True:
        user_list = input(f"Please enter {n} integers to the list, separated by spaces : \n").split()
        if len(user_list) == n:  # verify the list length is n
            try:  # verify the list elements are integers
                for element in user_list:
                    int(element)
                break
            except ValueError:
                print(f"Invalid type entered, use integers only")
                continue
        else:
            print(f"Wrong number of elements, please try again...")
            continue
    return [int(element) for element in user_list]


def is_list_equal(list1, list2):
    list1.sort()
    list2.sort()
    if list1 == list2:
        return "Equal"
    else:
        return "Not Equal"


def play(difficulty):
    gen_list = generate_sequence(difficulty)
    print("Generated List: \n", gen_list)
    time.sleep(0.7)
    system('cls')
    user_list = get_list_from_user(difficulty)
    print(is_list_equal(gen_list, user_list))



