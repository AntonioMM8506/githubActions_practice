#Polimorfismo

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        
def avanza(self):
    print("Ando caminando")

#En el caso del polimorfismo en Python, no es necesario incluir el @override como en java, por
#ejemplo, en este caso, solo basta con cambiar el desarrollo de la función. 
class Ciclista(Persona):

    def __init__(self, nombre):
        super.__init__(nombre)

    def avanza(self):
        print("Ando moviendome en bicicleta")


def main():
    persona = Persona("Antonio")
    persona.avanza()

    ciclista = Ciclista("Julian")
    ciclista.avanza()

if __name__ == "__main__":
    main()