# ShoPETfy 🐶

ShoPETfy is a one stop solution for dog owners. Learn more about your dog, products for them and the best platform to get those products. 
<br><br>
In addition to displaying stats about dogs, our application searches for the best products across Chewy.com, PetSmart.com and Amazon.com.

## Team Members
- Deborah Chan (dchan3)
- Shiyu He (shiyuhe)
- Tianyi Liao (tliao2)
- Xiaotong Yang (xiaoton3)

## Installation and Running
1. Install requirements using `pip3 install -r requirements.txt`
2. Run `python3 shopefy.py`

## Directory Layout
- Main program files are in the root directory. (The main program file is `shopetfy.py`)
- `data` contains all data for this application. 


## Functions
### Function 1 - Get dog information
The purpose of this function is to help dog owner find out more about their dog. 

Under this function, there are 2 options:
1.  Get information based on dog size
    - Select a dog size (S/M/L) to retrieve information about them. 
2.  Get information about your dog
    - Type in a dog breed to find information about them. 

<br>

### Function 2 - Find prices and discount info for chosen category
The purpose of this function is to display lowest product information for the chosen cateogry, it also displays a price comparison by the 3 channels (Chewy, Amazon, Petsmart).

There are 2 pet category options:
1. Pet Toys
2. Pet Treats

<br>

### Function 3 - Product recommender (based on pet size)
The purpose of this function is to give customer a list of products which fits their pets size; display the wordcloud of the most popular brands, based on reviews or price; display the top 20 products' summary based on pets size.

There are 3 pet size options:
1. S
2. M
3. L

There are 3 function options:
1. 'recommend by reviews',
2. 'recommend by price',
3. 'price distribution summary'


<br>

### Function 4 - Product statistics (based on holiday category)
The purpose of this function is to help dog owners find the designated products for certain holiday or their dog's birthday! 
The function will display the prices distribution and the amount of products in both categories for the holiday chosen, it will also offer the customer
the lowest price and the channel to buy it.

Under this function, there are 4 options:
1. Halloween
2. Christmas
3. Easter
4. Birthday

<br>

### Function 5 - Live pull of Chewy data
The purpose of this function is to conduct a live pull of product information from Chewy. The user can input a search word, and this function will display the cheapest 10 products associated with the keyword.
