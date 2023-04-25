def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
 fibonacci_recursivo(5)
#Este algoritmo no puedo ser analizado con el teroema del Maestro ya que en primer lugar no se tiene un arreglo y termina en orden exponencial de acuerdo a la Big O.

