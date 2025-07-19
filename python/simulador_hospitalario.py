from dataclasses import dataclass, field
from typing import List, Dict

# Diccionario de médicos predefinidos (con nombres reales, especialidades y horarios)
medicos = [
    {"nombre": "Dr. Luis Sánchez", "especialidad": "Traumatología", "horario": "Mañana"},
    {"nombre": "Dra. Carmen Rojas", "especialidad": "Cardiología", "horario": "Tarde"},
    {"nombre": "Dr. Miguel Torres", "especialidad": "Pediatría", "horario": "Mañana"},
    {"nombre": "Dra. Andrea López", "especialidad": "Cirugía General", "horario": "Noche"},
    {"nombre": "Dr. Juan Vargas", "especialidad": "Radiología", "horario": "Tarde"}
]

@dataclass
class Paciente:
    nombre: str
    especialidad_requerida: str
    gravedad: int
    tiempo: int
    materiales_necesarios: Dict[str, int]

pacientes: List[Paciente] = []
historial: List[Dict] = []

materiales = {
    "jeringas": 50,
    "vendas": 30,
    "oxigeno": 20,
    "analgesicos": 40
}

camas_disponibles = 10
turno_actual = "Mañana"

# Mostrar médicos predefinidos
def mostrar_medicos():
    print("\n--- Médicos Disponibles ---")
    for m in medicos:
        print(f"Nombre: {m['nombre']}, Especialidad: {m['especialidad']}, Horario: {m['horario']}")
    print()

# Registrar pacientes manualmente
def registrar_paciente():
    nombre = input("Nombre del paciente: ").strip()
    especialidad = input("Especialidad requerida: ").strip()
    gravedad = int(input("Gravedad (número, mayor es más grave): "))
    tiempo = int(input("Tiempo de atención requerido (minutos): "))
    
    materiales_necesarios = {}
    print("\nMateriales disponibles:")
    for mat in materiales:
        print(f"{mat} (disponible: {materiales[mat]})")
        cantidad = int(input(f"Cantidad de {mat} que necesita este paciente: "))
        materiales_necesarios[mat] = cantidad

    pacientes.append(Paciente(nombre, especialidad, gravedad, tiempo, materiales_necesarios))
    print("Paciente registrado correctamente.\n")

# Reponer materiales
def reponer_materiales():
    print("\n--- Reposición de Materiales ---")
    for mat in materiales:
        cantidad = int(input(f"Ingrese cantidad para reponer de {mat} (actualmente {materiales[mat]}): "))
        materiales[mat] += cantidad
    print("Materiales repuestos exitosamente.\n")

# Simulación de atención priorizada
def simular_atencion():
    global camas_disponibles
    if not pacientes:
        print("\nNo hay pacientes registrados para atender.\n")
        return
    
    pacientes_ordenados = sorted(pacientes, key=lambda p: p.gravedad, reverse=True)
    print("\n--- Iniciando Simulación ---")
    for paciente in pacientes_ordenados:
        medico_disponible = next(
            (m for m in medicos if m["especialidad"].lower() == paciente.especialidad_requerida.lower() and m["horario"] == turno_actual),
            None
        )
        if not medico_disponible:
            print(f"Paciente {paciente.nombre} NO pudo ser atendido (sin médico disponible en {turno_actual} para {paciente.especialidad_requerida}).")
            continue
        if camas_disponibles <= 0:
            print(f"Paciente {paciente.nombre} NO pudo ser atendido (sin camas disponibles).")
            continue
        suficientes_materiales = all(materiales[mat] >= cant for mat, cant in paciente.materiales_necesarios.items())
        if not suficientes_materiales:
            print(f"Paciente {paciente.nombre} NO pudo ser atendido (faltan materiales).")
            continue
        
        # Atender paciente
        for mat, cant in paciente.materiales_necesarios.items():
            materiales[mat] -= cant
        camas_disponibles -= 1

        historial.append({
            "Paciente": paciente.nombre,
            "Médico": medico_disponible["nombre"],
            "Especialidad": medico_disponible["especialidad"],
            "Turno": turno_actual,
            "Materiales Usados": paciente.materiales_necesarios
        })

        print(f"Paciente {paciente.nombre} atendido por el {medico_disponible['nombre']}.")

    print("\n--- Fin de la Simulación ---\n")

# Mostrar historial
def mostrar_historial():
    if not historial:
        print("\nNo hay historial registrado aún.\n")
        return
    print("\n--- Historial de Pacientes Atendidos ---")
    for idx, h in enumerate(historial, 1):
        print(f"{idx}. Paciente: {h['Paciente']}, Médico: {h['Médico']}, Especialidad: {h['Especialidad']}, Turno: {h['Turno']}, Materiales Usados: {h['Materiales Usados']}")
    print()

# Menú principal mejorado
def menu():
    global turno_actual
    while True:
        print("--- Simulador Hospitalario Avanzado (Profesional) ---")
        print("Turno Actual:", turno_actual)
        print("1. Mostrar médicos disponibles")
        print("2. Registrar paciente")
        print("3. Mostrar materiales disponibles")
        print("4. Reponer materiales")
        print("5. Ejecutar simulación de atención")
        print("6. Mostrar historial de atenciones")
        print("7. Cambiar turno")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_medicos()
        elif opcion == "2":
            registrar_paciente()
        elif opcion == "3":
            print("\n--- Materiales Disponibles ---")
            for mat, cant in materiales.items():
                print(f"{mat}: {cant}")
            print(f"Camas disponibles: {camas_disponibles}\n")
        elif opcion == "4":
            reponer_materiales()
        elif opcion == "5":
            simular_atencion()
        elif opcion == "6":
            mostrar_historial()
        elif opcion == "7":
            turno_actual = input("Ingrese el nuevo turno (Mañana, Tarde, Noche): ").strip().capitalize()
        elif opcion == "8":
            print("Saliendo del simulador...")
            break
        else:
            print("Opción no válida. Intente nuevamente.\n")

# Ejecutar menú
menu()
1
