
# Iniciamos con el Archivos: open()
# Creamos un nuevo archivo llamado my_notes.txt en modo escritura ('w')
print(":(-:(-:(..... Mi nota en texto :(-:(-:(.....")

# Nombre del archivo
nombre_archivo = "my_notes.txt"

# Abrimos el archivo en modo escritura
archivo = open(nombre_archivo, 'w')

# Escritura en Archivos: write()
# Escribimos tres líneas de notas personales en el archivo
archivo.write("Nota 1: Recuerda debes de realizar el deber de programación.\n")
archivo.write("Nota 2: Debes de estar listo para rendir el próximo examen del 7 de Octubre.\n")
archivo.write("Nota 3: El apagón es muy fuerte que no entra la señal en el celular.\n")
archivo.write("Nota 4: No tengo internet en mi casa y no podré hacer el examen.\n")

# Cierre de Archivos: close()
# Cerramos el archivo después de escribir
archivo.close()

# Lectura de Archivo de Texto:
# Abrimos el archivo my_notes.txt en modo lectura ('r')
archivo = open(nombre_archivo, 'r')

# Lectura de Archivos: readline()
# Leemos el contenido del archivo línea por línea
line_1 = archivo.readline()  # Leemos la primera línea
line_2 = archivo.readline()
line_3 = archivo.readline()
line_4 = archivo.readline()

# Mostramos en la consola cada línea leída
print("\n Mostrar el contenido línea por línea:")
print("línea 1:", line_1.strip())
print("línea 2:", line_2.strip())
print("línea 3:", line_3.strip())
print("línea 4:", line_4.strip())

# Cierre del archivo
archivo.close()

