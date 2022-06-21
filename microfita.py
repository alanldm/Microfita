import numpy as np

def e_efetiva(e_relativa, w, h):
    if w/h<1:
        return ((e_relativa+1)/2)+((e_relativa-1)/2)*(((1+12*h/w)**(-1/2))+0.04*((1-w/h)**2))
    elif w/h>1:
        return ((e_relativa+1)/2)+((e_relativa-1)/2)*(((1+12*h/w)**(-1/2)))

def velocidade(e):
    return 300000000/np.sqrt(e)

def impedancia(e, w, h):
    if w/h <=1:
        return (60/np.sqrt(e))*np.log(((8*h)/w)+(w/(4*h)))
    elif w/h >1:
        return np.sqrt(e)*((w/h)+1.393+0.667*np.log((w/h)+1.444))
