"""
modelos.py
Paradigma: Orientado a Objetos (POO)

Define las clases del dominio del Sistema Kawsay: Paciente, Medico y Cita.
Los atributos se marcan con guion bajo (encapsulamiento) y se exponen
únicamente mediante propiedades de solo lectura, tal como se documenta
en el diagrama UML (Figura 1) del informe.
"""


class Paciente:
    """Representa a un paciente ficticio registrado en el sistema."""

    def __init__(self, codigo: str, nombre: str, edad: int):
        self._codigo = codigo
        self._nombre = nombre
        self._edad = edad

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def nombre(self) -> str:
        return self._nombre

    def resumen(self) -> str:
        """Devuelve una descripción breve y legible del paciente."""
        return f"Paciente {self._codigo}: {self._nombre} ({self._edad} años)"


class Medico:
    """Representa a un médico ficticio registrado en el sistema."""

    def __init__(self, codigo: str, nombre: str, especialidad: str):
        self._codigo = codigo
        self._nombre = nombre
        self._especialidad = especialidad

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def especialidad(self) -> str:
        return self._especialidad

    def resumen(self) -> str:
        """Devuelve una descripción breve y legible del médico."""
        return f"Medico {self._codigo}: {self._nombre} - {self._especialidad}"


class Cita:
    """
    Representa una cita entre un Paciente y un Medico.

    Relaciones (ver Figura 1):
    - Paciente-Cita: asociación (1 a 0..*). Un paciente puede tener varias citas.
    - Medico-Cita: agregación (1 a 0..*). El médico existe independientemente
      de las citas que atiende.
    """

    def __init__(self, codigo: str, paciente: Paciente, medico: Medico, fecha: str):
        self._codigo = codigo
        self._paciente = paciente
        self._medico = medico
        self._fecha = fecha

    @property
    def paciente(self) -> Paciente:
        return self._paciente

    @property
    def medico(self) -> Medico:
        return self._medico

    def resumen(self) -> str:
        """Devuelve una descripción breve y legible de la cita."""
        return (
            f"Cita {self._codigo} el {self._fecha}: "
            f"{self._paciente.nombre} con médico {self._medico.codigo} "
            f"({self._medico.especialidad})"
        )
