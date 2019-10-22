#en este programa multiplicaremos los numeros que el usuario introduzca
def multiplicacion():
       a=input ("Introduzca un numero: ")
       b=input ("Intoduzca otro numero: ")
       c=input ("Introduzca otro numero: ")
       d=input ("Introduzca otro numero: ")
       i=a*b*c*d
       if(a==0):
              print "i= ",i , "su producto es 0"
       else:
              if(b==0):
                     print "i= ",i , "su producto es 0"
              else:
                     if(c==0):
                            print "i= ",i , "su producto es 0"
                     else:
                            if(d==0):
                                   print "i= ", i , "su producto es 0"
                            else:
                                   print "i= ", i
              
       
              
       
multiplicacion() 
