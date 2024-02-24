import pandas as pd 
import numpy as np
import src.hangman as hangman
import src.tictactoe as tictactoe
import os

if __name__=="__main__":
    # print('hello world')
    
    while True:
        game = input('Please select a game to play: hangman [H] or tictactoe [T]:')
        if game == 'H':
            script_dir = os.path.dirname(__file__)
            rel_path = 'data/words.txt'
            file_path = os.path.join(script_dir, rel_path)
            hangman.main_hangman(file_path)
            break
        elif game == 'T':
            tictactoe.printboard()
            tictactoe.main_tictactoe()
            break
        else:
            print('Wrong input')