
def es_bisiesto(anio):
    return not anio%4 and ((not anio%100 and not anio%400)or(anio%100!=0))


def main():
    #escribe tu código abajo de esta línea
    anio=int(input("Dame el año: "))
    print(es_bisiesto(anio))

    pass

if __name__=='__main__':
    main()
