def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
 fibonacci_recursivo(5)
#De acuerdo al teorema del Maestro este algoritmo tiene una complejidad de O(logn) ya que primero "a" tiene una cantidad de llamados recursivos de 2, después n/b es igual a n
#por lo tanto b=5/3 y finalmente tenemos que O(1) ya que las operaciones son en tiempo constante, por lo tanto c=0
#Finalmente sustituyendo tenemos que O(n^log1(2)).

