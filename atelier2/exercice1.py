def get_odds(list1, list2):
    a, b = [], [] 
    for i in range(0, len(list1)):
        if i % 2 != 0: a.append(list1[i])
    for j in range(0, len(list2)):
        if j % 2 == 0:  b.append(list2[j])
    return a + b

print(get_odds([1, 2, 3, 4, 5], [1, 2,  3]))