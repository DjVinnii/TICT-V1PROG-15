invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
invoer = invoer.split('-')
invoer = list(map(int, invoer))
invoer.sort()

print('Gesoorteede list van ints: {}\nGrootste getal: {} en kleinste getal: {}\nAantal getallen: {} en som van getallen: {}\nGemiddelde: {}'.format(str(invoer), invoer[-1], invoer[0], len(invoer), sum(invoer), str(sum(invoer)/len(invoer))))