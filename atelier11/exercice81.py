def fequence(str,val):
       cmpt = 1
   
       for i in range(len(str)):
          if str[i]==val:
            cmpt+=1
       return cmpt
str = input("Entrez un chaine de caractere : ")
val=input("Entrez une lettre : ")
print("nombre d'accurance  est")
print(fequence(str,val)-1)