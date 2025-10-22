#CRUD 2

class Crud:
    #CONSTRUCTOR
    def __init__(self, id = None, user = "", mail = "", password = "" ):
        self.id = id
        self.user = user
        self.mail = mail
        self.password = password
        self.db = []
    #MENU
    def menu_crud(self):
        print("CRUD by Bry")
        value = None
        while type(value) != int or 1 < value or value > 5 :
            try:
                print("Put: 1.Create, 2.Read, 3.Update, 4.Delete and 5.Exit")
                value = int(input())
                if 1 <= value <= 5:
                    break
            except Exception as error:
                print(error)
        if value == 1:
            self.create_crud()
        elif value == 2:
            self.read_crud()
        elif value == 3:
            self.update_crud()
        elif value == 4:
            self.delete_crud()
        elif value == 5:
            print("Finished execution")
    #CREATE
    def create_crud(self):
        print("CREATE USER:")
        print("Ingresa un ID")
        while type(self.user) != int:
            try: 
                self.id = int(input())
                break
            except Exception as error:
                print(error)
        #USER
        print("Ingresa un usuario")
        self.user = input()
        #EMAIL
        print("Ingresa un email")
        self.mail = input()
        while "@" and ".co" not in self.mail:
            print("Ingrese un email valido con @ y dominio")
            self.mail = input()
        #PASSWORD
        print("Ingresa una contraseña (Min. 8 caractres)")
        self.password = input()
        while len(self.password) < 8:
            print("La contraseña debe tener como minimo 8 caracteres")
            self.password = input()

        print("Confirma la contraseña")
        confirm_password = input()
        while self.password != confirm_password:
            try:
                while confirm_password != self.password or len(self.password) < 8:
                    print("(Contraseña invalida) La contraseña debe tener como minimo 8 caracteres y deben coincidir")
                    self.password = input()
                    print("Confirma la contraseña")
                    confirm_password = input()
                    if confirm_password == self.password:
                        break
            except:
                print("Las contraseñas no coinciden")
        self.db.append({
            "ID":self.id,
            "USER":self.user,
            "EMAIL":self.mail,
            "PASSWORD":self.password
        }
        )
        print("User created successfully", self.db)
        self.menu_crud()
    #READ
    def read_crud(self):
        print("READ USER")
        print(f"ID: {self.id} USER: {self.user} EMAIL: {self.mail} PASSWORD: {self.password}")
        self.menu_crud()
    #UPDATE
    def update_crud(self):
        print("UPDATE USER")
        if self.id == None:
            print("ERROR: First must create an user")
            self.create_crud()
        print("¿Qué desea editar? 1.ID, 2.USER, 3.EMAIL, 4.CONTRASEÑA")
        value = None
        while type(value) != int:
            try:
                value = int(input())
            except Exception as error:
                print(error)

            if 1 <= value <= 4:
                break
        #UPDATE ID
        if value == 1:
            print(f"ID ACTUAL:{self.id}")
            print("Ingresa un nuevo ID")
            while type(self.user) != int:
                try: 
                    self.id = int(input())
                    break
                except Exception as error:
                    print(error)
                self.menu_crud()
        
        #UPDATE USER
        if value == 2:
            print(f"USER ACTUAL:{self.user}")
            print("Ingresa un nuevo usuario")
            self.user = input()
            self.menu_crud()

        #UPDATE MAIL 
        if value == 3:
            print(f"EMAIL ACTUAL:{self.mail}")
            print("Ingresa un email")
            self.mail = input()
            while "@" and ".co" not in self.mail:
                print("Ingrese un email valido con @ y dominio")
                self.mail = input()
            print(f"New email, updated successfully {self.mail}")
            self.menu_crud()


        #UPDATE PASSWOORD
        if value == 4:
            print(f"CURRENTLY PASSWORD: {self.password}")
            print("Ingresa una nueva contraseña (Min. 8 caractres)")
            self.password = input()
            while len(self.password) < 8:
                print("La contraseña debe tener como minimo 8 caracteres")
                self.password = input()
            print("Confirma la contraseña")
            confirm_password = input()
            while self.password != confirm_password:
                try:
                    while confirm_password != self.password or len(self.password) < 8:
                        print("(Contraseña invalida) La contraseña debe tener como minimo 8 caracteres y deben coincidir")
                        self.password = input()
                        print("Confirma la contraseña")
                        confirm_password = input()
                        if confirm_password == self.password:
                            break
                except:
                    print("Las contraseñas no coinciden")

            print(f"New password, updated successfully {self.password}")
            self.menu_crud()
    #DELETE
    def delete_crud(self):
        print("DELETE USER")
        print("¿Está seguro de qué desea eliminar el user? 1.Sí, 2.No")
        value = None
        if self.id == None:
            print("Si no tienes datos no puedes borrar nada")
            self.menu_crud
        while type(value) != int or 1 < value or value > 2:
            try:
                value = int(input())
            except Exception as error:
                print(error)

            if 1 <= value <= 2:
                break
        if value == 1:
            self.db.clear()
            print(self.db)
            self.menu_crud()

        elif value == 2:
            self.menu_crud()

my_crud2 = Crud()
my_crud2.menu_crud() 