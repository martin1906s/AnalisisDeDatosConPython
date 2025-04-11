from Biblioteca import Libro

libro1 = Libro("Donde todo Brilla", "Allice Kellen", 300)
libro2 = Libro("100 años de soledad", "Gabriel Garcia Marquez", 400)
libro3 = Libro("El chico que dibujaba constelaciones", "Allice Kellen", 200)

Libro.mostrar_info(libro1)
Libro.mostrar_info(libro2)
Libro.mostrar_info(libro3)

print(Libro.es_grande(libro1.paginas))
print(Libro.es_grande(libro2.paginas))
print(Libro.es_grande(libro3.paginas))

print(Libro.total_libros([libro1, libro2, libro3]))