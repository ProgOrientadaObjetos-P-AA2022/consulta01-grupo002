class Persona():

    def __init__(self, nombre, edad, titulacion, nota):
        # se usa __ para determinar que un atributo es privado
        self.__nombre = nombre
        self.__edad = edad
        self.__titulacion = titulacion
        self.__nota = nota
# Se usa el @Property, siendo su equivalente en java al obtener

    @property
    def nota(self):
        return self.__nota
    @nota.setter
    def nota(self, nota):
        self.__nota = nota
    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def titulacion(self):
        return self.__titulacion

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @titulacion.setter
    def dni(self, titulacion):
        self.__dni = titulacion


    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    def __str__(self):
        cadena = "-----------------------------------------------\n"
        cadena = cadena + "Nombre de Profesional: {}\n" \
                          "Edad: {}\n" \
                          "Titulacion: {}\n" \
                          "Nota de Graduación: {}\n".format(str(self.__nombre)
                                                     , str(self.__edad)
                                                     , str(self.__titulacion)
                                                     , str(self.__nota))
        return cadena

a = Persona ("María Valladares", 22, "Bióloga Marina", 9.81)
b = Persona ("María Valladares", 22, "Bióloga Marina", 9.81)
c = Persona ("María Valladares", 22, "Bióloga Marina", 9.81)
print(a)
print(b)
print(c)