#notación asintótica
#Solo importa el número más grande

#Ley de la suma
def f(n):  
    for i in range(n):
        print(i)
    
    for i in range(n):
        print(i)
#O(n) + O(n*n) = O(n+n2) = O(n2)

#Ley de la  multiplicación
def f(n):

    for i in range(n):
        for j in range(n):
            print(i,j)
#O(n) * O(n) = O(n*n) = O(n2)

#Recursividad multiple
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return (fibonacci(n-1) + fibonacci(n-2))
#O(2**n)

#Clases de complejidad algorítmica
#O(1) Constante
#O(n) Lineal
#O(log n) Logarítmica
#O(n log n) Log lineal
#O(n**2) Polinomial
#O(2**n) Exponencial