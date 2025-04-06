"""Escritura de Archivo de Texto:

Crea un nuevo archivo llamado my_notes.txt.
Escribe al menos tres líneas de notas personales en el archivo.
Lectura de Archivo de Texto:

Abre el archivo my_notes.txt.
Lee el contenido del archivo línea por línea.
Muestra en la consola cada línea leída.
Cierre de Archivos:

Asegúrate de cerrar el archivo my_notes.txt después de realizar las operaciones necesarias.
Instrucciones Adicionales:

Utiliza métodos como write() y readline() para manipular el archivo de texto.
Agrega comentarios explicativos en tu código."""
# Ejemplo de Escritura en Archivos en Python usando write() y Readline()
# Definimos el nombre del archivo
file_name = "my_notes.txt"
# Escritura en el archivo de texto
# Modo de apertura: "w" para escritura (write)
file = open('my_notes.txt', 'w')

# Metodo write(): escribir una línea a la vez
file.write("1. Hoy organicé mi horario de estudio para la semana.\n")
file.write("2. Asistí a clases y tomé apuntes importantes.\n")
file.write("3. Estudié para el próximo examen de matemáticas.\n")
file.write("4. Hice un resumen del tema visto en clase de historia.\n")
file.write("5. Participé en un grupo de estudio con mis compañeros.\n")
file.write("6. Organicé mis archivos y tareas en la computadora.\n")
file.write("7. Revisé los materiales del curso en la plataforma educativa.\n")
file.write("8. Practiqué ejercicios adicionales para reforzar lo aprendido.\n")
file.write("9. Hablé con un profesor para resolver dudas sobre un tema.\n")
file.write("10. Me propuse mejorar mi rendimiento académico este mes.\n")

# Cierra el archivo después de escribir
file.close()

# Lectura del archivo de texto
# Abre el archivo 'my_notes.txt' en modo lectura ('r')
file = open('my_notes.txt', 'r')

# Metodo readline(): leemos cada línea una a una
# Lee y muestra cada línea del archivo
line = file.readline()
while line:
    print(line.strip())  # .strip() elimina saltos de línea adicionales
    line = file.readline()

# Cierra el archivo después de leer
file.close()