"""Escribe un programa que calcule el área y el perímetro de un cuadrado
 y muestre los resultados (indicando cuál es cuál) por pantalla."""

# ingreso de datos.
lados = int(input("- Ingrese el valor de los lados: "))

# Se calcula el area y perimetro del cuadrado.
area = lados * 2
perimetro = lados * 4
print()
print("> El cuadrado tiene un área de: ", area )
print()
print("> El cuadrado tendra un perimetro de:", perimetro)