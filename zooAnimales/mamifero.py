from zooAnimales.animal import Animal

class Mamifero:

    listado = []
    caballos = 0
    leones = 0
    

    def __init__(self,nombre,edad,habitat, genero, pelaje, patas):
        Animal.__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.listado.append(self)


    @classmethod
    def cantidadMamiferos(cls):return len(Mamifero.listado)

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        Mamifero.caballos+=1
        return Mamifero(nombre,edad,"pradera",genero,True,4)
    
    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        Mamifero.leones+=1
        return Mamifero(nombre,edad,"selva",genero,True,4)
    

    #getters y setters

    def getPatas(self) :return self._patas
    def setPatas(self, patas) :self._patas = patas

    def isPelaje(self) :return self._pelaje
    def setPelaje(self, pelaje) :self._pelaje = pelaje

