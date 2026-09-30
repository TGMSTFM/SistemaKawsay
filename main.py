from registro import (
    registrar_paciente,
    registrar_medico,
    programar_cita,
    registrar_atencion,
    mostrar_menu
)

from consultas import (
    buscar_medicos_por_especialidad,
    historial_de_paciente
)


def main():
    pacientes = []
    medicos = []
    citas = []
    historial = {}

    while True:
        print(mostrar_menu())
        opcion = input("Elija una opción: ").strip()

        match opcion:

            case "1":
                codigo = input("Código del paciente: ").strip()
                nombre = input("Nombre: ").strip()
                edad = input("Edad: ").strip()

                print(registrar_paciente(
                    pacientes, codigo, nombre, edad
                ))

            case "2":
                codigo = input("Código del médico: ").strip()
                nombre = input("Nombre: ").strip()
                especialidad = input("Especialidad: ").strip()

                print(registrar_medico(
                    medicos, codigo, nombre, especialidad
                ))

            case "3":
                codigo_cita = input("Código de la cita: ").strip()
                codigo_paciente = input("Código del paciente: ").strip()
                codigo_medico = input("Código del médico: ").strip()
                fecha = input("Fecha (AAAA-MM-DD): ").strip()

                print(programar_cita(
                    citas,
                    pacientes,
                    medicos,
                    codigo_cita,
                    codigo_paciente,
                    codigo_medico,
                    fecha
                ))

            case "4":
                codigo_paciente = input("Código del paciente: ").strip()
                nota = input("Nota de la atención: ").strip()

                print(registrar_atencion(
                    historial,
                    pacientes,
                    codigo_paciente,
                    nota
                ))

            case "5":
                especialidad = input("Especialidad a buscar: ").strip()

                resultados = buscar_medicos_por_especialidad(
                    medicos,
                    especialidad
                )

                if resultados:
                    for medico in resultados:
                        print(medico.resumen())
                else:
                    print("No se encontraron médicos con esa especialidad.")

            case "6":
                codigo = input("Código del paciente: ").strip()
                notas = historial_de_paciente(historial, codigo)

                if notas:
                    for nota in notas:
                        print(f"- {nota}")
                else:
                    print("El paciente no tiene atenciones registradas.")

            case "7":
                print("Cerrando Sistema Kawsay.")
                break

            case _:
                print("Opción no válida.")


if __name__ == "__main__":
    main()
