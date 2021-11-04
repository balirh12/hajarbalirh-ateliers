#compter les chiffres d'un nombre
def compter(num) :
#condition d'arret
     if num<10 :
      return 1 
     else :
      return 1 + compter(num/10)\
#demander un nombre de l'utilisateur 
nbr = int(input("Entrez un nombre : "))
#afficher resultat
print(compter(nbr))
