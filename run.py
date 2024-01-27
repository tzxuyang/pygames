import pandas as pd 
import numpy as np
import src.hangman as hangman
import os

if __name__=="__main__":
    print('hello world')
    script_dir = os.path.dirname(__file__)
    rel_path = 'data/words.txt'
    file_path = os.path.join(script_dir, rel_path)
    
    hangman.main_hangman(file_path)