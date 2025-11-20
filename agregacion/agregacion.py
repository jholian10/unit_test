
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def encender(self):
        return f"Motor de {self.potencia} HP encendido"


class Carro:
    def __init__(self, marca):
        self.marca = marca
        self.motores = []

    def agregar_motor(self, motor):
        self.motores.append(motor)

    def info_motores(self):
        return [motor.encender() for motor in self.motores]

motor1 = Motor(100)

mi_carro = Carro("Toyota")
mi_carro.agregar_motor(motor1)



