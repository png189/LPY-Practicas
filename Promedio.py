nombre= input ("Ingresa tu nombre: ")
print("Ingresa tus notas: ")
n1 = int(input("Nota 1 -> "))
n2 = int(input("Nota 2 -> "))
n3 = int(input("Nota 3 -> "))
promedio= (n1+n2+n3)/3
print(f"{nombre}, tu promedio es: {round(promedio, 2)}")