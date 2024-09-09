def calcular(multiplicando, multiplicador, sumador):
    res = multiplicando * multiplicador + sumador
    return res


def principal():
    multiplicando = float(input("Ingresa multiplicando: "))
    multiplicador = float(input("Ingresa multiplicador: "))
    sumador = float(input("Ingresa sumador: "))
    resultado = calcular(multiplicando, multiplicador, sumador)
    print("El resultado de la operacion")
    print(f"{multiplicando} * {multiplicador} + {sumador} = {resultado}")


principal()
