from typing import List
import random


def generate_grid() -> List[str]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. ["а", "і", "с", "х", "д"]
    """
    board = []
    ukrainian_alphabet = [i for i in 'ґйцукенгшщзхїфівапролджєячсмитьбю']
    while len(board) != 5:
        char = random.choice(ukrainian_alphabet)
        if char not in board:
            board.append(char)

    return board


def language_classes() -> str:
    """
    Generates certain language class
    """
    part = random.choice(['Дієслово', "Іменник", "Прислівник", "Прикметник"])
    return part


def get_words(f: str, letters: List[str]) -> List[tuple]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    possible_words = []
    with open(f, 'r') as file:
        file = file.read().split('\n')
        for row in file:
            if len(row) < 1 or len(row.split()[0]) > 5 or\
               row.split()[0][0] not in ''.join(letters) or\
               'intj' in row or 'noninfl' in row:
                continue
            if 'noun' in row or '/n' in row:
                possible_words.append((row.split()[0], "Іменник"))

            if 'verb' in row or '/v' in row:
                possible_words.append((row.split()[0], 'Дієслово'))

            if len(row.split()) == 2 and row.split()[1] == 'adv':
                possible_words.append((row.split()[0], "Прислівник"))

            if len(row.split()) == 2 and row.split()[1] == '/adj':
                possible_words.append((row.split()[0], "Прикметник"))

    return possible_words


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    pass


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    pass
