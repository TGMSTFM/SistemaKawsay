import pytest

from registro import (
    registrar_paciente,
    registrar_medico,
    programar_cita
)

from consultas import buscar_medicos_por_especialidad


@pytest.fixture
def datos_iniciales():
    pacientes = []
    medicos = []
    citas = []

    registrar_paciente(pacientes, "P001", "Ana Torres", "34")
    registrar_medico(medicos, "M001", "Luis Rojas", "Pediatría")

    return pacientes, medicos, citas


def test_caso_normal(datos_iniciales):
    pacientes, medicos, citas = datos_iniciales

    resultado = programar_cita(
        citas, pacientes, medicos,
        "C001", "P001", "M001", "2026-03-10"
    )

    assert "Cita creada correctamente" in resultado
    assert len(citas) == 1


def test_caso_extremo_edad_0_y_120():
    pacientes = []

    r1 = registrar_paciente(
        pacientes, "P010", "Bebé Ficticio", "0"
    )

    r2 = registrar_paciente(
        pacientes, "P011", "Adulto Mayor Ficticio", "120"
    )

    assert "registrado correctamente" in r1
    assert "registrado correctamente" in r2
    assert len(pacientes) == 2


def test_caso_error_edad_no_numerica():
    pacientes = []

    resultado = registrar_paciente(
        pacientes, "P020", "Paciente Ficticio", "treinta"
    )

    assert "Error" in resultado
    assert len(pacientes) == 0


def test_caso_duplicado():
    pacientes = []

    registrar_paciente(
        pacientes, "P030", "Paciente Uno", "40"
    )

    resultado = registrar_paciente(
        pacientes, "P030", "Paciente Dos", "25"
    )

    assert "ya está registrado" in resultado
    assert len(pacientes) == 1


def test_caso_referencia_invalida(datos_iniciales):
    pacientes, medicos, citas = datos_iniciales

    resultado = programar_cita(
        citas, pacientes, medicos,
        "C002", "P999", "M001", "2026-03-11"
    )

    assert "no existe un paciente" in resultado
    assert len(citas) == 0


def test_busqueda_funcional_no_modifica_lista(datos_iniciales):
    pacientes, medicos, citas = datos_iniciales

    original = list(medicos)

    resultado = buscar_medicos_por_especialidad(
        medicos, "pediatría"
    )

    assert len(resultado) == 1
    assert medicos == original
