class Paciente:
    def _init_(self, codigo, nombre, edad):
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
        return f"Paciente {self._codigo}: {self._nombre} ({self._edad} años)"


class Medico:
    def _init_(self, codigo, nombre, especialidad):
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
        return f"Medico {self._codigo}: {self._nombre} - {self._especialidad}"


class Cita:
    def _init_(self, codigo, paciente, medico, fecha):
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
            f"{self._paciente.nombre} con médico {self._medico.codigo} "
            f"({self._medico.especialidad})"
        )
