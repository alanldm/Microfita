def e_efetiva(e_relativa, w, h):
    if w/h<1:
        return ((e_relativa+1)/2)+((e_relativa-1)/2)*(((1+12*h/w)**(-1/2))+0.04*((1-w/h)**2))
    elif w/h>1:
        return ((e_relativa+1)/2)+((e_relativa-1)/2)*(((1+12*h/w)**(-1/2)))