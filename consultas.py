def buscar_medicos_por_especialidad(medicos, especialidad):
    return list(
        filter(
            lambda m: m.especialidad.lower() == especialidad.lower(),
            medicos
        )
    )


def historial_de_paciente(historial, codigo_paciente):
    return list(historial.get(codigo_paciente, []))


def citas_de_paciente(citas, codigo_paciente):
    return list(
        filter(lambda c: c.paciente.codigo == codigo_paciente, citas)
    )


def resumenes(personas):
    return [p.resumen() for p in personas]
