#Functions

def my_func():
    print("Soy una función")

for i in range(3): #Usar el rango para que se repita for _ in range(3):
    my_func()
"""
my_func() #Para no usar esto puse el ciclo For i in range(3):
my_func()
my_func()
"""
def suma (num_1, num_2):
    print(num_1 + num_2)

suma(1,2)
suma(20, 400)
suma("5","5")
suma(334,777)

def suma_return (num_1, num_2): #Cuando la func tiene return el valor se le debe asignar a una VARIABLE
    my_sum = num_1 + num_2
    return my_sum

result = suma(4, 1) #LA FUNCION SUM NO TIENE RETURN POR LO TANTO ES DE VALOR NONE
print(result)

result = suma_return(19, 1) #SE LE ASIGNO A RESULT EN ESTE CASO
print(result)

def print_name(name, lastname):
    print(f"My name is {name} {lastname}.")

print_name("BRY", "AN")

def print_name_default(name, lastname, nickname = False):
    
    if nickname :
        message = print(f"{name} {lastname} and his nickname is {nickname}")
    else:
        message = print(f"His name is {name} {lastname} and he has not a nickname.")
        
    print(message)

print_name_default("Brayan", "Ortega") #PONER EL NICKNAME

def print_texts_upper(*texts):
    for text in texts:
        print(str(text).upper())
print_texts_upper("Hola bro", "Q más?", 44, True)
