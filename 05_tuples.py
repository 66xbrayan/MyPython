#Tuplas: SON INMUTABLES Y CONSTANTES

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (33, 1.77, "BRY", "AN")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-5]) IntdexError

print(my_tuple.count("BRY"))
print(my_tuple.index("AN")) #EL INDICE DONDE SE ENCUENTRA EL VALOR 

my_other_tuple = (144,22,3,45,54,66,777)
print(my_other_tuple)

sum_tuples = my_other_tuple+my_tuple
#sum_tuples.sort() #AttributeError 
print(sum_tuples)

#CAMBIAR DE TUPLA A LISTA PARA INSERTAR DATOS
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple.insert(1, "REAL MADRID")
my_tuple[3] = "LIL"
print(my_tuple)

my_tuple = tuple(my_tuple)
print(type(my_tuple))
print(my_tuple)

del my_tuple #Si se puede eliminar el DEL sirve para cualquier variable
#print(my_tuple) NameError: name 'my_tuple' is not defined