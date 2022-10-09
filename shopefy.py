'''
Final project for 95-888 Data Focused Python
Group 7

Date: 10/9/22
Authors: Deborah Chan, Shiyu He, Tianyi Liao, Xiaotong Yang
Andrew ID: dchan3, shiyuhe, tliao2, xiaoton3
'''

# Import modules
import math as m
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
from funct_1 import *
from funct_2 import *
from funct_3 import *
from funct_4 import *
from funct_5 import *
from data.chewy.chewy_crawl import chewy_search
import warnings
warnings.filterwarnings('ignore')

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
1)  Get dog information
2)  [Historic] Display prices and discount info for chosen category
3)  [Historic] Product recommender based on pet size (small, medium, large)
4)  [Historic] Display product statistics by category, prices, counts based on holiday category
5)  [Live Pull] Keyword match on Chewy and sort by prices
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
'1': 'Get information based on dog size',
'2': 'Get information about your dog',
}

function_1_1 = {
'1': 'Small',
'2': 'Medium',
'3': 'Large'
}

### Function 2 Options ###
function_2 = {
'1': 'Toys',
'2': 'Treats',
}

### Function 3 Options ###
function_3_1 = {
'1': 'S',
'2': 'M',
'3': 'L'
}

function_3_2 = {
'1': 'recommend by reviews',
'2': 'recommend by price',
'3': 'price distribution summary'
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
                print("What dog size are you looking at?")
                display_options(function_1_1)
                answer_1_1 = get_input()

                if answer_1_1 in function_1_1.keys():
                    get_stats_by_size(function_1_1)
                else:
                    print('\nYour choice is not valid:', answer, '\n')

            # Function 1, Option 2
            elif answer_1 == '2':
                print("What breed of dog do you have?")
                answer_1_2 = get_input().lower()

                if is_valid_breed(answer_1_2):
                    print(tabulate(get_stats_by_breed(answer_1_2), headers = 'keys', tablefmt='psql', showindex=False))
                    print()
                else:
                    print("Sorry, we don't have information for that breed yet.\n")

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
            print('\nPlease choose your dog size')
            display_options(function_3_1)
            answer_3_size = get_input()
            print('\nPlease choose the method')
            display_options(function_3_2)
            answer_3_choice = get_input()
            if answer_3_size in function_3_1.keys():
                if (answer_3_choice in function_3_2.keys() and answer_3_choice != '3'):
                    recommand_by(get_by_size(df_combine, function_3_1[answer_3_choice]), answer_3_choice)
                    continue
                elif (answer_3_choice in function_3_2.keys() and answer_3_choice == '3'):
                    summary_by_size(get_by_size(df_combine, function_3_1[answer_3_size]))
                    continue
                else: # invalid option
                    print('\nYour choice is not valid:', answer_3_choice, '\n')
            else: # invalid option
                print('\nYour choice is not valid:', answer_3_size, '\n')

        ##### Function 4 #####
        elif answer == '4':
            display_options(function_4)
            answer_4 = get_input()
            if answer_4 in function_4.keys():
                #create the subdataframe which contains the keyword
                df_subset = fil_keyword(df_combine,function_4[answer_4])
                #price distribution in both categories
                draw(df_subset)
                #display the amount of products in both categories
                amount_cate(df_subset)
                print()
                print("Choose the category you want:")
                #choose a category
                display_options(function_2)
                answer_4_2 = get_input()
                # display the lowest price of this category and its channel
                print()
                lowest_cate(df_subset,function_2[answer_4_2].lower())
                #continue
                print()
            else: # invalid option
                print('\nYour choice is not valid:', answer_4, '\n')

        ##### Function 5 #####
        elif answer == '5':
            print('\nSearch for word on Chewy: ')
            #get user input
            answer_5_1 = get_input()
            print('\n\t[INFO] Searching for the term ' + answer_5_1 + '...')
            #search for the word using web scraping
            chewy_search(answer_5_1)
            print('\n\t[INFO] Search is finished')
            #reads the searched saved data
            chewy_search_df = pd.read_csv('data/chewy/chewy_search_term.csv')
            if chewy_search_df.shape[0] < 1:
                print('\n\t[INFO] Unable to find any results, refer to options 2-5 for saved scraped results')
            else:
                #cleans the searched data 
                results_df = clean_df(chewy_search_df)
                print('\n\t[INFO] Display cheapst 10 products on Chewy:')
                print(tabulate(sort_by_price(results_df), headers = 'keys', tablefmt='psql'))
            print()

        elif answer == 'q' or answer == 'Q':
            pass # while loop will terminate

        ##### Invalid Input #####
        else:
            print('\nYour choice is not valid:', answer, '\n')
