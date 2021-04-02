import os
import requests

answer = 'y'


def stringCheck(address):
    address = str(address)
    address = address.strip()
    address = address.lower()
    return address


def addressCheck(address):
    if ('.com' not in address):
        return "NoGood"
    elif ('http' not in address):
        address = 'https://'+address
        return address


while answer != 'n':
    print("Welcome to IsItDown.py!")
    print("Please write a URL or URLs you want to check. (seperated by comma) ")
    # take multiple inputs
    addresses = input()

    # send to stringCheck function for each word split by commas.
    addresses = list(map(stringCheck, addresses.split(",")))

    for address in addresses:
        check = addressCheck(address)
        if check == "NoGood":
            print(address, "is not a valid address")
        else:
            address = check
            r = requests.get(address)
            if (r.status_code == requests.codes.ok):
                print(address, "is up!")
            else:
                print(address, "is down!")
    answer = input("Do you want to start over? y/n ")

print("K Bye")
