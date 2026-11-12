import getpass
import json
import os
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen


def mostrar_origen_nombre(nombre):
    nombre = " ".join(nombre.split())
    if not nombre:
        print("No se indicó un nombre para buscar.")
        return

    clave = os.environ.get("SERPAPI_API_KEY", "").strip()
    if not clave:
        clave = getpass.getpass(
            "Clave de SerpApi (oculta; Enter para omitir la búsqueda): "
        ).strip()
    if not clave:
        print("Búsqueda omitida: no se ingresó una clave.")
        return

    parametros = urlencode({
        "engine": "google",
        "q": f"origen historia y significado del nombre {nombre}",
        "hl": "es",
        "api_key": clave,
    })
    print("Buscando el origen de tu nombre en Google...")

    try:
        with urlopen("https://serpapi.com/search.json?" + parametros,
                     timeout=20) as respuesta:
            datos = json.load(respuesta)
    except HTTPError as error:
        error.close()
        mensajes = {
            401: "La clave de SerpApi no es válida.",
            403: "SerpApi no autorizó la consulta. Revisa tu cuenta.",
            429: "Se alcanzó el límite de consultas. Revisa tu cuenta.",
        }
        print(mensajes.get(error.code, "El servicio de búsqueda falló."))
        return
    except (URLError, OSError):
        print("No se pudo conectar al servicio o se agotó el tiempo de espera.")
        return
    except ValueError:
        print("El servicio devolvió una respuesta que no se pudo leer.")
        return

    if not isinstance(datos, dict) or datos.get("error"):
        print("No se pudo obtener información. Intenta de nuevo más tarde.")
        return

    resultados = datos.get("organic_results", [])
    if not isinstance(resultados, list):
        resultados = []

    mostrados = 0
    for resultado in resultados:
        if not isinstance(resultado, dict):
            continue
        texto = resultado.get("snippet")
        fuente = resultado.get("link")
        if not isinstance(texto, str) or not texto.strip():
            continue
        if not isinstance(fuente, str) or not fuente.startswith(("https://", "http://")):
            continue
        print(f"\n{texto.strip()}")
        print(f"Fuente: {fuente}")
        mostrados += 1
        if mostrados == 3:
            break

    if not mostrados:
        print("Google no devolvió extractos sobre este nombre.")


# Saludo al usuario y presentación del programa
Nombre = input("¿Cómo te llamas? :  ").strip()
print(f"Hola {Nombre}! Bienvenido al programa de Cálculo de áreas")
mostrar_origen_nombre(Nombre)
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
        
