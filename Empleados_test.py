from Empleados import *

empleados = [
    EmpleadoMedioTiempo("Luis", 800),
    EmpleadoTiempoCompleto("Carlos", 1200),
    EmpleadoMedioTiempo("Laura", 900),
    EmpleadoTiempoCompleto("Martín", 470),
    EmpleadoMedioTiempo("Ana", 350)
]

for empleado in empleados:
    salarioFinal = empleado.calcular_salario()
    print(f"Nombre: {empleado.nombre}, Salario Base: {empleado.salario_base}, Salario Final: {salarioFinal}")