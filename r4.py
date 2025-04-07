datos = []

cantidad = int(input("¿Cuántos datos desea ingresar? "))

for i in range(cantidad):
    dato = input(f"Ingrese el dato {i + 1}: ")
    
    if dato.isdigit():  # Número entero
        datos.append(int(dato))
    elif dato.replace('.', '', 1).isdigit() and dato.count('.') < 2:  # Número decimal
        datos.append(float(dato))
    else:
        datos.append(dato)

print(f"Su lista es: {datos}")