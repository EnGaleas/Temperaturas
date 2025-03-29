""" Utilizar diccionarios en Python para representar información estructurada y realizar operaciones comunes.

Instrucciones:

Crear un Diccionario:

Crea un diccionario llamado informacion_personal que contenga información ficticia sobre una persona, incluyendo al menos las claves "nombre", "edad", "ciudad" y "profesion".
Acceder y Modificar Valores:

Accede al valor asociado con la clave "ciudad" y modifícalo con una ciudad diferente.
Agrega una nueva clave-valor al diccionario que represente la "profesion" de la persona.
Verificar Existencia de Claves:

Verifica si la clave "telefono" existe en el diccionario. Si no existe, agrégala con un número de teléfono ficticio.
Eliminar una Clave:

Elimina la clave "edad" del diccionario, ya que esa información no es necesaria.
Imprimir el Diccionario Final:

Imprime el diccionario resultante después de realizar todas las operaciones."""

# Crear un diccionario con información ficticia de una persona
informacion_personal = {
    "nombre": " Carlos Hurtado",
    "edad": 35,
    "ciudad": "Riobamba",
    "profesion": "Ingeniero"
}

# Acceder al valor de la clave "ciudad" y modificalo con una ciudad diferente
informacion_personal["ciudad"] = "Guaranda"

# Agregar una nueva clave-valor al diccionario que represente la "profesion" de la persona.
informacion_personal["profesion"] = "Desarrollador de software"

# Verificar si la clave "telefono" existe en el diccionario
# Si no existe, agregarla con un número ficticio
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0969877293"

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
