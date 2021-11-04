# Simple Function that reverse a string with Bracket
def inverser(str):
    length=len(str)
    for i in str:
        invstr=str[length::-1]
        return invstr
str = (input("Entrez une chaine de caractere: "))
print(inverser(str))