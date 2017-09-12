naam = input("Wat is je naam: ")
leeftijd = eval(input("Wat is je leeftijd: "))
paspoort = input("Nederlands paspoort (ja/nee): ")
if leeftijd >= 18 and paspoort == "ja":
    print(naam + ", je mag stemmen.")
else:
    print(naam + ", je mag niet stemmen.")