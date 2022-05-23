print("OPERADORES")
print("EJERCICIO 1")
print("Area de un triángulo")
base = float(input("Valor de la base: \n"))
altura = float(input("Valor de la altura: \n"))
area = base * altura / 2
print("El area del triángulo es: " + str(area))

print("EJERCICIO 2")
print("Sumar dos digitos")
n1 = float(input("Agrega cualquier número: \n"))
n2 = float(input("Agrega un segundo número: \n"))
suma = n1 + n2
print("resultado de la suma: " + str(suma))

print("EJERCICIO 3")
print("Número al cuadrado")
n1 = float(input("Ingresa un número: \n"))
nac = n1 * n1
print("Resultado: " + str(nac))

print("EJERCICIO 4")
print("De Euro a Dolar")
Euro = float(input("Valor de Euro: \n"))
Dolar = 1.06
convertir = Euro * Dolar
print("valor de Dolar: " + str(convertir))

print("EJERCICIO 5")
print("Lado de un cuadrado con área y perímetro")
lado = float(input("medida del lado: \n"))
área = lado * lado
perímetro = lado * 4
print("area: " + str(área))
print("perímetro: " + str(perímetro))

print("EJERCICIO 6")
print("Área del cilindro")
r = float(input("escriba el valor del radio: \n"))
h = float(input("escriba el valor de la altura: \n"))
área = 3.1416 * r * r
volumen = 3.1416 * h * r * r
print("área: " + str(área))
print("volumen: " + str(volumen))

print("EJERCICIO 7")
print("Longitud y área de una circunferencia")
r = float(input("escriba el valor del radio: \n"))
L = 2 * 3.1416 * r
A = 3.1416 * r * r
print("Longitud: " + str(L))
print("área: " + str(A))

print("EJERCICIO 8")
print("calcular promedio de 3 números ingresados por teclado")
pn = float(input("ingrese un número aleatorio: \n"))
sn = float(input("ingrese un número aleatorio: \n"))
tn = float(input("ingrese un número aleatorio: \n"))
prom = pn + sn + tn / 3
print("el promedio es: " + str(prom))

print("CONDICIONALES")
print("EJERCICIO 1")
print("Algoritmo para determinar números positivos y negativos")
número_como_cadena = input("escribe un número: \n")
número = float(número_como_cadena)
if número == 0:
    print("neutro")
elif número < 0:
    print("negativo")
else:
    print("positivo")

print("EJERCICIO 2")
print("Determinar que numero es mayor y cual es menor")

numeros = []
for i in range(2):
    numero = float(input("Introduce el número: ".format(i + 1)))
    numeros.append(numero)

mayor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero
menor = numeros[0]
for numero in numeros:
    if numero < menor:
        menor = numero

print("Mayor:", mayor)
print("Menor", menor)

print("EJERCICIO 3")
print("Numero mayor y menor")
numbers = []
for i in range(3):
    numero = float(input("Introduce un número: ".format(i + 1)))
    numbers.append(numero)

menor = numbers[0]

for numero in numbers:
    if numero < menor:
        menor = numero

mayor = numbers[0]

for numero in numbers:
    if numero > mayor:
        mayor = numero

print("Mayor:", mayor)
print("Menor:", menor)

print("EJERCICIO 4")
print("sumar si A es menor que B o restar si es lo contrario")

A = int(input("inserte un número A: \n"))
B = int(input("inserte un número B: \n"))

if (A <= B):
    print("Suma:" + str(A + B))
else:
    if (A >= B):
        print("Resta:" + str(A - B))

print("EJERCICIO 5")
print("Hallar el cosiente entre A y B")
dividiendo = float(input("ingrese un numero: \n"))
divisor = float(input("ingrese un numero: \n"))

if divisor == 0:
    print("No es posible dividir por 0")

else:
    if divisor > 0:
        print("resultado: " + str(dividiendo / divisor))

print("EJERCICIO 6")
print(
    "Dos números A y B, sumarlos si al menos uno de ellos es negativo, en caso contrario multiplicarlos."
)
N1 = int(input("inserte un numero: \n"))
N2 = int(input("inserte un numero: \n"))

if ((N1 < 0) or (N2 < 0)):
    print("la resta seria: " + str(N1 + N2))
else:
    if ((N1 > 0)) and (N2 > 0):
        print("resultado: " + str(N1 * N2))
#jfguuyfdguf
print("EJERCICIO 7")
print("Un algoritmo que determine si un año es bisiesto o no.")
año = int(input("digite el año: \n"))
if (año % 4 == 0 and (año % 100 != 0)) or (año % 400 == 0):
    print("Año:", str(año) + "es biciesto")
else:
    print("Año:", str(año) + "No es biciesto")

print("CICLOS")
print("EJERCICIO 1")
print("Imprimir todos los múltiplos de 3 que hay entre 1 y 100")
resultado = 0
while resultado < 98:
    resultado += 3
    print(resultado)

print("EJERCICIO 2")
print("Imprimir los números impares entre 0 y 100")
numero = 1
while numero < 100:
    numero += 2
    print(numero)

print("EJERCICIO 3")
print("Imprimir los números pares del 1 al 100")
numero = 0
while numero < 100:
    numero += 1
    print(numero)

print("EJERCICIO 4")
print("cuadrados de los números del 1 al 30")
for numero in range(1, 31):
    numero = numero**2
    print(numero)

print("EJERCICIO 5")
igual = 0
print("numeros al cuadrado sumados")
for numero in range(1, 101, 1):
    numero = numero**2
    igual = igual + numero
    print(igual)

print("EJERCICIO 7")
print(
    "Suma de todos los números que se digitan por teclado mientras no sea cero"
)
a = 1
y = 0
while a != 0:
    x = int(input("digite los numeros: \n"))
    if x == 0:
        a = 0
    else:
        y = y + x
    print(y)
