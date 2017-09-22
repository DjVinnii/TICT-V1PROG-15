def convert(celcius):
    fahrenheit = celcius * 1.8 + 32
    return fahrenheit

def table():
    print('  {:5}   {:5}'.format('F', 'C'))
    for i in range(-30, 50, 10):
        print('{:5}  {:5}'.format(convert(i), float(i)))

table()