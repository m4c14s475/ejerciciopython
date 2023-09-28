"""
Ejercicio 4
Los teléfonos de una empresa tienen el siguiente formato prefijo-localidad-numero 
donde el prefijo es el código del país +54, 
y la extensión tiene dos dígitos (por ejemplo +54-11-37247101). 

Escribir un programa que pregunte por un número de teléfono con este formato 
y muestre por pantalla el número de teléfono sin el prefijo y ni la localidad.
"""

tel=input("ingreso el numero telefonico: XX-XX-XXXXXXXX: ")
print("Su telefono sin prefijo ni localidad es : ",tel[4:12])

