"""
main.py
Integración multiparadigma

Punto de entrada del prototipo Kawsay. Usa:
- registro.py  (estructurado) para las operaciones de registro y el menú,
- modelos.py   (POO) para las entidades Paciente, Medico y Cita,
- consultas.py (funcional) para las búsquedas declarativas.

Corresponde al Hito 4 (Integración: citas e historial) del cronograma.
"""

from registro import (
    registrar_paciente,
    registrar_medico,
    programar_cita,
    registrar_atencion,
    mostrar_menu,
)
from consultas import buscar_medicos_por_especialidad, historial_de_paciente


def main():
    pacientes = []
    medicos = []
    citas = []
    historial = {}

    while True:
        print(mostrar_menu())
        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            codigo = input("Código del paciente: ").strip()
            nombre = input("Nombre: ").strip()
            edad = input("Edad: ").strip()
            print(registrar_paciente(pacientes, codigo, nombre, edad))

        elif opcion == "2":
            codigo = input("Código del médico: ").strip()
            nombre = input("Nombre: ").strip()
            especialidad = input("Especialidad: ").strip()
            print(registrar_medico(medicos, codigo, nombre, especialidad))

        elif opcion == "3":
            codigo_cita = input("Código de la cita: ").strip()
            codigo_paciente = input("Código del paciente: ").strip()
            codigo_medico = input("Código del médico: ").strip()
            fecha = input("Fecha (AAAA-MM-DD): ").strip()
            print(programar_cita(citas, pacientes, medicos, codigo_cita, codigo_paciente, codigo_medico, fecha))

        elif opcion == "4":
            codigo_paciente = input("Código del paciente: ").strip()
            nota = input("Nota de la atención: ").strip()
            print(registrar_atencion(historial, codigo_paciente, nota))

        elif opcion == "5":
            especialidad = input("Especialidad a buscar: ").strip()
            resultados = buscar_medicos_por_especialidad(medicos, especialidad)
            if resultados:
                for m in resultados:
                    print(m.resumen())
            else:
                print("No se encontraron médicos con esa especialidad.")

        elif opcion == "6":
            codigo_paciente = input("Código del paciente: ").strip()
            notas = historial_de_paciente(historial, codigo_paciente)
            if notas:
                for n in notas:
                    print(f"- {n}")
            else:
                print("El paciente no tiene atenciones registradas.")

        elif opcion == "0":
            print("Cerrando Sistema Kawsay.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
