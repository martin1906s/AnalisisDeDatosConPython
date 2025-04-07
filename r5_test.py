from r5 import agregar_nombre, agregar_edad, obtenerMayorMenor, nombre_paciente, edad
pacientes = [
    "Antonio Moreno 2000",
    "Carmen Díaz 2001",
    "Fernando García 2003",
    "Teresa Rodríguez 2004",
    "José López 2005",
    "Miguel Ángel Ortiz 1999",
    "Lucia Gómez 2000",
    "Francisco Javier Sánchez 2001",
    "Beatriz Domínguez 2002",
    "Adrián López 2011",
    "Martina Pascual 2012",
    "Álvaro Torres 2013",
    "Berta Romero 2014"
]
for paciente in pacientes:
    print(f"Ingresando: {paciente}")
    nombre, año = " ".join(paciente.split()[:-1]), int(paciente.split()[-1])
    agregar_nombre(nombre)  
    agregar_edad(año)       
print("\nLista de nombres:")
print(nombre_paciente)
print("\nLista de edades:")
print(edad)
obtenerMayorMenor()
