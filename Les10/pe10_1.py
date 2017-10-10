import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionairy = xmltodict.parse(filecontentstring)
        return xmldictionairy

productendict = processXML('producten.xml')
artikelen = productendict['artikelen']['artikel']

for artikel in artikelen:
    print(artikel['naam'])