"""Escribe un programa que permita ingresar las edades de las personas, hasta que el usuario decida no 
hacerlo más, y muestre, al final, un promedio de las edades ingresadas y el total de personas ingresadas"""

#ingreso de datos
contador_personas = 0
suma_edades = 0
ingresar_edad = 1

# Se utiliza while
while ingresar_edad == 1:
    detener = input("- Ingrese las edades -Escriba ¨salir¨ si no ingesa mas edades-:")
    print()
    
    # Se utiliza la variable detener asi el usuario elije cuando deja de cargar edades 
    if detener == "salir":
        ingresar_edad = 0
    else:
        edad = int(detener)
        suma_edades = suma_edades + edad
        contador_personas = contador_personas + 1

if contador_personas > 0:
    promedio = suma_edades / contador_personas
    print("> Promedio de edades ingresadas :", promedio , "Años" )

print()
print("> Total de personal ingresado:", contador_personas)