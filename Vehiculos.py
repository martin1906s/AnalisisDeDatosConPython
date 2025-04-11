class Vehiculo:
    def __init__(self, marca, modelo, anio: int):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def descripcion(self):
        print(f"\n\nMarca: {self.marca}\nModelo: {self.modelo}\nAño: {self.anio}\n")

class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio: int, puertas: int):
        super().__init__(marca, modelo, anio)
        self.puertas = puertas

    def descripcion(self):
        super().descripcion()
        print(f"Puertas: {self.puertas}")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio: int, tipo):
        super().__init__(marca, modelo, anio)
        self.tipo = tipo
    
    def descripcion(self):
        super().descripcion()
        print(f"Tipo: {self.tipo}")