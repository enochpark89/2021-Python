"""
Extracting Indeed pages
1. Get beautiSoup
2. Quickstart section
3. get HTML -> convert to text
4. Use the functionality within the Beautiful soup to get the tags and the data.
Under documentation:
from bs4 import BeutifulSoup
Soup: Data extracter.
soup = BeautifulSoup(html_doc, 'html.parser')

"""
import re
import os
import requests
from bs4 import BeautifulSoup

list = ['1', '2', 'aa1234567aa', 'aaaaa', 'aaa321aa']

"""
# Use the regular expression to return true if there are three digits
def hasNumbers(inputString):
    return bool(re.search(r'\d{3}', inputString))

try:
    print(hasNumbers(list[4]))
except:
    pass

# How to store the index?
items = [8, 23, 45, 12, 78]

for index, item in enumerate(items):
    print(index, item)


list = []

list.append('name', 'date', 'grade')

print(list[0], list[1], list[2])


    # get the index from the country number that user entered from the tds dictionary.
    # Then, use the index to access the lists.
list = tds_list[tds_dict[num]]
print("You chose", list[1])
print("The currency code is", list[2])


sort_tds = dict(sorted(tds.items(), key=lambda kv: kv[0]))

print("Hello! Please choose select a country by number:")
for k, v in sort_tds.items():
    print("#", k, v)

# for td in tds:


while(isinstance(num, str)):
    num = input("Enter number :")
    try:
        num = int(num)
    except:
        print("put the number")

is_found = False

while(is_found == False):
    for td_list in tds_list:
        if td_list[0] == num:
            is_Found = True
            print("You chose", list[2])
            print("The currency code is", list[3])
    if(is_found == False):
        print("Please Choose a number from the list")


print(num)
print(complexfunction(int(num), int(num)))


"""


def complexfunction(a, b):
    if (isinstance(a, int)):
        sum = a + b
        return sum


def isTrue(num):
    return (isinstance(num, str))


num = "string"
print(isTrue(num))
