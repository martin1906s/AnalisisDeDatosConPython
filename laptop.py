import random

class Laptop :
    def __init__(self,marca,procesador,memoria,costo = 500, impuesto = 10):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
        self.costo = costo
        self.impuesto = impuesto

    def valor_final(self):
        return self.costo + self.impuesto
    
    def valor_descuento(self, descuento):
        return (self.costo * descuento)/100


    def realizar_diagnostico_sistema(self):
        resultado = {
            "MARCA": f"{self.marca}",
            "PROCESADOR": f"{self.procesador}",
            "MEMORIA RAM": "OK" if self.memoria >= 8 else "Aumentar memoria RAM",
            "BATERIA": "OK" if random.choice([True, False]) else "Cambiar de batería"
        }
        return resultado
    #Polimorfismo
    def realizar_informe_usi(self):
        resultado_informe = {
            "Tipo": "Generica",
            "Uso Recomendado": "Tareas Cotidianas",
            "Horas de uso": 5,
            "Diagnostico actual" : self.realizar_diagnostico_sistema() 
        }
        return resultado_informe
            
        
    @staticmethod
    def comparar_costo(Laptop1,Laptop2):
        if Laptop1.costo == Laptop2.costo:
            return "Los costos son iguales"
        return "Los costos son diferentes"
    
    #Referencia a la propia clase
    @classmethod
    def asus_laptop (cls, costo) :
        marca = "asus"
        procesador = "i5"
        memoria = 16
        return cls(marca,procesador,memoria,costo)