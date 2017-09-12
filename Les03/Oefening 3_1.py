name = input("Wat is je naam: ")
age = eval(input("Wat is je leeftijd: "))
if age >= 18:
    print(name + ", je mag stemmen.")
else:
    print(name + ", je mag nog niet stemmen.")