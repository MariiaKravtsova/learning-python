import wikiquote
import random
import sys
import json

def read_quotes():
    with open('quotes.json') as data_file:
    data_loaded = json.load(data_file)

def write_quotes(author, quote):


def quote_today():
    inspiration = wikiquote.quote_of_the_day()
    quote = inspiration[0].split('\n')
    for each in quote:
        print(each)
    print('\n', 'Author:', inspiration[1])


def random_quote():
    quote = urllib.request.urlopen("https://favqs.com/api/qotd").read()
    print(quote)


if sys.argv[1] == 'day':
    quote_today()
elif sys.argv[1] == 'random':
    random_quote()
