def fibonacci(n):
    if(n <= 1):
        return n
    else:
    # la récursivité
        return (fibonacci(n-1) + fibonacci(n-2))
n = int(input("Entrez le nombre de termes:"))
print("Suite de Fibonacci :")
for i in range(n):
    # résultat 
    print(fibonacci(i))