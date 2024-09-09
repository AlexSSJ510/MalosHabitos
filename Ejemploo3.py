# Función para calcular el área de un rectángulo
def AreaRectangulo(longitud, ancho):
    result = longitud * ancho
    return result

# Función para calcular el área de un triángulo
def AreaTriangulo(base, altura):
    resultadoT = 0.5 * base * altura
    return resultadoT

# Función principal
def main():
    (print("Calcular el Area del Rectangulo"))
    longitud = float(input("Ingresa la longitud: "))
    ancho = float(input("Ingresa su anchura: "))
    rect_area = AreaRectangulo(longitud, ancho)
    print("Área del rectángulo: ", rect_area,"\n")

    (print("Calcular el Area del Triangulo"))
    base = float(input("Ingresa su base: "))
    altura = float(input("Ingresa su altura: "))
    tri_area = AreaTriangulo(base, altura)
    print("Área del triángulo: ", tri_area)


main()
