def multiplicacion(multiplicando, multiplicador):
    Producto = multiplicando * multiplicador
    return Producto


if __name__ == "__main__":
    multiplicando = float(input("Ingresa multiplicando: "))
    multiplicador = float(input("Ingresa multiplicador: "))
    resultado = multiplicacion(multiplicando, multiplicador)
    print(f"{multiplicando} * {multiplicador} = {resultado}")