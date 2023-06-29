"""Escribe un programa que muestre los números del 1 al 10. Además,
  el programa debe mostrar:

 - a. Si es número es par o impar.
  - b. Cuanto es la suma total de todos los números mostrados.
   - c. Cuanto es la suma total de todos los números pares mostrados.
    - d. Cuanto es la suma total de todos los números impares mostrados."""

#Ingreso de datos
suma_total = 0
suma_pares = 0
suma_impares = 0

# Se inicia el contador
numero = 1

# While para mostrar los números del 1 al 10.
while numero <= 10:
    # Mostrar el número.
    print("Número:", numero)
    
    # Verificacion si es par o impar y mostrar el resultado.
    if int(numero / 2) * 2 == numero:
        print("Es un número par")
        suma_pares = suma_pares + numero
    else:
        print("Es un número impar")
        suma_impares = suma_impares + numero
    
    # suma total.
    suma_total = suma_total + numero
    
    # Se suma 1 al contador para que no haya un bucle 
    numero = numero + 1

print("Suma total:", suma_total)
print("Suma total de pares:", suma_pares)
print("Suma total de impares:", suma_impares)