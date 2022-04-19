import currency_roulette_game
import guess_game
import memory_game


def welcome(name):
    print(f'Hello {name} and welcome to the World of Games (WoG).')
    print('Here you can find many cool games to play')


def load_game():
    while True:
        try:
            chosen_game = int(input('''Please choose a game to play:\n
            1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n
            2. Guess Game - guess a number and see if you chose like the computer\n
            3. Currency Roulette - try and guess the value of a random amount of USD in ILS:\n'''))
            if not 0 < chosen_game < 4:
                print('Invalid option, please choose a number between 1 to 3')
                continue
            else:
                while True:
                    try:
                        difficulty = int(input('Please choose difficulty from 1 to 5:\n'))
                        if not 0 < difficulty < 6:
                            print('Invalid option, please choose a number between 1 to 5')
                            continue
                        else:
                            if chosen_game == 1:
                                memory_game.play(difficulty)
                                break
                            elif chosen_game == 2:
                                guess_game.play(difficulty)
                                break
                            else:
                                currency_roulette_game.play(difficulty)
                                break
                    except ValueError:
                        print("Invalid option chosen, please enter a number between 1-3.")
                        continue
                break
        except ValueError:
            print("Invalid option chosen, please enter a number between 1-3.")
            continue











