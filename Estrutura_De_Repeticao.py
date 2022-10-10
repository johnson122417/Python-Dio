texto = input("INforme um Texto: ")
Vogais = "AEIOU"

for letra in texto:
    if letra.upper() in Vogais:
        print(letra, end="")

print()