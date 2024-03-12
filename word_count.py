import sys

if len(sys.argv) != 2:
    print("Uso: python word_count.py lorem_ipsum.txt")
    sys.exit(1)


ruta_archivo = sys.argv[1]


with open(ruta_archivo, "r") as archivo:
    texto = archivo.read()


caracteres_distintos = len(set(texto))
palabras = texto.split()
palabras_distintas = len(set(palabras))


print(f"El número de caracteres distintos es: {caracteres_distintos}")
print(f"El número de palabras distintas es: {palabras_distintas}")

