def standaardprijs(afstandKM):
    prijs = 0

    #Negatieve afstand -> 0km
    if afstandKM < 0:
        afstandKM = 0

    # Meer dan 50km, 15eu + 60 cent/km anders 80 cent/km
    if afstandKM >= 50:
        prijs = 15 + 0.6*afstandKM
    else:
        prijs = 0.8 * afstandKM
    return prijs

def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)
    if weekendrit == False and (leeftijd < 12 or leeftijd >= 65):
        prijs = prijs * 0.7
        return prijs
    if weekendrit == True and (leeftijd < 12 or leeftijd >= 65):
        prijs = prijs * 0.65
        return prijs
    if weekendrit == True and (leeftijd >= 12 or leeftijd < 65):
        prijs = prijs * 0.60
        return prijs
    else:
        return prijs

leeftijd = eval(input('Vul je leeftijd in: '))
weekendrit = eval(input('Is het een weekendrit? (True/False)'))
afstandKM = eval(input('Vul het aantal kilometers in: '))

print(ritprijs(leeftijd, weekendrit, afstandKM))