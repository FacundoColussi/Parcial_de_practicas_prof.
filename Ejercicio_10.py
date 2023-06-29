"""Escribe un programa que calcule el promedio general de una clase."""

# Ingreso de datos
cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))
contador = 0
suma_calificaciones = 0
alumnos = 0

# Se inicia while 
while contador < cantidad_alumnos:
    contador = contador + 1
    print()
    print("Alumno", contador)

    calificacion = float(input("Ingrese la calificación: "))
    suma_calificaciones = suma_calificaciones + calificacion


    # Se limita la nota entre 0 a 10 para prevenir que ingresen mal.
    if suma_calificaciones < 0 :
        print("> ¡Vuelva a intentantarlo! La nota debe ser de 0 a 10.")
        print()
        alumnos = alumnos - 1 
    elif suma_calificaciones >= 10 :
        print("> ¡vuelva a intentantarlo! La nota debe ser de 0 a 10.")
        alumnos = alumnos - 1 
    
promedio = suma_calificaciones / cantidad_alumnos

print()
print("el promedio de la clase es de:" , promedio )
