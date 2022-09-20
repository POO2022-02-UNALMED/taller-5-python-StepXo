class Animal:
    _totalAnimales=0
    
    def __init__(self, nombre, edad, habitat, genero, zona=None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal._totalAnimales += 1


    def movimiento(self): return "desplazarse"

    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.reptil import Reptil
        from zooAnimales.ave import Ave
        from zooAnimales.pez import Pez
        return "Mamiferos : " + str(Mamifero.cantidadMamiferos()) + "\nAves : " + str(Ave.cantidadAves()) + "\nReptiles : " + str(Reptil.cantidadReptiles()) + "\nPeces : " + str(Pez.cantidadPeces()) + "\nAnfibios : " + str(Anfibio.cantidadAnfibios())
    

    def toString(self):
        if self.zona != None:
            return "Mi nombre es " + self.nombre + ", tengo una edad de " + str(self.edad) + ", habito en " + self.habitat + " y mi genero es " + self.genero + ", la zona en la que me ubico es " + self.zona.getNombre() + ", en el " + self.zona.getZoo().getNombre()
        else:
            return "Mi nombre es " + self.nombre + ", tengo una edad de " + str(self.edad) + ", habito en " + self.habitat + " y mi genero es " + self.genero
        
    

    #getters y setters
    def getNombre(self):return self._nombre
    def setNombre(self, nombre):self._nombre = nombre

    def getEdad(self):return self._edad
    def setEdad(self, edad):self._edad = edad

    def getGenero(self):return self._genero
    def setGenero(self, genero):self._genero = genero

    def getHabitat(self):return self._habitat
    def setHabitat(self, habitat):self._habitat = habitat


