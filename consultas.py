def buscar_medicos_por_especialidad(medicos, especialidad):
    resultados = []

    for medico in medicos:
        if medico.especialidad.lower() == especialidad.lower():
            resultados.append(medico)

    return resultados


def historial_de_paciente(historial, codigo_paciente):
    return historial.get(codigo_paciente, [])


def citas_de_paciente(citas, codigo_paciente):
    resultados = []

    for cita in citas:
        if cita.paciente.codigo == codigo_paciente:
            resultados.append(cita)

    return resultados


def resumenes(personas):
    return [persona.resumen() for persona in personas]
