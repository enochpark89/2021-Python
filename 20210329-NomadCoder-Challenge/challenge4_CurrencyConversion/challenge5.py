import os
import requests
from bs4 import BeautifulSoup



# Functions

# Ask the user the put in the country number to query country information

def hasNumbers(inputString):
    return bool(re.search(r'\d{3}', inputString))


os.system("clear")
url = "https://www.iban.com/currency-codes"
iban_result = requests.get(url)

# This basically convert HTML to text.
iban_soup = BeautifulSoup(iban_result.text, "html.parser")

# div - class - pagination
# table - class - table table-bordered downloads tablesorter

table = iban_soup.find(
    "table", {"class": "table table-bordered downloads tablesorter"})
"""
# For some odd reason you have to call 1, 3, 5, 7
print(table.tbody.tr.contents[1])
"""

tds_list = []
trs = table.find_all('tr')
for tr in trs:
    try:
        # get the country_name and country_code
        country_name = str(tr.contents[1])
        currency_code = str(tr.contents[5])
        country_number = str(tr.contents[7])

        # delete the html tags and leave only necessary data.
        country_name = country_name[4:-5]
        currency_code = currency_code[4:-5]
        country_number = country_number[4:-5]

        # Create a list that store a index, country_number, currency_code, country_name, country_number
        list = [int(country_number), country_name, currency_code]
        tds_list.append(list)

    except:
        pass

# Print out the index and country for the user to choose from
for index, td_list in enumerate(tds_list):
    print("#", index, td_list[1])
    # the index becomes the index 0 of the tds_list
    td_list.insert(0, index)


# This loop will force the user to put in the number instead of string
num = "null"
while(isinstance(num, str)):
    num = input("Enter number :")
    try:
        num = int(num)
    except:
        print("Please input a number")

is_found = False

# This check_list will check the list and print the information if found and notify the the data is found. If not found, it will return is_found to be false.


def check_list(num, is_found):

    for item in tds_list:
        if item[0] == num:
            print("You chose", item[2])
            print("The currency code is", item[3])
            is_found = True

    return is_found


# is_found will be true or false after it checked the list
is_found = check_list(num, is_found)

# if is_found is false, it will ask users to put in the number in the list.
while(is_found == False):
    try:
        print("Please Choose a number from the list.")
        num = int(input("Enter number :"))
    except:
        print("Please input a number")
    is_found = check_list(num, is_found)
