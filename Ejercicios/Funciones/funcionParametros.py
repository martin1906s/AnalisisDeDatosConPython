def datos(nombre,apellido,edad,mensaje="Hola"):
    if edad<18:
        print(f"{mensaje} {nombre} {apellido} es menor de edad")
    else:
        print(f"{mensaje} {nombre} {apellido} es mayor de edad")