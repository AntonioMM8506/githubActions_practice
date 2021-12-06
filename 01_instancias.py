class Coordenada:

    #Constructor de la clase
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Función para usar la clase
    def distancia(self, otra_coordendada):
        x_diff = (self.x - otra_coordendada.x)**2
        y_diff = (self.y - otra_coordendada.y)**2

        return (x_diff + y_diff)**0.5


if __name__ == '__main__':
    #crea 2 instancias del objeto. 
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    #usa la función previamente declarada a través del primer objeto 
    print(coord_1.distancia(coord_2))
    
    #Método que ayuda a determinar si un elementos es instancia del objeto
    print(isinstance(coord_2, Coordenada))
    print(isinstance(3, Coordenada))