try:
    bedrag = 4356
    personen = eval(input('Hoeveel personen gaan er mee op reis? '))
    if personen < 0:
        print('NEgeatieve getallen zijn niet toegestaan!')
    else:
        print(bedrag / personen)
except ZeroDivisionError:
    print('Delen door 0 kan niet!')
except NameError:
    print('Gebruik cijfers voor het invoeren van het aantal!')
except:
    print('Onjuiste invoer!')
