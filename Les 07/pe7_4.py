filename = 'tickersymbols.txt'

def ticker(filename):

    tickers = {}

    infile = open(filename, 'r')
    lines = infile.readlines()
    infile.close()

    for line in lines:
        info = line.split(':')
        info[1] = info[1].strip()
        tickers[info[0]] = info[1]

    return tickers

naam = input('Enter Company name: ')
print('Ticker symbol: ' + ticker(filename).get(naam))
