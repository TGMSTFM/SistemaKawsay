from modelos import Medico, Paciente


def buscar_medicos_por_especialidad(medicos: list, especialidad: str) -> list:
    """
    Devuelve, sin modificar la lista original, los médicos cuya
    especialidad coincide (comparación insensible a mayúsculas).
    """
    return list(
        filter(lambda m: m.especialidad.lower() == especialidad.lower(), medicos)
    )


def historial_de_paciente(historial: dict, codigo_paciente: str) -> list:
    """
    Devuelve las notas de atención de un paciente a partir del historial,
    o una lista vacía si no tiene atenciones registradas. No modifica el
    diccionario original.
    """
    return list(historial.get(codigo_paciente, []))


def citas_de_paciente(citas: list, codigo_paciente: str) -> list:
    """Devuelve, de forma declarativa, las citas asociadas a un paciente."""
    return list(filter(lambda c: c.paciente.codigo == codigo_paciente, citas))


def resumenes(personas: list) -> list:
    """Aplica resumen() a cada elemento sin alterar la colección original."""
    return [p.resumen() for p in personas]
