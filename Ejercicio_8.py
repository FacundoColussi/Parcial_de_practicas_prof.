"""Escribe un programa solicite y muestre por pantalla el nombre, 
apellido y edad de 5 personas."""

#Ingreso de datos
persona = 1

while persona <= 5:
    nombre = input("- Ingrese Nombre: ")
    print()
    apellido = input("- Ingrese su Apellido: ") 
    print()
    edad = int(input("- Ingrese su edad: "))
    print()
    
    # Se usa un acumulador
    persona = persona + 1 
    
    if edad < 0 :
        print("¡Vuelve a intentarlo!")
        persona = persona - 1
        
    elif edad >= 0 :
        print("> Nombre", nombre)
        print()
        print("> Apellido", apellido)
        print()
        print("> Edad:", edad )
        print("___________________________________")
