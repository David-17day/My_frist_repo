# Saludo
Nombre = input("¿Cómo te llamas? :  ")
print(f"Hola {Nombre}! Bienvenido al programa de Suma de dos números")
# Suma
def suma():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    return num1 + num2
# Menú
while True:
    print("-------MENU DE SUMA DE DOS NÚMEROS------")
    print("1. Sumar dos números")
    print("2. Salir del menu")
    
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        print(f"La suma de los dos números es: {suma()}")
    elif opcion == "2":
        print("Ha salido del menu")
        break
    else:
        print('Opcion no valida - Error')
