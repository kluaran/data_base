import bot_sozdanie_classa.chek.punctuation as punct
import bot_sozdanie_classa.chek.registr as reg

def fullcheck(vhod_dan):
    vhod_dan=punct.filtr(vhod_dan)
    y=[]
    for x in vhod_dan:
        x=reg.zagl(x)
        y.append(x)
    vhod_dan=y
    return vhod_dan

