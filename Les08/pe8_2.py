import random

def monopolyworp():
    teller = 0

    while True:
        aantal1 = random.randrange(1,7)
        aantal2 = random.randrange(1,7)

        if aantal1 == aantal2:
            teller += 1
            if teller < 3:
                print(str(aantal1) + ' + ' + str(aantal2) + ' = ' + str(aantal1 + aantal2) + '(Dubbel)')
            else:
                print(str(aantal1) + ' + ' + str(aantal2) + ' = ' + str(aantal1 + aantal2) + '(Direct naar de gevangenis!)')
                break
        else:
            print(str(aantal1) + ' + ' + str(aantal2) + ' = ' + str(aantal1+aantal2))
            break

monopolyworp()