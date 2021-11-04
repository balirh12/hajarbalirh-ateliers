def tri_insertion(tab): 
    for i in range(len(tab)): 
        k = tab[i] 
        j = i-1
        while j >= 0 and k < tab[j] : 
                tab[j + 1] = tab[j] 
                j -= 1
        tab[j + 1] = k
tab = list((input("Entrez un tableau separe par un espace:")))
tri_insertion(tab)
print ("Le tableau trié est:")
for i in range(len(tab)): 
    print ( tab[i])