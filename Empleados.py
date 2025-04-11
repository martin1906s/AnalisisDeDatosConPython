from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, salario_base: float):
        self.nombre = nombre
        self.salario_base = salario_base

    @abstractmethod
    def calcular_salario(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    def calcular_salario(self):
        bono = self.salario_base * 0.20
        return self.salario_base + bono

class EmpleadoMedioTiempo(Empleado):
    def calcular_salario(self):
        bono = self.salario_base * 0.10
        return self.salario_base + bono