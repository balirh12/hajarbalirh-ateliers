# Programme Python pour l'implémentation du Tri à bulle
 
def tri_bulle(tab):
    number = len(tab)
    for i in range(number):
        for j in range(0, number-i-1):
            if tab[j] > tab[j+1] :
                tab[j], tab[j+1] = tab[j+1], tab[j]



tab=list(input("veuillez saisir les elements d'un tablau"))
tri_bulle(tab)

 
print ("Le tableau trié est:")
for i in range(len(tab)):
    print (tab[i])

