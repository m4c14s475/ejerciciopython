"""
Ejercicio 2
Escribir un programa que pregunte el nombre completo del usuario en la consola 
y después muestre por pantalla el nombre completo del usuario tres veces, 
una con todas las letras minúsculas, 
otra con todas las letras mayúsculas 
y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""

nom1=input("por favor ingrese su nombre nuevamente: ")

print("1: todas minusculas       :",nom1.lower())
print("2: todas mayusculsa       :",nom1.upper())
print("3: 1er letra en mayuscula : ",nom1.capitalize())


