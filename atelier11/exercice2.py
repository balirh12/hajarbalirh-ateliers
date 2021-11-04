# Function convert Number to inversed Binary 
def binaire(nombre):
    if nombre > 1:
         # Start of Recursion 
        binaire(nombre // 2)
    print(nombre % 2,)
nombre = int(input("veuillez entrez un nombre en décimal: "))

binaire(nombre)

 