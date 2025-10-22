#Listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [3, 7, 9, 9, 0, 6, 5, 6, 44, 11]

print(len(my_list))

my_other_list = [33, 1.75, "Bry", "Ortega"]
print(type(my_other_list))
print(type(my_list))

print(my_list[0])
print(my_list[-1])
#print(my_other_list.count(input())) #Si cuenta con algo esta lista, se le digita por el input
#print(my_list.count(input("Que necesita??: "))) #solo recibe str
#print(my_list.count(int(input("Que necesita??: ")))) #Solo recibe numeros enteros
"""
x = input("Q necesita??: ") #Hacer el count que formatee los str en caso de que sean numeros
if x.isdigit():
    x = int(x)
print(my_other_list.count(x))
"""
age, height, name, lastname = my_other_list
print(age)

name, lastname, age, height = my_other_list[2], my_other_list[3], my_other_list[0], my_other_list[1]
print(height)

print(my_other_list+my_list)

my_other_list.append("Testiando")
print(my_other_list)

my_other_list.insert(1, "Violeta")
print(my_other_list)

my_other_list[1] = "Red"
print(my_other_list)

my_other_list.remove("Red")
print(my_other_list)

print(my_list)
my_list.remove(9)
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()#ordenar de menor a mayor
print(my_new_list)

print(my_new_list[2:3])

print(my_other_list.index("Ortega")) #EL INDICE DONDE SE ENCUENTRA EL VALOR 

my_list = "Hola Python" #El tipado se cambia facilmente, puede ser peligroso
print(my_list)
print(type(my_list))