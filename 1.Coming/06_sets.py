#SETS: No son una estructura ordenada y no admite repetidos

my_set = set()
print(type(my_set))
my_other_set = {}
print(type(my_other_set)) #Inicialmente es un dictionary

my_other_set = {"Bry", "Ortega", 44}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Testiando")
print(my_other_set) #no es una estructura ordenada 
my_other_set.add("Testiando") #no admite repetidos
print(my_other_set)

print("Bry" in my_other_set) #Realizar busquedas
print("Brian" in my_other_set)

my_other_set.remove("Bry")
print(my_other_set)

my_other_set.clear() #Limpiar
print(my_other_set)
print(len(my_other_set))

del my_other_set #3liminar

my_set = {"Bry","Ortega", 33}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"UFC", "WWE", 22}
my_set_2 = {44, 66}
my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_set_2).union({"JS", "PY"}))

print(my_new_set.difference(my_set))