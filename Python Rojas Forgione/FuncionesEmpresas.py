def saludar ():
    print ("Hola")
    print ("Cómo estás?")
    print ("Un gusto verte")


def saludar (nombre):
    print ("Cómo estás?")
    print ("Un gusto verte")


def saludar (nombre, estado):
    print ("Hola" + nombre)
    print ("¿Cómo estás?")
    if estado == "bien":
          print ("Que lindo verte bien! ¿En qué más te puedo ayudar?")
    else:
        print ("¿En qué te puedo ayudar?")
        print ("Un gusto verte")


saludar (input("Escribe tu nombre:")),input("Escribe tu estado:(bien/mal)")


def saludar (nombre, apellido, empresa="Belgrano Day School"):
    print ("Hola" + nombre + apellido)
    print ("Bienvenidos a" + empresa)
    print ("Un gusto tenerte con nosotros")


saludar (nombre="Vir", apellido="He", empresa="Belgrano Day School")


