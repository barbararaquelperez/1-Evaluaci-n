def primo():
       numero=input ("say me your number ")
       primo=True
       for i in range(1, numero):
              for p in range (2,i-1):
                     if(i%p==0):
                            primo=False
              if (primo==True):
                     print "i= ", i, "es primo"
              else:
                     print "i= ", i, "no es primo"
              primo=True 
primo() 
