studentencijfers = [[95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0]]

def gemiddelde_per_student(studentencijfers):
    antw = []
    for cijfers in studentencijfers:
        antw.append(sum(cijfers)/len(cijfers))
    return antw

def gemiddelde_van_alle_studenten(studentencijfers):
    cijfers = gemiddelde_per_student(studentencijfers)
    antw = sum(cijfers)/len(cijfers)
    return antw

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))