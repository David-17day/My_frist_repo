# Salud
Nombre = input("¿Cómo te llamas? :  ")
print(f"Hola {Nombre}! Bienvenido al programa de Cálculo de áreas")
# Área de un cuadrado, triángulo y círculo.
import math
def area_cuadrado():
    lado = float(input("Ingresa el lado del cuadrado: "))
    return lado**2
def area_triangulo():
    base = float(input("Ingrese la base del triangulo: "))
    altura= float(input("Ingrese la altura del triangulo: "))
    return (base*altura)/2
def area_circulo():
    radio = float(input("Ingrese el radio del circulo: "))
    return math.pi * (radio**2)

while True:
    print("-------MENU DE CÁLCULO DE ÁREAS------")
    print("1. Calculo de area un cuadrado")
    print("2. Calculo de area un triangulo")
    print("3. Calculo de area circulo")
    print("4. Salir del menu")
    
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        print(f"El area del cuadrado es : {area_cuadrado()}")
    elif opcion == "2":
        print(f"El area del triangulo es: {area_triangulo()}")
    elif opcion == "3":
        print(f"El area del circulo es: {area_circulo()}")
    elif opcion == "4":
        print("Ha salido del menu")
        break
    else:
        print('Opcion no valida - Error')
        