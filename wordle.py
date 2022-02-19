import os
from random import choice
from enum import Enum
from string import ascii_lowercase
from collections import defaultdict


class Color(Enum):
    DEFAULT = '\033[97m'
    CORRECT = '\033[92m'
    EXISTS = '\033[93m'
    MISS = '\033[90m'


def set_color(color=Color.DEFAULT):
    print(color.value, end='')


def print_board():
    set_color()
    print('\n' * 2)
    print('----------- wordle -----------')
    print()
    print(f'tries left: {tries}')
    print_alphabet()
    print()
    for row in range(6 - tries):
        print_guess(guesses[row])
    for row in range(tries):
        print('_____')


def print_guess(guess):
    used = defaultdict(lambda: 0)
    for n, letter in enumerate(guess):
        if letter == secret_word[n]:
            color = Color.CORRECT
        elif 1 < secret_word.count(letter) >= used[letter]:
            color = Color.EXISTS
        else:
            color = Color.MISS
        used[letter] += 1
        set_color(color)
        print(letter, end='')
    set_color()
    print()


def print_alphabet():
    used_letters = set()
    for w in guesses:
        used_letters.update(iter(w))
    for letter in ascii_lowercase:
        if letter in used_letters and letter in secret_word:
            color = Color.CORRECT
        elif letter in used_letters:
            color = Color.EXISTS
        else:
            color = Color.MISS
        set_color(color)
        print(letter, end='')
    print()
    set_color()


def load_file_to_list(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.strip())
    return lines


os.system('color')
all_words = set(load_file_to_list('wordle-allowed-guesses.txt'))
answers = tuple(load_file_to_list('wordle-answers-alphabetical.txt'))
all_words.update(answers)
quit_to_os = False

while True:
    tries = 6
    guesses = []
    secret_word = choice(answers)
    print_board()
    while tries:
        while True:
            guess = input("Your guess: ")
            if guess.lower() == 'q':
                quit_to_os = True
                break
            elif guess.lower() == 'c':
                print(secret_word)
            elif guess in all_words:
                break
        if quit_to_os:
            break
        guesses.append(guess)
        tries -= 1
        print_board()
        if guess == secret_word:
            break
    if quit_to_os:
        break
    print('Sorry, you lost!' if guess != secret_word else
          f'Congratulations, you won! Number of tries: {6 - tries}')
    if input('type "q" - to quit.\n').lower() == 'q':
        break
