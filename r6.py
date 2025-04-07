class Auto:
    def __init__(self, marca, modelo, año, kilometraje=0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
    
    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Kilometraje: {self.kilometraje} km")
    
    def actualizar_kilometraje(self, km):
        if km >= self.kilometraje:
            self.kilometraje = km
            print(f"Kilometraje actualizado a {self.kilometraje} km")
        else:
            print("No se puede reducir el kilometraje.")
    
    def realizar_viaje(self, kilometros):
        if kilometros > 0:
            self.kilometraje += kilometros
            print(f"Se han agregado {kilometros} km al kilometraje. Kilometraje actual: {self.kilometraje} km")
        else:
            print("La cantidad de kilómetros debe ser positiva.")
    
    def estado_auto(self):
        if self.kilometraje < 20000:
            print("Estoy como nuevo")
        elif 20000 <= self.kilometraje <= 100000:
            print("Ya estoy usado")
        else:
            print("¡Ya déjame descansar por favor!")

    @classmethod
    def crear_auto(cls, marca="Toyota", modelo="Family"):
        from datetime import datetime
        año_actual = datetime.now().year
        return cls(marca, modelo, año_actual, kilometraje=0)

    @staticmethod
    def comparar_kilometraje(auto1, auto2):
        if auto1.kilometraje == auto2.kilometraje:
            return "Ambos autos tienen el mismo kilometraje."
        elif auto1.kilometraje > auto2.kilometraje:
            return f"El auto {auto1.marca} tiene más kilometraje que el auto {auto2.marca}."
        else:
            return f"El auto {auto2.marca} tiene más kilometraje que el auto {auto1.marca}."
