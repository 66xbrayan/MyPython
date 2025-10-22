#Dictionaries
my_dict = dict()
print(type(my_dict))
my_other_dict = {}
print(my_other_dict)

my_other_dict = {"Name":"Bry", "Lastname":"Ortega", "Edad":33, 1: "Python"}

my_dict = {
    "Name":"Bry",
    "Lastname":"Ortega",
    "Age":33,
    "Lang":{"Python", "JS", "C++"},
    1 : 444
    }

print(my_dict)
print(my_other_dict)

print(len(my_dict))
print(len(my_other_dict))
print(len(my_dict["Lang"]))

my_dict["Name"] += "an"
print(my_dict["Name"])

print(my_dict[1])

my_dict["ID"] = "1385970" # AÑADIR CLAVE Y VALOR
print(my_dict)

del my_dict["ID"] #Borrar clave
print(my_dict)

print("Name" in my_dict) #Busca la clave
print("Namee" in my_dict) #Busca la clave

print("Ortega" in my_dict.values()) #Buscar este valor en el dict
print("Ortegaa" in my_dict.values()) #Buscar este valor en el dict

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["name", "lastname", "age"]

my_new_dict = dict.fromkeys((my_list))
print((my_new_dict))

my_new_dict = dict.fromkeys(("name", "lastname", "age"))
print((my_new_dict))

my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))

my_new_dict = dict.fromkeys(my_dict, "BRY")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print("HEYYY: ",(list(dict.fromkeys(list(my_new_dict.values())).keys()))) #SE LE PUEDE QUITAR EL VALUES PARA QUE QUEDE CON LAS CLAVES
print( tuple(my_new_dict))
print(set(my_new_dict))