#LOOPS

#While
my_con = 10
while my_con < 10:
    print(my_con)
    my_con += 1
if my_con == 15:
    print("VALOR = 10")
else: #OPCIONAL PONER ELSE
    print("El valor es mayor o igual que 10")

while my_con < 20:
    my_con += 1
    print(my_con)
    
    if my_con ==15:
        print("My condition is 15")
        break
print(my_con)

print("La ejecución continúa")

#For

my_list = [99, 33, 111, 44]
for element in my_list:
    print(element)

my_tuple = (33, "Bry", 2007)
for element in my_tuple:
    print(element)

my_set = {"22", 44, "ESTIVEN"}
for element in my_set:
    print(element)

my_dict = {"name":"Bry", "lastname":"Soto", "age":20, "id": 2244}
for element in my_dict:
    print(element)
    if element == "age":
        continue 
    print("Se ejecuta")

else:
    print("Finalizó el ciclo for")

print("La ejecución continúa")
