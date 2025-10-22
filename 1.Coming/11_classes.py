#Classes

class MyEmptyPerson:
    pass
"""
class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

my_person = Person("Brayan", "Estiven")
print(f"{my_person.name} {my_person.lastname}")
"""

class Person:
    def __init__(self, name, lastname, nickname="Sin apodo"):
        self.full_name = f"{name} {lastname} ({nickname})" #propiedad pública
        self.__name = name #Propieda privada con el __

    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        self.__name = new_name

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Bry", "Ortega")

print(my_person.full_name)

my_person.walk()

print("#", my_person.get_name()) #Para obtener el nombre guardado en name "privado"

my_other_person = Person("Kakashi", "Hatake", "El ninja que copia")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Sasuke Uchiha" #Cambie el fullname sencillo
print(my_other_person.full_name)

my_other_person.__name = "Rex" #Acá pensé que cambie el name "Privado" pero solo cree uno nuevo ya que python le cambia el nombre internamente
print(my_other_person.__name)
my_other_person.set_name("Riuk") #Utilizando el setter si se puede establecer otro nombre en name del init

print(my_other_person.__dict__) #Para ver el valor de los atributos de las variables de my_other_person
