"""Escribe un programa que solicite y muestre por pantalla nombre, apellido
 y edad de una cantidad de personas ingresada por el usuario."""

#ingrso de datos.
personas = int(input("- Ingrese la cantidad de personas: "))
contador = 0

# Se inicia while con el contador
while contador < personas:
    contador = contador + 1
    print()
    print("- Empleado", contador)
    print()

    nombre = input("- Ingrese el nombre: ")
    print()
    apellido = input("- Ingrese el apellido: ")
    print()
    edad = input("- Ingrese la edad: ", "Años")
    print()

    print("> Nombre: ", nombre)
    print("> Apellido: ", apellido)
    print("> Edad: ", edad , "Años" )