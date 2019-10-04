import math
def ecuacion(): 
    print "Introduzca los coeficientes del polinomio"
    print "A*X^2+B*X+C=0"
    a=input ("A= ")
    b=input ("B= ")
    c=input ("C= ")
    radicando=b*b-4*a*c
    if (radicando>=0):
        raiz1=(-b+(radicando)^1/2)/(2*a)
        raiz2=(-b-(radicando)^1/2)/(2*a)
        print "primera solucion = ", raiz1
        print "segunda solucion = ", raiz2
    else:
        print "error, no existe solucion real"

ecuacion()
