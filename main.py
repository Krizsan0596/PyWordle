from time import sleep
from colorama import init, Fore, Back, Style
import requests
import random


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

def main():             #Add guess limit? Maybe
    while True:
        difficulty = int(input("How long should the word be? (3 - 10)\n>"))
        if not(difficulty < 3 or difficulty > 10):
            break
    game(difficulty)
    
word_site = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"  #https://www.mit.edu/~ecprice/wordlist.10000
response = requests.get(word_site)
WORDS = response.content.splitlines()


def game(difficulty:int):
    guess_count = 0
    while True:
        word = random.choice(WORDS).decode("utf-8").lower()
        if len(word) == difficulty:
            break
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

main()