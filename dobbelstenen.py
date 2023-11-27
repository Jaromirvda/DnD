import random

def dobbelsteen_x(x):
    if x.lower() == 'd6':
        d6 = random.randint(1,6)
        return d6
    elif x.lower() == 'd4':
        d4=random.randint(1,4)
        return d4
    elif x.lower() == 'd8':
        d8=random.randint(1,8)
        return d8
    elif x.lower() == 'd10':
        d10=random.randint(1,10)
        return d10
    elif x.lower() == 'd12':
        d12=random.randint(1,12)
        return d12
    elif x.lower() == 'd20':
        d20=random.randint(1,20)
        return d20
    elif x.lower() == 'd100':
        d100=random.randint(1,4)
        return d100




def rollen(x,y,z):    
    
    o = []
    for i in range(y):
        w = dobbelsteen_x(x)
        o.append(w)
    return o

   
