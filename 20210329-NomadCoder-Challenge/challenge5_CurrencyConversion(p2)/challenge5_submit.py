import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""


IbanURL = "https://www.iban.com/currency-codes"

countries = []

request = requests.get(IbanURL)
soup = BeautifulSoup(request.text, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")[1:]

for row in rows:
    items = row.find_all("td")
    name = items[0].text
    code = items[2].text
    if name and code:
        if name != "No universal currency":
            country = {
                'name': name.capitalize(),
                'code': code
            }
            countries.append(country)


# List where two currency is stored.
two_country_currency = []
howMany = []


def askHowMany():
    try:
        print(
            f"\nHow many {two_country_currency[0]} do you want to convert to  {two_country_currency[1]}:")
        howMany.append(int(input("")))

    except ValueError:
        print("That wasn't a number.")
        askHowMany()


def askAnother():
    try:
        choice = int(input("#: "))
        if choice > len(countries):
            print("Choose a number from the list.")
            askAnother()
        else:
            country = countries[choice]
            print(
                f"You chose {country['name']}")
            two_country_currency.append(country['code'])
            askHowMany()

    except ValueError:
        print("That wasn't a number.")
        askAnother()


def ask():
    try:
        choice = int(input("#: "))
        if choice > len(countries):
            print("Choose a number from the list.")
            ask()
        else:
            country = countries[choice]
            print(
                f"You chose {country['name']}")
            two_country_currency.append(country['code'])
            print("\nNow choose another country.")
            askAnother()
    except ValueError:
        print("That wasn't a number.")
        ask()


print("Where are you from? Choose a country by number.")
for index, country in enumerate(countries):
    print(f"#{index} {country['name']}")

ask()

# Set a new URL to get the result page
TransferwiseURL = f"https://transferwise.com/gb/currency-converter/{two_country_currency[0]}-to-{two_country_currency[1]}-rate?amount={howMany[0]}"

countries = []


request2 = requests.get(TransferwiseURL)
soup2 = BeautifulSoup(request2.text, "html.parser")
calculator = soup2.find("div", {"class": "js-Calculator"})
sourcetarget = calculator.find(
    "h3", {"class": "cc__source-to-target"}).find("span", {"class": "text-success"}).string

conversion_rate = float(str(sourcetarget).strip())
converted_value = howMany[0]*conversion_rate
amount1 = format_currency(howMany[0], two_country_currency[0])
amount2 = format_currency(converted_value, two_country_currency[1])

print(
    f"{amount1} in {two_country_currency[0]} is {amount2} in {two_country_currency[1]}")
