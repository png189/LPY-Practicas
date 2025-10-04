nombre = input("Como te llamas?: ")
cantidad = int(input("Cuantos dolares quieres comprar?: "))
tasapreferir = (input("Que tasa quiere ver? "))
tasabcv = 158.93
tasaEuro = 188.03
preciobcv = cantidad*tasabcv
precioEuro = cantidad*tasaEuro

if tasapreferir.upper() == "BCV" :
    print(tasabcv)
    print(preciobcv)
elif tasapreferir.capitalize() == "Euro" :
    print(tasaEuro)
    print(precioEuro)
else: 
    print ("Tasa no disponible")