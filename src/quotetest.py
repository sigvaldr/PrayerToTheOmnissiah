import random
def loadQuotes():
    with open('assets/quotes.txt') as file:
        q = file.readlines()
        return q

def Quote():
    quotes = loadQuotes()
    return quotes[random.randint(0,len(quotes)-1)]

if __name__ == '__main__':
    print("+--------------------------------------------------------------------------------------------------+")
    print()
    print(Quote())
    print("+--------------------------------------------------------------------------------------------------+")
