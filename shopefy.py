'''

Final project for 95-888 Data Focused Python
Group 7

Author:
Andrew ID:
'''
import math as m
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from funct_2 import get_by_category

def display_all():
    print('display all data')

if __name__ == "__main__":
    answer = ''
    df_combine = pd.read_csv("data/clean/df_final.csv")
    while answer != 'Q' and answer != 'q':
        print('''
        Please select from this menu:

        1)  Given a name, display the characteristics, temperament, and other who are in the same breed group (Debbie)
        2)  Display prices and discount info for chosen category (concatenate chewy and amazon, toys and treats) (Connie)
        3)  Based on pet size (small, medium, large), give product recommendation (based on reviews?) (Tianyi)
        4)  Display summary by category, counts, user input keyword (Halloween) as filter (Xiaoting)
        Q)  Quit from this program
        ''')
        answer = input('    Your choice: ').strip()
        if answer == '1':
            print('anser1')
            display_all()
        elif answer == '2':
            print('''
            1) Toys
            2) Treats
            ''')
            answer_2 = input('    Your choice: ').strip()
            # depending on user input, prints correspodnin info
            if answer_2 == '1':
                answer_2 = 'toys'
            elif answer_2 == '2':
                answer_2 = 'treats'
            else: # ask again
                print('\n    Your choice is not valid:', answer_2, '\n')
            get_by_category(df_combine,str(answer_2))
        elif answer == '3':
            print()
            print('ans3')
            print()
        elif answer == '4':
            print()
            print('ans4')
            print()
        elif answer == 'q' or answer == 'Q':
            pass   # the loop will terminate
        else:
            print('\n    Your choice is not valid:', answer, '\n')

            