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
    # stop with key combination 'cmd+d' ('ctrl+d' if ran in terminal)
    word = ''
    running = True
    user_words = []
    while running:
        try:
            print('Введіть слово: ')
            word = input()
        except:
            running = False

        if not word:
            break

        try:
            if user_words.index(word) >= 0:
                continue
        except:
            user_words.append(word)

    return user_words


def check_user_words(user_words, language_part, letters, dict_of_words):
    """
    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    correct_by_letters, missed_words, correct_words = [], [], []
    for user_word in user_words:
        user_word = user_word.lower()
        if user_word[0] in ''.join(letters):
            correct_by_letters.append(user_word)

    for word in dict_of_words:
        if word[1] != language_part:
            continue
        try:
            if correct_by_letters.index(word[0]) >= 0:
                correct_words.append(word[0])
        except:
            missed_words.append(word[0])

    return correct_words, missed_words


def results():
    board = generate_grid()
    language_class = language_classes()
    with open('result.txt', 'w') as file:
        print(board)
        file.write(str(board) + '\n')
        print(language_class)
        file.write(language_class + '\n')
        user_words = get_user_words()
        checker = check_user_words(user_words, language_class, board, get_words('base.lst', board))
        print(len(checker[0]))
        file.write(str(len(checker[0])) + '\n')
        possible_words = [i[0] for i in get_words('base.lst', board) if i[1] == language_class]
        print(possible_words)
        file.write(str(possible_words) + '\n')
        print(checker[1])
        file.write(str(checker[1]))
