# Jouw functies komen hier!!

stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '\'s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

def inlezen_beginstation(stations):
    beginstation = input('Voer het beginstation van uw reis in: ')
    if beginstation not in stations:
        print('Dit is geen station op het traject Schagen - Maastricht. Probeer het opnieuw.')
        inlezen_beginstation(stations)
    else:
        return beginstation

def inlezen_eindstation(stations, beginstation):
    eindstation = input('Voer het eindstation van uw reis in: ')
    if eindstation not in stations:
        print('Dit is geen station op het traject Schagen - Maastricht. Probeer het opnieuw.')
        inlezen_eindstation(stations, beginstation)
    else:
        if stations.index(eindstation) <= stations.index(beginstation):
            print('Dit station  is eerder op het traject Schagen - Maastricht dan het beginstation. Probeer het opnieuw.')
            inlezen_eindstation(stations, beginstation, eindstation)
        else:
            return eindstation

def omroepen_reis(stations, beginstation, eindstation):
    begin_index = stations.index(beginstation) + 1
    eind_index = stations.index(eindstation) + 1
    x = begin_index

    print('\nHet beginstation {} is het {}e station in het traject.'.format(beginstation, begin_index))
    print('Het eindstation {} is het {}e station in het traject.'.format(eindstation, eind_index))
    print('De afstand bedraagt {} station(s).'.format(eind_index-begin_index))
    print('De prijs van het kaartje is {} euro.\n'.format((eind_index-begin_index)*5))
    print('Jij stapt in de trein in: {}'.format(beginstation))
    while x < eind_index-1:
        print('  - {}'.format(stations[x]))
        x +=1
    print('Jij stapt uit de trein in: {}'.format(eindstation))

beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)