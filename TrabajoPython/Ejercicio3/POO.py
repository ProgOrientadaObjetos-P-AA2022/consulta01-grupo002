class Profesional:
    def __init__(self,titulacion,  edad, nombre, notaGraduacion, sexo):
        self.__titulacion = titulacion
        self.__edad = edad
        self.__nombre = nombre
        self.__notaGraduacion = notaGraduacion
        self.__sexo = sexo
    @property
    def titulacion(self):
        return self.__titulacion
    @property
    def edad(self):
        return self.__edad

    @property
    def dni(self):
        return self.__nombre
    @property
    def notaGraduacion(self):
        return self.__notaGraduacion
    @property
    def sexo(self):
        return self.__sexo

    @titulacion.setter
    def nombre(self, titulacion):
        self.__titulacion = titulacion

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre


    @notaGraduacion.setter
    def notaGraduacion(self, notaGraduacion):
        self.__notaGraduacion = notaGraduacion
    @sexo.setter
    def sexo(self):
        return self.__sexo

    def __str__(self):
        cadena = "-----------------------------------------------\n"
        cadena = cadena + "Nombre: {}\nTitulación: {}\nEdad del Profesional: {}\nNota de Graduacion: {}\nSexo: {}\n"\
            .format(str(self.__nombre)
                    ,str(self.__titulacion)
                    , str(self.__edad)
                    , str(self.__notaGraduacion)
                    ,str(self.__sexo))
        return cadena
a = Profesional("Ingeniera Ambiental", 22,"Graciela Aguirre", 8.91, "Femenino")

print(a)


