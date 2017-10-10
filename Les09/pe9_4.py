import csv

with open('producten.csv', 'r') as myCSVFile:
    reader = csv.DictReader(myCSVFile, delimiter=';')

    hoogsteprijs = 0.0
    laagstevoorraad = 9999
    totaalvooraad = 0
    for row in reader:
        totaalvooraad = totaalvooraad + int(row['Voorraad'])
        if float(row['Prijs']) > hoogsteprijs:
            hoogsteprijs = float(row['Prijs'])
            naam = row['Naam']
            prijs = row['Prijs']
        if int(row['Voorraad']) < laagstevoorraad:
            laagstevoorraad = int(row['Voorraad'])
            artnr = row['Artikelnummer']
            voorraad = row['Voorraad']


        output = 'Het duurste artikel is {} en die kost {} Euro.\nEr zijn slechts {} exemplaren in voorraad van het product met nummer {}.\nIn totaal hebben wij {} producten in ons magazijn liggen'.format(naam, prijs, voorraad, artnr, totaalvooraad)
    print(output)

