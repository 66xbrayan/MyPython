#crud
class Crud:
    
    
    #CONSTRUCTOR
    def __init__(self, id=None, article="", price=None):
        self.id = id
        self.article = article
        self.price = price
        self.db = []

    #CREATE
    def create(self):
    
        while type(self.id) != int:
            print("ID: (MUST TO BE A INTEGER)")
            self.id = (input())
            try:
                self.id = int(self.id)
            except ValueError as error:
                print(error)
            if type(self.id) == int:
                print("Enter article's name: ")
                self.article = input()
                break

        while type(self.price) != int:
            print("PRICE: (DON´T PUT $)")
            self.price = (input())
            try:
                self.price = int(self.price)
            except ValueError as error:
                print(error)
            if type(self.price) == int:
                break
        print(f"id: {self.id} - name: {self.article} - price: ${self.price} ")

        self.db.append({
            "ID": self.id,
            "Article": self.article,
            "Value $$$": self.price
        })

        print(self.db)
        self.menu()


    #READ
    def read(self):
        print("OP: READ")
        print(f"ID: {self.id} Article's Name: {self.article} and its value is ${self.price}")
        print(self.db)
        self.menu()
        #HACER UN QUE QUIERES VER CON CICLO FOR wip

    #UPDATE
    def update(self):
        print("Qué quieres editar?: (Pon 1 para id, 2 para el nombre del articulo y 3 para precio)")
        value = 0
        while value < 1 or value > 3:
            try:
              print("INGRESA: ")
              value = int(input())
                
            except Exception as error:
                print(error)
                print("Número debe ser entre 1 y 3")
            
            if 1 <= value <= 3:
                if value == 1:
                    self.id = None
                    while type(self.id) != int:
                        try:
                            print("INGRESA NUEVA ID:")
                            self.id = (input())
                            self.id = int(self.id)
                        except ValueError as error:
                            print(error)
                    if type(self.id) == int:
                        print(f"ID EDITED SUCCESSFULLY: {self.id}")
                        print(f"ID: {self.id} Article's Name: {self.article} and its value is ${self.price}")

                        break
                    
                if value==2:
                    print("Enter article's name: ")
                    self.article = input()
                    print(f"ARTICLE EDITED SUCCESSFULLY: {self.article}")
                    print(f"ID: {self.id} Article's Name: {self.article} and its value is ${self.price}")
                    break
  
                if value == 3:
                    self.price = None
                    while type(self.price) != int:
                        try:
                            print("INGRESA NUEVO PRECIO:")
                            self.price = (input())
                            self.price = int(self.price)
                        except ValueError as error:
                            print(error)
                    if type(self.price) == int:
                        print(f"PRICE EDITED SUCCESSFULLY: {self.id}")
                        print(f"ID: {self.id} Article's Name: {self.article} and its value is ${self.price}")

                        break
        self.menu()

    #DELETE
    def delete(self):
        print(f"Eliminar producto: id: {self.id} - name: {self.article} - price: ${self.price} ")
        self.db.clear()
        print(self.db)
        print("ELIMINADO")
        self.menu()
   
   #MENÚ
    def menu(self):
        #print("CRUD - BY BRAYAN")
        #print("¿Qué querés hacer hoy?")
        #print("Recuerda:")
        print("1.Crear nuevo producto en la DB, 2.Ver producto, 3.Actualiza informción del producto ")
        print("4.Eliminar Producto y 5.SALIR")

        answer = 0
        while answer < 1 or answer > 5:
            
            try:
              print("INGRESA: ")
              answer = int(input())
                
            except Exception as error:
                print(error)
                print("Número debe ser entre 1 y 5")
            
            if 1 <= answer <= 4:
                if answer==1:
                    self.create()
                  
                    break
                    
                if answer==2:
                    self.read()
                 
                    break
                        
                if answer==3:
                    self.update()
                        
                if answer==4:
                    self.delete()
                   
                    break
                if answer==5:
                    print("EJECUCIÓN FINALIZADA")
                    break
                    

my_crud = Crud()
my_crud.menu()