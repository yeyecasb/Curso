with open("M3/clase9/textos.txt","r") as archivo:
    contenido = archivo.read()

palabras = contenido.split()

print(palabras)

palabras.append("Nueva palabra")

with open("M3/clase9/textos.txt","w") as archivo:
    archivo.write(" ".join(palabras))

print(palabras)