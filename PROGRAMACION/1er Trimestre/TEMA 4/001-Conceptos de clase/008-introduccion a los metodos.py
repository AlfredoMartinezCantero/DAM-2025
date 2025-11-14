class Gato:
    def _init_(self):
        self.color = ""
        self.edad = 0   
    def maulla(self):
        print("El gato está maullando")
        
        
jaegger = Gato()
jaegger.color = "crema"
jaegger.edad = 9
jaegger.maulla()


lana = Gato()
lana.color = "gris"
lana.edad = 11
lana.maulla()
