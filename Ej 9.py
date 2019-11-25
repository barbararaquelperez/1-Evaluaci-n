#Este programa calculara el salario semanal de un trabajador
def salario():
    b=input ("Escribe las horas trabajadas en la semana: ")
    if(b>40):
            print "El salario de esta semana es: ", (40*30)+(b-40)*45, "euros"
    else:
        if(b<=40):
            print "El salario semanal es: ", b*30, "euros"
salario()
    
