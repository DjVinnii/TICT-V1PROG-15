import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

stationsdict = processXML('stationslijst.xml')
stations = stationsdict['Stations']['Station']

print('Dit zijn de codes en de types van de {} stations: \n'.format(len(stations)))
for station in stations:
    print('{:4} - {}'.format(station['Code'], station['Type']))

print('\nDit zijn alle stations met één of meer synoniemen:')
for station in stations:
    if station['Synoniemen'] is not None:
        synoniemen = station['Synoniemen']['Synoniem']
        for synoniem in synoniemen:
            print('{:4} - {}'.format(station['Code'], synoniem))

print('\nDit is de lange naam van elk station:\n')
for station in stations:
    print('{:4} - {}'.format(station['Code'], station['Namen']['Lang']))