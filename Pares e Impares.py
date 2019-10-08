def ejemplo_for():
    #i es una variable que toma los valores comprendidos en
    #el rango
    x=input("Hasta que numero: ")
    
    for i in range (1,x+1):
       if(i%2==0):
              print "i= ",i, "es par"
       else:
              print "i= ", i, "es impar"
        
ejemplo_for() 
