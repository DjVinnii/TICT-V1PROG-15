def gemiddelde():
    woordcount = 0
    lettercount = 0
    zin = input('Voer een zin in: ')
    zin = zin.split()
    for woord in zin:
        woordcount = woordcount + 1
        lettercount = lettercount + len(woord)
    gem = lettercount / woordcount
    return gem
print(gemiddelde())