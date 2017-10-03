def code(invoerstring):
    uitvoerstring = ''
    for letter in invoerstring:
        letter = ord(letter)
        letter +=3
        letter = chr(letter)
        uitvoerstring = uitvoerstring + letter
    print(uitvoerstring)

code("RutteAlkmaarDen Helder")