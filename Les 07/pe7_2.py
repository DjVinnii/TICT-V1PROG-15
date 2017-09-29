while True:
    woord = input('Geef een string van vier letters: ')
    if len(woord) == 4:
        break
    else:
        print(woord + ' woord heeft ' + str(len(woord)) + ' letters')

print('Inlezen van correcte string: ' + woord + ' is geslaagd')
