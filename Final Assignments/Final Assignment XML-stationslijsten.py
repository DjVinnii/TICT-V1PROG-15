import xmltodict
xmlfile = xmltodict.parse(open('stationslijst.xml').read())
print('Dit zijn de codes en de types van de {} stations:'.format(len(xmlfile['Stations']['Station'])))
for station in xmlfile['Stations']['Station']: print('{:4} - {}'.format(station['Code'], station['Type']))
print('\nDit zijn alle stations met één of meer synoniemen:')
for station in xmlfile['Stations']['Station']:
    if station['Synoniemen'] is not None:
        for synoniem in station['Synoniemen']['Synoniem']: print('{:4} - {}'.format(station['Code'], synoniem))
print('\nDit is de lange naam van elk station:')
for station in xmlfile['Stations']['Station']:print('{:4} - {}'.format(station['Code'], station['Namen']['Lang']))