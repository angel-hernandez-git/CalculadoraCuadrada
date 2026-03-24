#Desarrollar un programa que solucione una funcion cuadratica (La que sea), que contenga dentro de si los siguientes parametros
#if // while // For // Funcion // Metodo // Clase....
#Debe de arrojar una grafica y solucion numerica (En jupyter).

import numpy as np
import matplotlib.pyplot as plt


def graficar_funcion(a, b, c, x_min=-10,x_max=10):
    # Generar valores de x
    x = np.linspace(x_min, x_max, 400)
    y = a*x**2 + b*x + c

    # Mostrar la función
    print(f"f(x) = {a}x² + {b}x + {c}")

    # Graficar
    plt.figure(figsize=(6,4))
    plt.plot(x, y, label=f"{a}x² + {b}x + {c}", color="blue")
    plt.axhline(0, color="black", linewidth=0.7)
    plt.axvline(0, color="black", linewidth=0.7)
    plt.legend()
    plt.title("Función cuadrática")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    print("=== Calculadora de función cuadrática ===")
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))
    x_min = float(input("Ingrese el valor mínimo de x: "))
    x_max = float(input("Ingrese el valor máximo de x: "))

    graficar_funcion(a, b, c, x_min, x_max)