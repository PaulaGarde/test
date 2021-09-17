producto = str (input("Nombre producto: "))
cantidad = int (input("Numero de items: "))
precio = int (input("Ingresar Precios: "))
iva = int (input("Porcentaje del iva : "))

total = cantidad * precio
totaliva = total / (1+ (iva/100))
subtotal = total - totaliva

print (totaliva)
print (subtotal)
print (total)