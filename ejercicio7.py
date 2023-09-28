"""
Ejercicio 7 
Escribir un programa que pregunte el correo electrónico del usuario en la consola 
y muestre por pantalla otro correo electrónico con el mismo nombre 
(la parte delante de la arroba @) pero con dominio alu.ar
"""

mail=input("por favor introduzca su mail : ")
mail=mail.lower()
print (mail.strip(),"@alu.ar")
