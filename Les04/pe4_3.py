lengte = eval(input('Wat is je lengte in centimeters: '))

def lang_genoeg(lengte):
    if lengte >= 120:
        print('Je bent lang genoeg voor de attractie!')
    else:
        print('Sorry, je bent te klein!')

lang_genoeg(lengte)