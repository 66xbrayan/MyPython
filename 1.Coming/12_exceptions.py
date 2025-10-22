#Exception hangling

num_1 = 2
num_2 = 3
num_2 = "2"

#Try Except

try:
    print(num_2+num_1)
    print("Ningún error")
except TypeError as error:
    print("Error de tipo")

#Try Except Else Finally

try:
    print(num_2+num_1)
    print("Ningún error")
except TypeError as error:
    print("Error de tipo")
else: #Opcional--
    # Se ejecuta cuando no hay un error
    print("Continúa la ejecución")
finally: #Opcional--
    #Se ejecuta siempre
    print("sigue la ejecución")

# Exceptions by type, value or some error

try:
    print(num_1+num_2)
    print("Ningún error")
except ValueError as error:
    print(error)
except Exception as exception:
    print(exception)
