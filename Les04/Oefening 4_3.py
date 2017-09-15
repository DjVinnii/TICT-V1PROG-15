lst = [4, 0, 1, -2]

def swap(lijst):
    if len(lijst) > 1:
        #Doe de swap
        lijst[0], lijst[1] = lijst[1], lijst[0]
        return(lst)
    else:
        print('De lijst is te klein!')

swap(lst)
print(lst)