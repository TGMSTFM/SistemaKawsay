class Paciente:
    def __init__(self, codigo, nombre, edad):
        self._codigo = codigo
        self._nombre = nombre
        self._edad = edad

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    def resumen(self):
        return f"Paciente {self.codigo}: {self.nombre} ({self._edad} años)"


class Medico:
    def __init__(self, codigo, nombre, especialidad):
        self._codigo = codigo
        self._nombre = nombre
        self._especialidad = especialidad

    @property
    def codigo(self):
        return self._codigo

    @property
    def especialidad(self):
        return self._especialidad

    def resumen(self):
        return f"Medico {self.codigo}: {self._nombre} - {self.especialidad}"


class Cita:
    def __init__(self, codigo, paciente, medico, fecha):
        self._codigo = codigo
        self._paciente = paciente
        self._medico = medico
        self._fecha = fecha

    @property
    def paciente(self):
        return self._paciente

    @property
    def medico(self):
        return self._medico

    def resumen(self):
        return (
            f"Cita {self._codigo} el {self._fecha}: "
            f"{self.paciente.nombre} con médico {self.medico.codigo} "
            f"({self.medico.especialidad})"
        )
