nombre = input("Como se llama?\n")
cedula = input("Ingrese el número de cédula\n")
producto = input("Cual es el nombre del producto?\n")
precio = float(input("Ingrese el precio del producto \n"))
fecha = input("Ingrese la fecha de hoy\n")
telefono = input("Ingrese el número de telefono del cliente: ")
saldo = float(input("Saldo Disponible\n"))

iva = precio*0.16
total = precio+iva


print("-"*40)
print("Nombre del cliente: ", nombre)
print("Cédula: ", cedula)
print("telefono: ", telefono)
print("Fecha: ", fecha )
print("-"*40)
print("--DATOS DE PAGO--")
print("Producto a comprar: ", producto)
print("Precio del producto: ", precio)
print("IVA del producto: ", iva)
print("Total a pagar es: ", total)
print("Saldo disponible del cliente: ", saldo)