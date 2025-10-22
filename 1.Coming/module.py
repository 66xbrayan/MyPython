# ejemplo de FICHERO con funciones

def sumValues (num1, num2):
    try:
        result = (num1+num2)
        print(f"La suma de {num1} + {num2} es:", result)

    except Exception as errors:
        print(errors)
    finally:
        print("Execution continue")

def printValues (value):
    print(f"{value}") #Solo formatea a str datos como bool, int, float
