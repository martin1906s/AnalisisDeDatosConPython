import random
aleatorio = random.randint(1, 9)
aleatorio2 = random.randint(1, 9)

if aleatorio == 4:
    print("Te ganaste un coche")
elif aleatorio == 8:
    print("Te ganaste una casa")
elif aleatorio == 3 and aleatorio2 == 7:
    print("Te ganaste un perro")
else:
    print("Perdiste")