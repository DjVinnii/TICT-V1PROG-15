getallenrij = [2, 4, 6, 8, 10, 9, 7]
gevonden = False
zoekgetal =  eval(input("Welk getal wil je zoeken: "))
for getal in getallenrij:
    if getal == zoekgetal:
        gevonden = True
if gevonden == True:
    print(str(zoekgetal) + " heb ik gevonden!")
else:
    print(str(zoekgetal) + " heb ik niet gevonden!")