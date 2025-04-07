menu = ["Ensalada", "Sopa", "Pasta", "Pizza", "Tacos", "Hamburguesa"]
print(menu)

print("*** Segunda es Todo ***\n   1. Añadir plato al menú\n   2. Buscar en el menú\n   3. Eliminar plato del menú\n   4. Mostrar platos del menú")
seleccion = int(input ("Seleccione: "))


if seleccion == 1: 
    plato = str(input("Nombre del Plato:"))
    menu.append(plato)
    print(menu)
elif seleccion == 2:
    plato = str(input("Nombre del Plato:"))
    if plato in menu:
        print(f"El plato {plato} está en el menú")
    else:
        print(f"El plato {plato} no está en el menú")
    print(menu)
elif seleccion == 3:
    plato = str(input("Nombre del Plato:"))
    if plato in menu:
        menu.remove(plato)
        print(menu)
elif seleccion == 4:
    print(menu)
else:
    print("Seleccion invalida")
