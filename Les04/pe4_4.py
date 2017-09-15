def new_password(oldpassword, newpassword):
    if newpassword != oldpassword and len(newpassword) >= 6:
        for c in newpassword:
            if c in '0123456789':
                return True
        return False
    else:
        return False

#Correcte wachtwoorden --> True
res = new_password('vakProg17', 'python17')
print(res)

#Hetzelfde wachtwoord --> False
print(new_password('huProg17', 'huProg17'))

#Te kort wachtwoord --> False
print(new_password('vakProg17', 'Pro17'))