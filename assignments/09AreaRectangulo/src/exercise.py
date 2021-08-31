def areaRect(base,altura):
    resp=base*altura
    return resp


def main():
    #escribe tu código abajo de esta línea
    base=float(input("Dame la base: "))
    altura=float(input("Dame la altura: "))
    print("El área del rectángulo es: ",areaRect(base,altura))
    pass

if __name__=='__main__':
    main()
