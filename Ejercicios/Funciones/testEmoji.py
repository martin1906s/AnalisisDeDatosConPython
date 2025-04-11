import emoji

cantidad=int(input("Cantiad: "))
for i in range(cantidad):
    frase=input("Frase: ")
    emoji.encontrar_palabra(frase)
    emoji.aggFrase(frase)