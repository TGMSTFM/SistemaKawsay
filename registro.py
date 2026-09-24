from modelos import Paciente, Medico, Cita


def crear_persona(tipo, codigo, nombre, dato):
    if tipo == "paciente":
        return Paciente(codigo, nombre, dato)
    if tipo == "medico":
        return Medico(codigo, nombre, dato)
    return None


def buscar_por_codigo(lista, codigo):
    for elemento in lista:
        if elemento.codigo == codigo:
            return elemento
    return None


def registrar_paciente(pacientes, codigo, nombre, edad_texto):
    if buscar_por_codigo(pacientes, codigo):
        return f"Error: el código {codigo} ya está registrado."

    try:
        edad = int(edad_texto)
    except ValueError:
        return "Error: la edad debe ser un número."

    if edad < 0 or edad > 120:
        return "Error: la edad debe estar entre 0 y 120."

    paciente = crear_persona("paciente", codigo, nombre, edad)
    pacientes.append(paciente)
    return f"Paciente registrado correctamente: {paciente.resumen()}"


def registrar_medico(medicos, codigo, nombre, especialidad):
    if buscar_por_codigo(medicos, codigo):
        return f"Error: el código {codigo} ya está registrado."

    if not especialidad.strip():
        return "Error: debe indicar una especialidad."

    medico = crear_persona("medico", codigo, nombre, especialidad)
    medicos.append(medico)
    return f"Médico registrado correctamente: {medico.resumen()}"


def programar_cita(citas, pacientes, medicos, codigo_cita,
                   codigo_paciente, codigo_medico, fecha):

    paciente = buscar_por_codigo(pacientes, codigo_paciente)
    medico = buscar_por_codigo(medicos, codigo_medico)

    if paciente is None:
        return f"Error: no existe un paciente con código {codigo_paciente}."

    if medico is None:
        return f"Error: no existe un médico con código {codigo_medico}."

    if buscar_por_codigo(citas, codigo_cita):
        return f"Error: el código de cita {codigo_cita} ya está registrado."

    cita = Cita(codigo_cita, paciente, medico, fecha)
    citas.append(cita)

    return f"Cita creada correctamente: {cita.resumen()}"


def registrar_atencion(historial, pacientes, codigo_paciente, nota):
    if not buscar_por_codigo(pacientes, codigo_paciente):
        return f"Error: no existe un paciente con código {codigo_paciente}."

    if not nota.strip():
        return "Error: la nota no puede estar vacía."

    if codigo_paciente not in historial:
        historial[codigo_paciente] = []

    historial[codigo_paciente].append(nota)

    return f"Atención registrada para el paciente {codigo_paciente}."


def mostrar_menu():
    return """
--- SISTEMA KAWSAY ---
1. Registrar paciente
2. Registrar médico
3. Programar cita
4. Registrar atención
5. Buscar médicos por especialidad
6. Consultar historial de un paciente
7. Salir
"""
