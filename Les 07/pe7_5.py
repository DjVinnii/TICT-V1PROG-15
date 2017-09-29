def namen():
    klas = {}
    while True:
        naam = input('Volgende naam: ')
        if naam == '':
            break
        else:
            if naam in klas.keys():
                klas[naam] += 1
            else:
                klas[naam] = 1
    for k, v in klas.items():
        if v == 1:
            print('Er is ' + str(v) + ' student met de naam ' + k)
        else:
            print('Er zijn ' + str(v) + ' studenten met de naam ' + k)

namen()