class Persona():

    def __init__(self, nombre, edad, dni):
        # se usa __ para determinar que un atributo es privado
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
# Se usa el @Property, siendo su equivalente en java al obtener
    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def dni(self):
        return self.__dni

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @dni.setter
    def dni(self, dni):
        self.__dni = dni


    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    def __str__(self):
        cadena = "-----------------------------------------------\n"
        cadena = cadena + "Nombre: {}\nCédula de identidad: {}\nEdad de la persona: {}\n".format(str(self.__nombre)
                                                                                        ,str(self.__dni)
                                                                                        , str(self.__edad))
        return cadena

nombre = input("Ingrese el nombre de la persona: ")
edad = input("Ingrese la edad de la persona: ")
id = int(input("Ingrese el número de cédula de la persona: "))
a = Persona (nombre, edad, id)
print(a)

