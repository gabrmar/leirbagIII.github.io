print("Bienvenido al código de prueba para estudios de repositorio Git")
print("Este es el primer cambio que realizaremos en el código")
x1 = 3
x2 = 5
y1 = 4
y2 = 5
m = (x2-x1)/(y2-y1)
print("El valor de la pendiente de la recta es {a}".format(a=m))
print ("Imprimiendo nuevos valores")
print(x1,x2,y1,y2,m)
b = y1 - m*x1
print("El valor del intercepto en el eje Y es {}".format(b))
print("La ecuación de la recta es y = {m}x + {b}".format(m=m,b=b))

print("El próximo paso será probar uno de los puntos con la ecuación de la recta")
