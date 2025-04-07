nombre_paciente = []
edad = []

def agregar_nombre(info):
    nombre_completo = " ".join(info.split()[:-1])
    nombre_paciente.append(nombre_completo)

def agregar_edad(año_nacimiento):
    año_actual = 2025 
    if año_nacimiento <= año_actual:
        anios = año_actual - año_nacimiento
        edad.append(anios)
    else:
        print("Edad no válida")

def obtenerMayorMenor():
    if edad:
        mayor = max(edad)
        menor = min(edad)
        indice_mayor = edad.index(mayor)
        indice_menor = edad.index(menor)
        print(f"El paciente mayor es {nombre_paciente[indice_mayor]} con {mayor} años.")
        print(f"El paciente menor es {nombre_paciente[indice_menor]} con {menor} años.")
    else:
        print("No hay datos para procesar.")
