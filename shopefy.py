'''
Final project for 95-888 Data Focused Python
Group 7

Authors: Deborah Chan, Shiyu He, Tianyi Liao, Xiaotong Yang
Andrew ID: dchan3, xiaoton3# todo: add andrew id
'''

# Import modules
import math as m
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
from funct_1 import *
from funct_2 import get_by_category, display_graph
from funct_4 import *

########## define options ##########
# Welcome Banner
welcome ='''
  ______ _           ______ _______ _______ ___       
 / _____) |         (_____ (_______|_______) __)      
( (____ | |__   ___  _____) )____      _ _| |__ _   _ 
 \____ \|  _ \ / _ \|  ____/  ___)    | (_   __) | | |
 _____) ) | | | |_| | |    | |_____   | | | |  | |_| |
(______/|_| |_|\___/|_|    |_______)  |_| |_|   \__  |
                                               (____/ 
'''
def display_welcome():
    print(welcome)

# Main Menu
main_menu = '''Please select from this menu:
1)  Given a name, display the characteristics, temperament, and other who are in the same breed group (Debbie)
2)  Display prices and discount info for chosen category (concatenate chewy and amazon, toys and treats) (Connie)
3)  Based on pet size (small, medium, large), give product recommendation (based on reviews?) (Tianyi)
4)  Display summary by category, counts, user input keyword (Halloween) as filter (Xiaotong)
Q)  Quit from this program'''

def display_main_menu():
    print(main_menu)

# Function to get user input
def get_input():
    print()
    answer = input('Your choice: ').strip()
    return answer

### Function 1 Options ###
function_1 = {
'1': 'Information for all dogs',
'2': 'Information for your dog',
}

function_1_1 = {
'1': 'Height',
'2': 'Weight',
'3': 'Life Span'
}

### Function 2 Options ###
function_2 = {
'1': 'Toys',
'2': 'Treats',
}

### Function 3 Options ###
function_3 = {
}

### Function 4 Options ###
function_4 = {
'1': 'Halloween',
'2': 'Christmas',
'3': 'Easter',
'4': 'Birthday'
}

# Function to display options
def display_options(function):
    print()
    [print('{}) {}'.format(k,v)) for k,v in function.items()]



########## Main Program ##########
if __name__ == "__main__":
    answer = ''
    display_welcome()

    df_combine = pd.read_csv("data/clean/df_final.csv")

    while answer != 'Q' and answer != 'q':
        ##### Print Main Menu #####
        display_main_menu()
        answer = get_input()

        ##### Function 1 #####
        if answer == '1':
            display_options(function_1)
            answer_1 = get_input()

            # Function 1, Option 1
            if answer_1 == '1':
                display_options(function_1_1)
                answer_1_1 = get_input()

                if answer_1_1 in function_1_1.keys():
                    pass
                else:
                    print('\nYour choice is not valid:', answer, '\n')

            # Function 1, Option 2
            elif answer_1 == '2':
                print('''
                What breed of dog do you have?
                Input breed: 
                ''')
                answer_1_2 = get_input()

            else:
                print('\nYour choice is not valid:', answer_1, '\n')


        ##### Function 2 #####
        elif answer == '2':
            display_options(function_2)
            answer_2 = get_input()

            if answer_2 in function_2.keys():
                df_result = get_by_category(df_combine,function_2[answer_2].lower())
                print()

                # displays top 10 cheapst product, sort by price
                print(tabulate(df_result.head(10), headers = 'keys', tablefmt='psql'))

                # plot cheapest product by each channel
                display_graph(df_result)
                print()

            else: # invalid option
                print('\nYour choice is not valid:', answer_2, '\n')


        ##### Function 3 #####
        elif answer == '3':
            display_options(function_3)
            answer_3 = get_input()

            if answer_3 in function_3.keys():
                # do something
                continue

            else: # invalid option
                print('\nYour choice is not valid:', answer_3, '\n')

        ##### Function 4 #####
        elif answer == '4':
            display_options(function_4)
            answer_4 = get_input()

            if answer_4 in function_4.keys():
                # do something
                df_subset = fil_keyword(df_combine,function_4[answer_4])
                #price distribution in both categories
                #draw(df_subset)
                amount_cate(df_subset)
                print("Choose the category you want:")
                #choose a category
                display_options(function_2)
                answer_4_2 = get_input()
                # display the lowest price of this category and its channel
                lowest_cate(df_subset,function_2[answer_4_2].lower())
                #continue

            else: # invalid option
                print('\nYour choice is not valid:', answer_4, '\n')


        elif answer == 'q' or answer == 'Q':
            pass # while loop will terminate

        ##### Invalid Input #####
        else:
            print('\nYour choice is not valid:', answer, '\n')