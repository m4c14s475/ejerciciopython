"""
Ejercicio 11
Escribir un programa que pregunte 
el nombre el un producto, 
su precio y 
un número de unidades 

y muestre por pantalla una cadena con el nombre del producto 
seguido de su precio unitario con 6 dígitos enteros y 2 decimales, 
el número de unidades con tres dígitos y 
el coste total con 8 dígitos enteros y 2 decimales.
"""

producto=input("por favor ingrese el nombre del producto : ")
precio  =float(input("por favor ingrese el precio del producto : "))
unidades=int(input("por favor ingrese la cantidad de unidades: "))
total=precio*unidades

print("El producto es: ",producto,", \n(forma1) su valor es $ ",round(precio,2),
      "\n(forma2) su valor es $",format(precio, '0.2f'),"\ny adquirio ",
      format(unidades,'3.0f'),"unidades. \nEl total de su compra es de :",format(total,'8.2f'))
