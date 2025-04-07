print("*** KrakeTravels ***")
print("*** Pais ***")
print("1. Ecuador\n2. Colombia\n3. Perú")
pais = int(input("Seleccion: "))

print("*** Zona ***")
print("1. Zona Urbana\n2. Zona Rural\n3. Zona Perimetral")
zona = int(input("Seleccion: "))

print("*** Velocidad ***")
velocidad = int(input("Velocidad (km/h): "))

if pais == 1:
    print("*** Ecuador **")
    if zona == 1:
        print("Zona Urbana")
        if 10 <= velocidad <= 50:
            print("Velocidad permitida")
        else:
            print("Fuera de rango Máximo 50 Km/h y mínimo 10 Km/h") 
    elif zona == 2:
        print("Zona Rural")
        if 51 <= velocidad <= 70:
            print("Velocidad permitida")
        else:
            print("Fuera de rango Máximo 70 Km/h y mínimo 51 Km/h")
    elif zona == 3:
        print("Zona Perimetral")
        if 71 <= velocidad <= 90:
            print("Velocidad permitida")
        else:
            print("Fuera de rango Máximo 90 Km/h y mínimo 71 Km/h")

elif pais == 2:
    print("*** Colombia **")
    if zona == 1:
        print("Zona Urbana")
        if 10 <= velocidad <= 30:
            print("Velocidad permitida")
        else:
            print("Fuera de rango Máximo 30 Km/h y mínimo 10 Km/h")
    elif zona == 2:
        print("Zona Rural")
        if 31 <= velocidad <= 80:
            print("Velocidad permitida")
        else:
            print("Fuera de rango Máximo 80 Km/h y mínimo 31 Km/h")
    elif zona == 3:
        print("Zona Perimetral")
        if 81 <= velocidad <= 100:
            print("Velocidad permitida")
        else:
            print("Fuera de rango Máximo 100 Km/h y mínimo 81 Km/h")

elif pais == 3:
    print("*** Perú **")
    if zona == 1:
        print("Zona Urbana")
        if 10 <= velocidad <= 40:
            print("Velocidad permitida")
        else:
            print("Fuera de rango Máximo 40 Km/h y mínimo 10 Km/h")
    elif zona == 2:
        print("Zona Rural")
        if 41 <= velocidad <= 60:
            print("Velocidad permitida")
        else:
            print("Fuera de rango Máximo 60 Km/h y mínimo 41 Km/h")
    elif zona == 3:
        print("Zona Perimetral")
        if 61 <= velocidad <= 120:
            print("Velocidad permitida")
        else:
            print("Fuera de rango Máximo 120 Km/h y mínimo 61 Km/h")

else:
    print("Opción no válida")

