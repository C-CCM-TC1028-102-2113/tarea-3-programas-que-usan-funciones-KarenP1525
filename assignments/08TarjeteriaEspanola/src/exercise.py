
def maxTe(papeles,plumones):
    totPapTar=papeles*12
    totPluTar=plumones*35
    if(totPapTar==totPluTar):
        r=totPluTar
    elif(totPapTar<totPluTar):
        r=totPapTar
    else:
        r=totPluTar
    return r

def main():
    #escribe tu código abajo de esta línea
    papeles=int(input("Dame la cantidad de pliegos de papel albanene: "))
    plumones=int(input("Dame la cantidad de plumones: "))
    
    totTarjetas=maxTe(papeles,plumones)
    print("El número máximo de tarjetas que se pueden hacer es:",totTarjetas)
    pass

if __name__=='__main__':
    main()
