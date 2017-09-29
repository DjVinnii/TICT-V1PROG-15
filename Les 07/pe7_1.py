som = 0
teller = 0

while True:
    getal = eval(input('Voer een getal in: '))
    if getal == 0:
        break
    som = som + getal
    teller = teller + 1

print('Er zijn ' + str(teller) + ' getallen in gevoerd, de som is ' + str(som))