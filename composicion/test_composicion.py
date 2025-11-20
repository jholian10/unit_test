import pytest
from composicion import Corazon, Persona 

def test_instancias():
    corazon = Corazon()
    persona = Persona("Jholian", corazon)
    assert isinstance(persona, Persona)
    assert isinstance(persona.corazon, Corazon)

def test_atributos():
    corazon = Corazon()
    persona = Persona("Jholian", corazon)
    assert hasattr(persona, "nombre")
    assert persona.nombre == "Jholian"
    assert hasattr(persona.corazon, "latidos")
    assert persona.corazon.latidos == 0

def test_metodos():
    corazon = Corazon()
    persona = Persona("Jholian", corazon)
    assert hasattr(persona, "latir")
    latido1 = persona.latir()
    assert latido1 == "Latido número 1"
    latido2 = persona.corazon.latir()
    assert latido2 == "Latido número 2"

