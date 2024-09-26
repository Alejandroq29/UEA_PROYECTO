#Crearemos un diccionario llamdo informacion_personal que incluya nombre, edad, ciudad y profesion.

# Paso 1: Crear un diccionario llamado 'informacion_personal'
informacion_personal = {
    "nombre": "Alejandro Borja",        # Nombre de la persona
    "edad": 25,                   # Edad de la persona
    "ciudad": "Guayaquil",          # Ciudad donde vive
    "profesion": "Ingeniero"     # Profesión de la persona
}

# Paso 2: Imprimir el diccionario original
print("Información personal original:")
print(informacion_personal)

# Paso 3: Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Quito"  # Cambiamos la ciudad de Guayaquil a Quito
print("\nDespués de cambiar la ciudad:")
print(informacion_personal)

# Paso 4: Agregar una nueva clave-valor al diccionario para representar el "telefono"
informacion_personal["telefono"] = "026010661"  # Agregamos un número de teléfono ficticio
print("\nDespués de agregar el teléfono:")
print(informacion_personal)

# Paso 5: Verificar si la clave "correo" existe en el diccionario
if "correo" not in informacion_personal:  # Si "correo" no está en el diccionario
    informacion_personal["correo"] = "alejandro.borja@example.com"  # Agregamos un correo electrónico ficticio
print("\nDespués de verificar y agregar el correo:")
print(informacion_personal)

# Paso 6: Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:  # Si "edad" está en el diccionario
    del informacion_personal["edad"]  # Eliminamos la clave "edad"
print("\nDespués de eliminar la edad:")
print(informacion_personal)

# Paso 7: Imprimir el diccionario final
print("\nInformación personal final:")
print(informacion_personal)

# Imprimir el diccionario resultante después de realizar todas las operaciones
print(informacion_personal)