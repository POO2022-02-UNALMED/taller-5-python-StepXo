from zooAnimales.animal import Animal

class Reptil(Animal):
    listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola) :
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil.listado.append(self)
    

    @classmethod
    def cantidadReptiles(cls): return len(Reptil.listado)

    def movimiento(self, ):return "reptar"

    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        Reptil.iguanas+=1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)
    
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        Reptil.serpientes+=1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)
    

    #getters y setters
    def getColorEscamas(self) :return self._colorEscamas
    def setColorEscamas(self, colorEscamas) :self._colorEscamas = colorEscamas

    def getLargoCola(self) :return self._largoCola
    def setLargoCola(self, largoCola) :self._largoCola = largoCola

