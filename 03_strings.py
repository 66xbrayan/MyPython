#Strings

my_string = "Mi cadena"
my_other_str = 'Mi otra cadena'

print(len(my_string))
print(len(my_other_str))

print(my_string+ " "+ my_other_str)

my_new_line_str="este es un str \ncon salto de linea"
print(my_new_line_str)

my_tab_str="\tEste es un str con tabulación"
print(my_tab_str)

my_scape_str="\\t Este es un str con \\n escapado"
print(my_scape_str)

#Formateo

name, lastname, age = "Bry", "AN", 33

#Esta es la manera más eazy
print("My name is {} {} and i am {}".format(name, lastname,age)) #<-------para formatear
print("My name is %s %s and i am %d" %(name, lastname,age))

print(f"My name is {name} {lastname} and i am {age}") #La mejor manera

#Más asquerosa
print("My name is "+name + " " + lastname + " and i am "+str(age))

#Desempaquetado de caracteres
language = "Python"
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)

#División NO ENTIENDO MUCHO

language_slice=language[1:3] #Da las letras contando 1 y sin contar 3 (como un intervalo)
print(language_slice)

language_slice=language[-2] #da la letra de atrás para delante
print(language_slice)

language_slice=language[1] #Pilla todo menos la posición 0
print(language_slice)



#Reverse

reversed_language=language[::-1]
print(reversed_language)

#Funciones

print(language.capitalize()) #Poner primera letra mayuscula
print(language.upper()) #Poner todo en mayus
print(language.count("t"))  #la palabra cuenta con esa letra
print(language.isnumeric()) #la palabra es un numero?? False
print("1".isnumeric()) #1 es un numero?? True
print(language.lower()) #palabra en minuculas
print(language.upper().isupper()) #poner mayuscula y comprobar si es mayuscula, True
print(language.startswith("pyt")) #para saber si la palabra empieza con tales letras, tienen valor si estan o no en mayusculas, en este caso esta False