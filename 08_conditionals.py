#Conditionals

my_condition = True
if my_condition == False: #Si no se pone el "==" se entiende que es True de primera
    print("SE EJECUTA LA CONDICIÓN DEL IF")

my_condition = 4*2
if my_condition == 8:
    print("Se ejecuta la condición del segundo IF")

my_condition = 25
if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25: 
    print("IGUAL A 25")
else:
    print("Es menor o igual que  que 10 y mayor que 20 o diferente a 25")

print("La ejecución continúa")

my_str = "99" #Cuando esta vacío es un false

if my_str: #esto es un if de true se puede negar tambien con un if not my_str:
    print("My string isn´t empty")

my_str = "" #Cuando esta vacío es un false

if not my_str: #se puede negar tambien con un if not my_str:
    print("My string is empty")