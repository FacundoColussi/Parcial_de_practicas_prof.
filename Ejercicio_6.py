""" Del punto anterior, calcular y mostrar por pantalla el sueldo bruto, el monto a bonificar y el sueldo neto 
(bruto + bonif), considerando:
a. Si trabajo más de 120hs, la bonificación es de %18
b. Si trabajo entre 80 y 120 horas, la bonificación es de %15
c. Si trabajo menos de 80 horas, la bonificación es de %13. """

# Ingreso de datos.
horas_trabajadas = int(input("Por favor ,ingrese la cantidad de horas trabajadas en el mes: "))  

#calculo de horas trabajadas con bonificacion 0.18
if horas_trabajadas > 120:
    pago_por_hora = 1500 
    sueldos_brutos = pago_por_hora * horas_trabajadas
    bonificacion_018 = ( horas_trabajadas * pago_por_hora ) * 0.18
    sueldos_netos = sueldos_brutos + bonificacion_018 
    print("- Su sueldo bruto es de: $", sueldos_brutos)
    print("- Con una bonificacion de: $", bonificacion_018)
    print("- Su sueldo neto es de: $", sueldos_netos )

#calculo de horas trabajadas con bonificacion 0.15
elif 80 <= horas_trabajadas <= 120:
    pago_por_hora = 1300 
    sueldos_brutos = pago_por_hora * horas_trabajadas
    bonificacion_015 = ( horas_trabajadas * pago_por_hora ) * 0.15
    sueldos_netos = sueldos_brutos + bonificacion_015 
    print("- Su sueldo bruto es de: $", sueldos_brutos)
    print("- Con una bonificacion de: $", bonificacion_015)
    print("- Su sueldo neto es de: $", sueldos_netos )
    
#calculo de horas trabajadas con bonificacion 0.13
elif horas_trabajadas < 80:
    pago_por_hora = 1100
    sueldos_brutos = pago_por_hora * horas_trabajadas
    bonificacion_013 = ( horas_trabajadas * pago_por_hora ) * 0.13
    sueldos_netos = sueldos_brutos + bonificacion_013 
    print("- Su sueldo bruto es de: $", sueldos_brutos)
    print("- Con una bonificacion de: $", bonificacion_013)
    print("- Su sueldo neto es de: $", sueldos_netos ) 
   

