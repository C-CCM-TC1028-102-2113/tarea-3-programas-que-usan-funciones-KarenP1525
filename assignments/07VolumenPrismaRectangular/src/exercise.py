
def areaRect(base,altura):
    resultado=base*altura
    return resultado

def volRect(base,altura,profundidad):
    
    return areaRect(base,altura)*profundidad
    
def main():
  #escribe tu código abajo de esta línea
  base=float(input("Dame la base: "))
  altura=float(input("Dame la altura: "))
  profundidad=float(input("Dame la profundidad: "))
  v=volRect(base,altura,profundidad)
  print("El volumen del prisma es: ",v)

if __name__ == '__main__':
    main()
