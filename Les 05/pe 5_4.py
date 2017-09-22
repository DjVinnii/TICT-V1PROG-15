def strftime():
    import datetime
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d %b %Y, %H:%M:%S")
    return s

naam = input('Voer de naam van de hardloper in: ')
outfile = open('hardlopers.txt', 'a')
outfile.write(strftime() + ', ' + naam + '\n')
outfile.close()
