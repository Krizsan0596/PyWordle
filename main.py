from time import sleep
from colorama import init, Fore, Back, Style
import requests
import random
import sys


init(autoreset=True)

def get_input(length):
    inp = str(input("\n>")).lower()
    if len(inp) != length:
        print(Fore.RED + "Please enter a {}-letter word.".format(length))
        return get_input(length)
    if inp.__contains__(" "):
        print(Fore.RED + "Please enter a word without spaces.")
        return get_input(length)
    return inp

def main():
    while True:
        difficulty = input("How long should the word be? (" + Fore.RED + "3 - 10" + Fore.WHITE + ")[" + Fore.CYAN +"Q for defaults" + Fore.WHITE +  "]\n>")
        if difficulty.upper() == "D":
            game(5, 0, True)
        elif difficulty.upper() == "Q":
            game(5, 5)
        difficulty = int(difficulty)
        if not(difficulty < 3 or difficulty > 10):
            break
    while True:
        guesses = int(input("How many guesses would you like?(" + Fore.RED +"<15 or 0 for infinite" + Fore.WHITE + ")\n>"))
        if guesses < 15:
            break
    game(difficulty, guesses)
    
word_site = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"  #https://www.mit.edu/~ecprice/wordlist.10000
response = requests.get(word_site)
WORDS = response.content.splitlines()

def game_over(word:str):
    print("\nYou ran out of guesses! Better luck next time!\nYour word was:")
    for i in word:
        print(Fore.RED + i, end='')
        sleep(0.1)
    play_again = input(Fore.CYAN + "\nWould you like to play again? [Y]es/[N]o/[C]hange difficulty\n>" + Fore.WHITE)
    if play_again.upper() == "Y":
        game(len(word))
    elif play_again.upper() == "C":
        main()
    elif play_again.upper() == "N":
        sys.exit()


def game(difficulty:int, guess_limit:int, debug:bool=False):
    guess_count = 0
    while True:
        word = random.choice(WORDS).decode("utf-8").lower()
        if len(word) == difficulty:
            break
    if debug:
        print(word)
    while True:
        guess = get_input(difficulty)
        guess_count += 1
    #    if guess.encode("utf-8") not in WORDS:
    #        print(Fore.RED + "That is not a valid english word.")
    #        continue
    #    print(guess_list)
    #    for letter in guess_list:
    #        if letter not in word_list:
    #            print(Fore.WHITE + letter, end="")
    #            continue
        match = [a==b for a,b in zip(guess, word)]
        if all(match):
            print("\n")
            for char in word:
                print(Fore.GREEN + char, end="")
                sleep(0.1)
            break
        for i, x in enumerate(guess):
            if x in word:
                if match[i]:
                    print(Fore.GREEN + x, end='')
                else:
                    print(Fore.YELLOW + x, end='')
            else:
                print(Fore.WHITE + x, end='')
        if guess_limit != 0:
            if guess_count >= guess_limit:
                game_over(word)
            rem_guess = "\n{} guess{} remaining."
            if guess_limit - guess_count == 1:
                rem_guess = rem_guess.format("1", "")
            else:
                rem_guess = rem_guess.format(guess_limit - guess_count, "es")
            print(rem_guess)

    #print(Fore.GREEN + "\nCongratulations!")
    win_txt = "\nCongratulations!"
    win_txt = list(win_txt)
    for i in win_txt:
        print(Fore.GREEN + i, end='')
        sleep(0.05)
    guess_txt = "You guessed {guess_count} times.".format(guess_count=guess_count)
    if guess_count < 5:
        guess_txt = "Impressive! Only {guess_count} guesses.".format(guess_count=guess_count)
    if guess_count < 3:
        guess_txt = "Amazing! Less than 3 guesses. ({guess_count})".format(guess_count=guess_count)
    if guess_count == 1:
        guess_txt = "Come on! You have got to be cheating!"
    print("\n" + guess_txt)
    play_again = input(Fore.CYAN + "\nWould you like to play again? [Y]es/[N]o/[C]hange difficulty\n>" + Fore.WHITE)
    if play_again.upper() == "Y":
        game(difficulty)
    elif play_again.upper() == "C":
        main()
    elif play_again.upper() == "N":
        sys.exit()

main()