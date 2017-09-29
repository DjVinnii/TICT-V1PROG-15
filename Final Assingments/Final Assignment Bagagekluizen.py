def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt', 'r')
    kluizen = 12 -len(infile.readlines())
    infile.close()
    return kluizen

def nieuwe_kluis():
    list = [1,2,3,4,5,6,7,8,9,10,11,12]
    infile = open('kluizen.txt', 'r')
    kluizen = infile.readlines()
    for kluis in kluizen:
        kluisinfo = kluis.split(';')
        list.remove(int(kluisinfo[0]))

    if len(list) == 0:
        print('Er zijn geen kluizen beschikbaar.')
    else:
        kluisnummer = list[0]
        print('Uw kluisnummer is {}'.format(kluisnummer))
        wachtwoord = input('Voer het gewenste wachtwoord in: ')
        outfile = open('kluizen.txt', 'a')
        outfile.write('\n' + str(kluisnummer) +  ';' + wachtwoord)
        outfile.close()
        print('Uw kluis is nu klaar voor gebruik.')

def kluis_openen():
    kluisnummer = eval(input('Voer uw kluisnummer in:'))
    wachtwoord = input('Voer uw wachtwoord in:')
    code = str(kluisnummer) + ';' + wachtwoord
    infile = open('kluizen.txt', 'r')
    regels = infile.readlines()
    for regel in regels:
        regel = regel.strip()
        if regel == code:
            print('Uw kluis is geopend')
            infile.close()
            return
    print('Onjuiste combinatie!')
    infile.close()

def kluis_teruggeven():
    kluisnummer = eval(input('Voer uw kluisnummer in:'))
    wachtwoord = input('Voer uw wachtwoord in:')
    code = str(kluisnummer) + ';' + wachtwoord
    file = open('kluizen.txt', 'r')
    lines = file.readlines()
    file.close()
    outfile = open('kluizen.txt', 'w')
    for line in lines:
        line = line.strip()
        if line == code:
            for line in lines:
                line = line.strip()
                if line != code:
                    outfile.write(line + '\n')
                elif line == code:
                    print('Uw kluis is nu terug gegeven.')
                    outfile.close()
                    return
    print('Onjuiste combinatie!')
    outfile.close()

while True:
    #Startmenu
    print('1: Ik wil weten hoeveel kluizen nog vrij zijn\n2: Ik wil een nieuwe kluis\n3: Ik wil even iets uit mijn kluis halen\n4: Ik geef mijn kluis terug\n5: Ik wil stoppen')

    #Keuze
    keuze = eval(input('Maak uw keuze: '))
    if keuze == 1:
        #Lege kluizen
        print('Er zijn nog {} kluizen beschikbaar.'.format(toon_aantal_kluizen_vrij()))
    elif keuze == 2:
        #Nieuwe kluis
        nieuwe_kluis()
    elif keuze == 3:
        #Kluis openen
        kluis_openen()
    elif keuze == 4:
        #Kluis terug
        kluis_teruggeven()
    elif keuze == 5:
        #Stop while loop
        break
    else:
        #Foute input
        print('FOUT! Dit is een ongeldige keuze.')