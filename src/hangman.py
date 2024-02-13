from random import choice
import string
import os

MAX_INCORRECT_GUESSES = 6

def select_word(file_path):
    with open(file_path, mode = '+r') as words:
        word_list = words.readlines()
    return choice(word_list).strip()

def validate_input(player_input, guessed_letters):
    return (
        len(player_input)==1
        and
        player_input >='a'
        and
        player_input <= 'z'
        and
        player_input not in guessed_letters
    )
    
def get_input(guessed_letters):
    while True:
        player_input = input('Guess a letter: ').lower()
        if validate_input(player_input, guessed_letters):
            return player_input
        
def display_guess(target_word, guessed_letters):
    result_str = ''
    for char_tmp in target_word:
        if char_tmp in guessed_letters:
            result_str += char_tmp
        else:
            result_str += '_'
    return result_str

def gameover(wrong_guess, target_word, guessed_letters):
    if wrong_guess == MAX_INCORRECT_GUESSES:
        return True
    if target_word == display_guess(target_word, guessed_letters):
        return True
    return False

def gamewin(target_word, guessed_letters):
    return target_word == display_guess(target_word, guessed_letters)
    

def main_hangman(file_path):
    target_word = select_word(file_path)
    wrong_guess = 0
    guessed_letters = set()
    
    while not gameover(wrong_guess, target_word, guessed_letters):
        draw_hangman(wrong_guess)
        print(f"Current guessed letters: {display_guess(target_word, guessed_letters)}\n")
        
        player_guess = get_input(guessed_letters)
        if player_guess in target_word:
            guessed_letters.add(player_guess)
        else:
            print('Sorry, wrong guess')
            wrong_guess+=1
    
    print('\n**********************************************************************************')
    print(f"Current guessed letters: {display_guess(target_word, guessed_letters)}")
    if (gamewin(target_word, guessed_letters)):
        print('Great, you won!')
    else:
        print(f'Sorry, you lost. The target word is {target_word}')
    print('\n**********************************************************************************')
    
def draw_hangman(wrong_guesses):
    hanged_man = [
        r"""
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
  |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/     |
|     |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
""",
    ]

    print(hanged_man[wrong_guesses])
    
        


if __name__=='__main__':
    script_dir = os.path.dirname(__file__)
    rel_path = '../data/words.txt'
    file_path = os.path.join(script_dir, rel_path)
    # abs_file_path = os.path.abspath(os.path.realpath(file_path))
    # print(select_word(file_path))
    
    # guessed_letters = {'a', 'g', 'o'}
    # print(validate_input('?', guessed_letters))
    # print(validate_input('B', guessed_letters))
    # print(validate_input('g', guessed_letters))
    # print(validate_input('p', guessed_letters))
    
    # # print(get_input(guessed_letters))
    
    # print(display_guess('apple', {'p'}))
    # print(display_guess('banana', {'b', 'a'}))
    
    # print('a' in 'apple')
    
    # draw_hangman(4)
    
    
    # print(gameover(6, 'banana', {'a'}))
    # print(gameover(5, 'banana', {'a'}))
    # print(gameover(1, 'banana', {'a', 'b', 'n'}))
    
    main_hangman(file_path)
        
    