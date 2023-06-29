"""Escribe un programa que calcule la edad que cumplió o debe 
cumplir este año la persona, basado en el año de nacimiento.""" 

#ingeso de datos.
nacimiento = int(input("- Por favor ,ingrese su año de nacimiento: "))
print()
cumpliria = int(input("- Por favor ,ingrese el año actual: "))
print()

#calculo para saber la edad actual de la persona.
actualidad = cumpliria - nacimiento
print("> ¡Felicidades! Este año usted cumplira: ", actualidad, "Años.")
