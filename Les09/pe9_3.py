import csv

with open('scores.csv', 'r') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter=';')

    hoogstescore = 0
    for row in reader:
        if int(row[2]) > hoogstescore:
            output = 'De hoogste score is: {} op {} beaald door {}'.format(row[2], row[0], row[1])
    print(output)