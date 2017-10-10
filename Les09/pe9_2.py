import datetime
import csv

bestand = 'inloggers.csv'

with open(bestand, 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(('tijd', 'voorletters', 'naam', 'geboortedatum', 'email'))
    while True:
        naam = input("Wat is je achternaam? ")
        if naam == 'einde':
            break
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        tijd = datetime.date.today()
        writer.writerow((tijd.ctime(), voorl, naam, gbdatum, email))

