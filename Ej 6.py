def calculadora():
       a=input("Escribe un numero ")
       b=input("Escribe otro numero ")
       o=raw_input("Escribe la operacion que desea hacer ")
       if(o=="s"):
              print "el resultado es ", a+b
       if(o=="r"):
              print "el resultado es ", a-b
       if(o=="m"):
              print "el resultado es ", a*b
       if(o=="d"):
              print "el resultado es", a/b
calculadora()

