cijfers = {'Jan':1, 'Klaas':8, 'Piet':9, 'Henk':10, 'Harry':9}

for k,v in cijfers.items():
    if v >= 9:
        print(k + ': ' + str(v))