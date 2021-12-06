#Encapsulamiento

class CasillaDeVotacion:

    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None
    
    #decorador que indicar una propiedad del objeto, como un GET
    @property
    def region(self):
        return self._region
    
    #nombre_de_propiedad.setter, para cambiar el valor de dicha propiedad, como un SET
    @region.setter
    def set_region(self, region):
        if region in self ._pais:
            self._region = region

        raise ValueError(f"La region {region} no es valida en self ._pais")


    casilla = CasillaDeVotacion(123, ["CDMX", "Morelos"])
    casilla.region = "CDMX"