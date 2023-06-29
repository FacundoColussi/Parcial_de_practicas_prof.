"""Del punto anterior, y considerando que durante 12 meses el empleado trabajó las mismas cantidades de 
horas, escribe un programa que calcule el descuento anual a realizarse, considerando: 
a. Si el sueldo anual es mayor a $2.000.000, el descuento es del %5.
b. Si el sueldo anual esta entre $1.000.000 y $2.000.000, debe aplicarse un descuento del %3.
c. Si el sueldo anual es menor a $1.000.000, debe aplicarse un descuento del %1. 
d. El programa debe mostrar elsalario anual bruto, el monto anual de bonificaciones, el monto anual 
a descontarse y las horas trabajadas en todo el año."""

# Ingreso de datos.
horas_trabajadas = int(input("- por favor, Ingrese la cantidad de horas trabajadas en el mes: "))  

#calculo de horas trabajadas con bonificacion 0.18%
if horas_trabajadas > 120:
    pago_por_hora = 1500 
    sueldos_brutos = pago_por_hora * horas_trabajadas
    bonificacion_018 = ( horas_trabajadas * pago_por_hora ) * 0.18
    sueldos_netos = sueldos_brutos + bonificacion_018 
    salario_anual = sueldos_brutos * 12
    bonificacion_anual = bonificacion_018 * 12
    desc_anual = (salario_anual + bonificacion_anual) * 0.05
    horas_trabajadas_anuales = horas_trabajadas * 12
    print("- Su salario anual bruto es de: $", salario_anual)
    print()
    print("- Su bonificacion anual es de: $", bonificacion_anual)
    print()
    print("- Su monto anual descontado es de: $", desc_anual)
    print()
    print("- Sus horas trabajadas son: ", horas_trabajadas_anuales)

#calculo de horas trabajadas con bonificacion 0.15%
elif 80 <= horas_trabajadas <= 120:
    pago_por_hora = 1300 
    sueldos_brutos = pago_por_hora * horas_trabajadas
    bonificacion_015 = ( horas_trabajadas * pago_por_hora ) * 0.15
    sueldos_netos = sueldos_brutos + bonificacion_015
    sueldos_netos = sueldos_brutos + bonificacion_015 
    salario_anual = sueldos_brutos * 12
    bonificacion_anual = bonificacion_015 * 12
    desc_anual = (salario_anual + bonificacion_anual) * 0.03
    horas_trabajadas_anuales = horas_trabajadas * 12
    print("- Su salario anual bruto es de: $", salario_anual)
    print()
    print("- Su bonificacion anual es de: $", bonificacion_anual)
    print()
    print("- Su monto anual descontado es de: $", desc_anual)
    print()
    print("- Sus horas trabajadas son: ", horas_trabajadas_anuales)
    
#calculo de horas trabajadas con bonificacion 0.13%
elif horas_trabajadas < 80:
    pago_por_hora = 1100
    sueldos_brutos = pago_por_hora * horas_trabajadas
    bonificacion_013 = ( horas_trabajadas * pago_por_hora ) * 0.13
    sueldos_netos = sueldos_brutos + bonificacion_013 
    sueldos_netos = sueldos_brutos + bonificacion_013
    salario_anual = sueldos_brutos * 12
    bonificacion_anual = bonificacion_013 * 12
    desc_anual = (salario_anual + bonificacion_anual) * 0.01
    horas_trabajadas_anuales = horas_trabajadas * 12
    print("- Su salario anual bruto es de: $", salario_anual)
    print()
    print("- Su bonificacion anual es de: $", bonificacion_anual)
    print()
    print("- Su monto anual descontado es de: $", desc_anual)
    print()
    print("- Sus horas trabajadas son: ", horas_trabajadas_anuales)
   

