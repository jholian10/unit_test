
import pytest
from agregacion import Motor, Carro 

def test_instancia_motor():
    motor = Motor(120)
    assert isinstance(motor, Motor)
    assert hasattr(motor, "potencia")
    assert motor.potencia == 120

def test_metodo_encender_motor():
    motor = Motor(120)
    resultado = motor.encender()
    assert resultado == "Motor de 120 HP encendido"

def test_instancia_carro():
    carro = Carro("Toyota")
    assert isinstance(carro, Carro)
    assert hasattr(carro, "marca")
    assert carro.marca == "Toyota"
    assert hasattr(carro, "motores")
    assert carro.motores == []

def test_agregar_motor():
    motor1 = Motor(100)
    carro = Carro("Toyota")

    carro.agregar_motor(motor1)

    assert carro.motores[0] == motor1

def test_info_motores():
    motor = Motor(100)
    carro = Carro("Toyota")
    carro.agregar_motor(motor)
    info = carro.info_motores()
    assert info == ["Motor de 100 HP encendido"]
