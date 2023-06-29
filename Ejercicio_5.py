"""Escribe un programa que calcule el sueldo de un empleado basándose
 en la cantidad de horas y muestre por pantalla el resultado,
 considerando lo siguiente:

  a. Si trabajo más de 120hs por mes, la hora tiene un valor de $1500.

   b. Si trabajo entre 80 y 120hs por mes, la hora tiene un valor de $1300.

    c. Si trabajo menos de 80 horas por mes, la hora tiene un valor de $1100.""" 

# Ingreso de datos.
horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas en el mes: "))  

#calculo de horas trabajadas 
if horas_trabajadas > 120:
    pago_por_hora = 1500 * horas_trabajadas
    print("Su sueldo es de $", pago_por_hora)

elif 80 <= horas_trabajadas <= 120:
    pago_por_hora = 1300 * horas_trabajadas
    print("Su sueldo es de $", pago_por_hora)

elif horas_trabajadas < 80:
    pago_por_hora = 1100 * horas_trabajadas
    print("Su sueldo es de $", pago_por_hora)


   

