"""Escribe un programa que calcule la equivalencia a pesos
de los dólares ingresados por pantalla. El programa debe 
preguntar el tipo de cambio a convertir (es decir, cuánto cotiza el dólar)."""

#Ingreso de datos
dolares = int(input("- Ingrese la cantidad de dolares que desea cambiar: $"))
print()
pesos = int(input("- Ingrese el tipo de cambio al que desea cambiar: $"))

#Calculo de conversion de dolares a pesos.
conversion = dolares * pesos
print()
print("> Su conversion de dolares a pesos es: $", conversion)