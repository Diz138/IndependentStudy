import re


def emails_reader(filepath= "emailTest.txt"):
    with open(filepath, "r") as file:
        data = file.read()

    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", data)
    print (emails)

def url_reader(filepath= "urlTest.txt"):
    with open(filepath, "r") as file:
        data = file.read()

    url = re.findall(r'[a-z0-9\.\-+_]+\.[a-z0-9\.\-+_]+', data)
    print (url)
#include backlash and period and more
