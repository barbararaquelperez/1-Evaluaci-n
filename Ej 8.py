def IVA():
       a=input ("Precio del producto ")
       b=raw_input ("Tipo de IVA ")
       if(b=="general"):
              print a+(a*0.16)
       if(b=="reducido"):
              print a+(a*0.07)
       if(b=="superreducido"):
              print a+(a*0.04)
IVA()


