infile = open('kaartnummers.txt', 'r')
regels = infile.readlines()
infile.close()
count = 0
kaartnummer = 0
regelnummer = 0
for regel in regels:
    count = count + 1
    kaartinfo = regel.split(',')
    if int(kaartinfo[0]) > kaartnummer:
        kaartnummer = int(kaartinfo[0])
        regelnummer = count
print('Deze file telt ' + str(count) + ' regels.')
print('Het grootste kaartnummer is: {} en dat staat op regel {}'.format(str(kaartnummer), str(regelnummer)))