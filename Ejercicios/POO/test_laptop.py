from laptop import Laptop
from laptop_gaming import Laptop_Gaming

def imprimir_informe(laptop):
    informe=laptop.realizar_informe_uso()
    for clave, valor in informe.items():
        print(f"{clave}: {valor}")
    print("\n")


laptopPepito=Laptop_Gaming("Hp","i7",32,20,"RTX")
laptopMartin=Laptop_Gaming("Asus","i5",16,1000,"GTX")


print("Pepito:")
imprimir_informe(laptopPepito)

print("Martin:")
imprimir_informe(laptopMartin)

# print(laptop.comparar_costo(laptopPepito,laptopMartin))

# laptopGamingPepito=laptopGaming("Hp","i7",32,1000,20)
# print(laptopGamingPepito.valorFinal())


# # for numero in range(1,1001):
# #     ausLaptop=laptop.asus(numero)
# #     print(ausLaptop.__dict__)