def cantidad():
    a=input("Numero entero: ")
    b=raw_input("Introduce una palabra: ")
    print (len(b))
    if (a==b):
        print "Enhorabuena campeon,tu palabra tiene el mismo n� de letras que tu numero entero"
    else:
        print "Intentalo otra vez, no conciden"
cantidad()
