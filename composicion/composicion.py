
class Corazon:
    def __init__(self):
        self.latidos = 0 

    def latir(self):
        self.latidos += 1
        return f"Latido número {self.latidos}"

class Persona:
    def __init__(self, nombre, corazon=None):
        self.nombre = nombre
        self.corazon = corazon if corazon is not None else Corazon()

    def latir(self):
        return self.corazon.latir()


persona1 = Persona("jholian")

print(persona1.nombre)       
print(persona1.latir())      
