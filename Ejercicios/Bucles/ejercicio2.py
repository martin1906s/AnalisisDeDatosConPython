frase = str(input("Frase: "))
letra = str(input("Letra"))

contador=0
for i in frase:
    if i==letra:
        contador+=1
print(f"La letra {letra} se repite {contador} veces")
print(f"{frase.count(letra)}")