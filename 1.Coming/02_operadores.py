#Operadores Aritmeticos

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 2) #Es el residuo de la división
print(3 // 2) #floor division, aproxima el valor 
print(3 ** 3)
print(3 ** 3 + 2 - 7 / 2 // 8)

print("Hello"+"World")
print("Hello"+str(5))
print("hello"*3)
print("hello"*(3**5//3))
my_float = 2.5*2
print("Hey "* int(my_float))

#Operadores Comparativos

print(3>4) #mayor que F
print(3<4) #menor que T
print(3 <= 4) #menor o igual que T
print(3 >= 4) #mayor o igual que F
print(4 == 4) #verificar si son iguales T
print(3 != 4) #No es igual T
print(3>42) #F

#Comparar Strings con ordenación alfabetica por ASCII

print("hola" > "joke")
print("hola" < "joke")
print("hola" <= "joke")
print("hola" >= "joke")
print("hola" == "joke")
print("hola" != "joke")

print(len("hola") <= len("joke"))

#Operadores lógicos
print("-------------------------------------------")

print(3>4 and "hola">"joke")
print(3>4 or "hola">"joke")

print(3<4 and "hola"<"joke")
print(3<4 or "hola"<"joke" and 4==4)
print(3<4 and "hola">"joke" or 5!=4)

print(not("hola">"joke")) #negar la condición
