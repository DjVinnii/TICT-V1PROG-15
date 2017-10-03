def seizoen(maand):
    if maand < 1 or maand > 12:
        return('FOUT! Dit is geen geldig maand nummer.')
    if maand >=3 and maand <= 5:
       return('lente')
    if maand >=6 and maand <= 8:
        return('zomer')
    if maand >=9 and maand <= 11:
        return('herfst')
    else:
        return('winter')

maand = eval(input('Geeft een maand nummer: '))
print('Tijdens maand {} is het {}'.format(maand,seizoen(maand)))