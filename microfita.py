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

def A(z, e_relativa):
    return (z/60)*np.sqrt((e_relativa+1)/2)+((e_relativa-1)/(e_relativa+1))*(0.23+0.11/e_relativa)

def B(z, e_relativa):
    return (377*np.pi)/(2*z*np.sqrt(e_relativa))