""" SPRINT DE ENTREGA:
Se solicita como entregable de este Sprint la implementación final de todos los conceptos vistos durante
el Módulo 1 de Python básico. Por tanto, se debe poner foco en lo siguiente:
● Elaborar un programa que recorra una lista con los nombres de 10 de sus futuros usuarios de tu
aplicación (pueden ser personas, pacientes, organizaciones sociales o instituciones públicas).
● Mediante una función, a todos los usuarios se les creará una cuenta automáticamente.
● Asigne una contraseña para cada cuenta. La contraseña debe ser creada con random y debe
cumplir con los siguientes criterios: mayúsculas, minúsculas y números.
● Cada cuenta debe guardarse en una nueva variable con su respectiva contraseña.
● Por cada cuenta debe pedir un número telefónico para contactarse
 El programa no terminará de preguntar por los números hasta que todas las organizaciones
tengan un número de contacto asignado.
● El programa debe verificar que el número telefónico tenga 8 dígitos numéricos.
● Se debe guardar como un string.
A modo de entrega, se debe disponer un documento Word o PDF en el que se indique:
- Ruta del repositorio en GitHub
Consideraciones adicionales
- El código debe estar debidamente indentado """



import time
import random
import string
print(string.ascii_letters)


nombres = ["jjvv cordillera","jjvv baron","jjvv ramaditas","jjvv playa ancha","jjvv san roque", "jjvv lecheros","jjvv monjas","jjvv concepción", "jjvv polanco", "jjvv carcel "]

usuarios = {}

#generar contraseña
def GeneraPassword(nombre):
    caracteres = 8
    for i in range(len(nombres)):
        password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(caracteres))
        return password
#validar telefono
def ValidaTelefono(telefono):
    telefono = input(f"ingrese numero telefonico del usuario {nombre}: ")
    if len(telefono) == 8:
        print("telefono válido\n")
        time.sleep(0.5)
        return telefono
    else:
        print("contener 8 caracteres. Intente nuevamente\n")
        time.sleep(1)
        ValidaTelefono(telefono)


# Programa Principal
for nombre in nombres:
    password = GeneraPassword(nombre)
    telefono = ValidaTelefono(nombre)

    values = [password, telefono]
    usuarios.setdefault(nombre,values)

print(f"JJVV     |    CONTRASEÑA   |   TELEFONO")
for x, y in usuarios.items():
  print(f"{x} : {y}")
