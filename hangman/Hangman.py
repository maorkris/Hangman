from colorama import Fore, Back, Style, init
from photo import *
import random

def print_welcome():
    """
    This function prints the opening screen of the game
    :return: None
    """

    MAX_TRIES = 6
    print(Fore.LIGHTBLUE_EX , HANGMAN_GAME_LOGO ,Fore.RESET )
    print("Welcome to the game Hangman")

    print(f"You have{Fore.CYAN} {MAX_TRIES}{Fore.RESET} tries")


def print_hangman(num_of_tries):
    """
    This function prints all situations of the hangman
    :return: None
    """
    HANGMAN_PHOTOS = {0:pic1, 1:pic2, 2:pic3, 3:pic4, 4:pic5, 5:pic6, 6:pic7}

    print(HANGMAN_PHOTOS[num_of_tries])


def guess_a_letter ():
    """
    This function prompts the user to guess a letter
    :return: The guessed letter if it's valid, otherwise it will prompt again
    """
    print()
    hebrew_letters = ['א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'כ', 'ל', 'מ', 'נ', 'ס', 'ע', 'פ', 'צ', 'ק','ר', 'ש', 'ת']
    get_one_letter = input("Guess a letter:")
    while get_one_letter.isalpha() and len(get_one_letter) == 1 and get_one_letter not in hebrew_letters:
        return get_one_letter.lower()
    else:
        print("Error, please enter only one English letter")
        return guess_a_letter()



def check_valid_input(letter_guessed, old_letters_guessed):
    """
    This function checks if the guessed letter is valid
    :param letter_guessed: The guessed letter
    :param old_letters_guessed: A list of letters that have been guessed before
    :return: True if the guessed letter is valid, False otherwise
    """

    if len(letter_guessed) > 1 and letter_guessed.isalpha():
        return False
    elif len(letter_guessed) == 1 and not letter_guessed.isalpha():
        return False
    elif len(letter_guessed) > 1 and not letter_guessed.isalpha():
        return False
    elif letter_guessed.lower()in old_letters_guessed:
        return False
    else:
        return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed,secret_word):
    """
    This function tries to update the list of guessed letters
    :param letter_guessed: The guessed letter
    :param old_letters_guessed: A list of letters that have been guessed before
    :param secret_word: The word that the user is trying to guess
    :return: True if the guessed letter is in the secret word, False otherwise
    """
    joined_sorted_old_letters = " -> ".join(sorted(old_letters_guessed))
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        print(f"Letter '{letter_guessed}' added to guessed letters: {Fore.LIGHTYELLOW_EX +joined_sorted_old_letters + Style.RESET_ALL} ")
        if letter_guessed not in secret_word:
            return True
    else:
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT,X,"Wrong answer",Fore.RESET)
        return False



def show_hidden_word(secret_word, old_letters_guessed):
    """
    This function shows the current state of the secret word, with guessed letters revealed and unguessed letters hidden
    :param secret_word: The word that the user is trying to guess
    :param old_letters_guessed: A list of letters that have been guessed before
    :return: A string representing the current state of the secret word
    """

    result = ""
    for i in secret_word:
        if i == " ":
            continue
        if i in old_letters_guessed:
            result += (i + " ")
        else:
            result += "_ " + " "
    return Fore.LIGHTGREEN_EX + 'The secret Word :\n' + result + Fore.RESET

def check_win(secret_word, old_letters_guessed):
    """
    This function checks if the user has won the game
    :param secret_word: The word that the user is trying to guess
    :param old_letters_guessed: A list of letters that have been guessed before
    :return: True if the user has won the game, False otherwise
    """
    for i in secret_word:
        if i not in old_letters_guessed:
            return False
    return True

def choose_word(file_path, index):
    """
    This function chooses a word from a file
    :param file_path: The path to the file
    :param index: The index of the word to choose
    :return: The chosen word
    """
    words_arr = []
    with open(file_path) as file:
        words = file.read().split(",")
        for i in words:
            if i not in words_arr:
                words_arr.append(i)

        index = index % len(words)
        return words[index -1]


def main():


    """
    This is the main function of the game
    :return: None
    """
    Animal = 'Animal.txt'
    countries = 'countries.txt'
    names = 'names.txt'


    print_welcome()
    choice = input("please choose a category: \n 1. Animals \n 2. names \n 3. Countries \n")
    match choice:
        case "1":
            file_from_user = Animal
        case "2":
            file_from_user = names
        case "3":
            file_from_user = countries
        case _:
            file_from_user = Animal

    secret_word = choose_word(file_from_user, random.randint(1, 100))
    old_letters_guessed = []
    MAX_TRIES = 7
    num_of_tries = 1
    print_hangman(0)
    while MAX_TRIES > num_of_tries and not check_win(secret_word,old_letters_guessed):
        if num_of_tries == MAX_TRIES:
            if check_win(secret_word, old_letters_guessed):
                print(f" The secret Word is : {secret_word.upper()}")
                return WIN_MESSAGE
            else:
                print(f" The secret Word is : {secret_word.upper()}")
                return LOSE_MESSAGE

        print(show_hidden_word(secret_word, old_letters_guessed))
        letter_guessed = guess_a_letter()
        if try_update_letter_guessed(letter_guessed,old_letters_guessed,secret_word):
            if letter_guessed not in secret_word:
                print(f"\n{Fore.RED}you have more {(MAX_TRIES - num_of_tries) -1} tries{Fore.RESET} ")
                print_hangman(num_of_tries)
                try_update_letter_guessed(letter_guessed, old_letters_guessed,secret_word)
                num_of_tries += 1

    else:

        if check_win(secret_word,old_letters_guessed):
            print(f"The secret Word is : {secret_word.upper()}")
            return Fore.LIGHTMAGENTA_EX + WIN_MESSAGE + Style.RESET_ALL
        else:
                print()
                return Fore.RED + LOSE_MESSAGE + f"\nThe secret Word was : {secret_word.upper()}{Style.RESET_ALL}"



if __name__ == "__main__":
    print(main())

    pass