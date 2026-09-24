"""
registro.py
Paradigma: Estructurado

Contiene las funciones que organizan el flujo del programa mediante
listas, diccionarios y validaciones explícitas: registrar personas,
buscar por código, programar citas y registrar atenciones. Cubre los
requerimientos RF01 a RF05 del informe (Tabla 1).
"""

from modelos import Paciente, Medico, Cita


def crear_persona(tipo: str, codigo: str, nombre: str, dato_extra):
    """
    Centraliza la decisión de instanciar Paciente o Medico.

    tipo: "paciente" o "medico"
    dato_extra: edad (int) si tipo == "paciente";
                especialidad (str) si tipo == "medico"
    """
    if tipo == "paciente":
        return Paciente(codigo, nombre, dato_extra)
    if tipo == "medico":
        return Medico(codigo, nombre, dato_extra)
    raise ValueError(f"Tipo de persona no reconocido: {tipo}")


def buscar_por_codigo(lista: list, codigo: str):
    """RF03: Dado un código registrado, cuando se busca, se devuelve el objeto."""
    for elemento in lista:
        if elemento.codigo == codigo:
            return elemento
    return None


def registrar_paciente(pacientes: list, codigo: str, nombre: str, edad_texto: str) -> str:
    """
    RF01: Registrar paciente.
    Valida código duplicado (Riesgo 1) y edad numérica (Riesgo 2).
    Devuelve un mensaje de resultado legible para el menú.
    """
    if buscar_por_codigo(pacientes, codigo) is not None:
        return f"Error: el código {codigo} ya está registrado."

    try:
        edad = int(edad_texto)
    except ValueError:
        return "Error: la edad debe ser un valor numérico."

    if edad < 0 or edad > 120:
        return "Error: la edad debe estar entre 0 y 120."

    nuevo = crear_persona("paciente", codigo, nombre, edad)
    pacientes.append(nuevo)
    return f"Paciente registrado correctamente: {nuevo.resumen()}"


def registrar_medico(medicos: list, codigo: str, nombre: str, especialidad: str) -> str:
    """RF02: Registrar médico. Valida código duplicado y especialidad no vacía."""
    if buscar_por_codigo(medicos, codigo) is not None:
        return f"Error: el código {codigo} ya está registrado."

    if not especialidad.strip():
        return "Error: debe indicarse una especialidad."

    nuevo = crear_persona("medico", codigo, nombre, especialidad)
    medicos.append(nuevo)
    return f"Médico registrado correctamente: {nuevo.resumen()}"


def programar_cita(
    citas: list, pacientes: list, medicos: list,
    codigo_cita: str, codigo_paciente: str, codigo_medico: str, fecha: str
) -> str:
    """
    RF04: Programar cita.
    Dado paciente y médico existentes, cuando se ingresan fecha y código,
    entonces se crea la cita. Valida referencias inválidas (Riesgo del RF04).
    """
    paciente = buscar_por_codigo(pacientes, codigo_paciente)
    medico = buscar_por_codigo(medicos, codigo_medico)

    if paciente is None:
        return f"Error: no existe un paciente con código {codigo_paciente}."
    if medico is None:
        return f"Error: no existe un médico con código {codigo_medico}."
    if buscar_por_codigo(citas, codigo_cita) is not None:
        return f"Error: el código de cita {codigo_cita} ya está registrado."

    nueva_cita = Cita(codigo_cita, paciente, medico, fecha)
    citas.append(nueva_cita)
    return f"Cita creada correctamente: {nueva_cita.resumen()}"


def registrar_atencion(historial: dict, codigo_paciente: str, nota: str) -> str:
    """
    RF05: Registrar atención.
    Dadas referencias válidas, cuando se completan campos, entonces se
    añade al historial. El historial se organiza como diccionario
    {codigo_paciente: [notas]} para acceso estructurado por código.
    """
    if not nota.strip():
        return "Error: la nota de atención no puede estar vacía."

    historial.setdefault(codigo_paciente, [])
    historial[codigo_paciente].append(nota)
    return f"Atención registrada para el paciente {codigo_paciente}."


def mostrar_menu() -> str:
    """Menú de texto del prototipo (paradigma estructurado)."""
    return (
        "\n--- SISTEMA KAWSAY ---\n"
        "1. Registrar paciente\n"
        "2. Registrar médico\n"
        "3. Programar cita\n"
        "4. Registrar atención\n"
        "5. Buscar médicos por especialidad\n"
        "6. Consultar historial de un paciente\n"
        "0. Salir"
    )
