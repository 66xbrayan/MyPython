#Variables

my_variable = "My String Variable"
print(my_variable)
print(len(my_variable))

my_int_variable = 2
print("int: ", my_int_variable)

my_int_to_str = str(my_int_variable)
print(my_int_to_str)
print(type(my_int_to_str))


my_bool_var = False
print(my_bool_var)


#concatenación de variables  en un print
print(my_variable, my_int_variable, my_bool_var)
print("Este es el valor:", my_bool_var)


#funciones de python

#contar longitud
print(len(my_variable))

#Variables en una sola linea. CUIDADO CON EL ABUSO DE SINTAXIS!! 

name, lastname, age = "Bry", "Ortega", 18

print("Mi nombre es:", name, lastname, ". Mi edad es:", age)

#input
#se esta reasignando el valor de las variables
"""
name = input('What is your name: ')
age = input('How old are you? ')

print(name)
print(age)
"""

#cambiamos su tipo
name = 33
age = "Bryan"
print(name)
print(age)

# ¿¿¿Forzar tipado???
address: str = "be@hotmail.com"
address: int = 32 
print(type(address))
