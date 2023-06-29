"""Escribe un programa que calcule el promedio final de una materia, 
basado en 3 notas de parciales, indicando por pantalla si el alumno 
aprobó o debe recursar la materia (se aprueba con 6)."""

#Ingreso del acumulador.
alumnos = 1
acumulador_nota = 0
contador = 0

# Se usa while para establecer cuantas notas se pueden cargar
while alumnos <= 3:
    nota = float(input("- Por favor ,ingrese la nota del alumno: "))
    print()
    alumnos = alumnos + 1
    
    # Se limita la nota entre 0 a 10 para prevenir que ingresen mal.
    if nota < 0 :
        print("> ¡Vuelva a intentantarlo! La nota debe ser de 0 a 10.")
        print()
        alumnos = alumnos - 1 
    elif nota > 10 :
        print("> ¡vuelva a intentantarlo! La nota debe ser de 0 a 10.")
        alumnos = alumnos - 1 
    else:
        acumulador_nota = acumulador_nota + nota

#Calculo para promedio de los alumnos.
promedio_final = acumulador_nota / 3
    
if promedio_final >= 6:
    print("¡EL alumno aprobo! su promedio es de: ", promedio_final)
    print()
else:
    print("¡El alumno desaprobo! su promedio es de: ", promedio_final)