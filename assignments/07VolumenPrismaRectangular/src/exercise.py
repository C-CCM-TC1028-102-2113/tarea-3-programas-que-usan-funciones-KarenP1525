def main():
  #escribe tu código abajo de esta línea
  
  def areaRect(base,altura):
    resultado=base*altura
    return resultado

  def volRect(profundidad):
    resVol=areaRect(base,altura)*profundidad
    return resVol
    

  
  base=float(input("Dame la base: "))
  altura=float(input("Dame la altura: "))
  profundidad=float(input("Dame la profundidad: "))
  a=areaRect(base,altura)
  v=volRect(profundidad)
  print("El volumen del prisma es: ",v)

if __name__ == '__main__':
    main()
