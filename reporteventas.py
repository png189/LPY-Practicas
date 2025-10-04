#entrada
nombre = input("Ingresa tu nombre: ")
sbase=float(input("De cuanto es tu salario base?"))
print("Cuanto vendiste en los ultimos 3 meses? ")
mes1= float(input("Mes 1: "))
mes2= float(input("Mes 2: "))
mes3= float(input("Mes 3: "))
#proceso
total=mes1+mes2+mes3
promedio=total/3
#5% del seguro social
desc_segurosocial= sbase*0.05
#10% bono de aumento por aniversario sobre el salario base
aumento_ani=sbase*0.1

salariototal=sbase+aumento_ani-desc_segurosocial
#salida
print(f"Empleado: {nombre}, vendio un total de {total}")
print(f"Siendo su promedio de ventas de: {round(promedio, 2)}")
print(f"Descuento del seguro social {desc_segurosocial} y aumento de aniversario {aumento_ani}, su salario final es de {salariototal}")