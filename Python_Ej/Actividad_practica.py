from dataclasses import dataclass
from datetime import datetime

# struct: representa cada computador
@dataclass
class ComputadorStruct:
    id_pc: int
    esta_disponible: bool = True

# record: representa cada registro de uso inmutable
@dataclass(frozen=True)
class RegistroRecord:
    nombre_usuario: str
    computador_id: int
    hora: str

# clase objeto
class SalaComputo:
    def __init__(self, cantidad_equipos):
        # Arreglo de structs
        self.equipos = [ComputadorStruct(i + 1) for i in range(cantidad_equipos)]
        # Arreglo de records
        self.historial = []

    # Mostrar estado de todos los equipos
    def mostrar_estado(self):
        print("\nEstado de los Equipos")
        for pc in self.equipos:
            estado = "Disponible" if pc.esta_disponible else "Ocupado"
            print(f"PC-{pc.id_pc}: {estado}")

    # Mostrar solo disponibles
    def mostrar_disponibles(self):
        print("\nEquipos Disponibles")
        disponibles = [pc for pc in self.equipos if pc.esta_disponible]
        if disponibles:
            for pc in disponibles:
                print(f"[PC-{pc.id_pc}] ", end="")
            print()
        else:
            print("Ninguno, la sala está llena.")

    # Registrar uso
    def registrar_uso(self, usuario, id_computador):
        indice = id_computador - 1

        if 0 <= indice < len(self.equipos):
            if self.equipos[indice].esta_disponible:
                # modificar struct (mutable)
                self.equipos[indice].esta_disponible = False

                # crear record (inmutable)
                hora_actual = datetime.now().strftime("%H:%M:%S")
                nuevo_registro = RegistroRecord(usuario, id_computador, hora_actual)
                self.historial.append(nuevo_registro)

                print(f"\n[Exito] Usuario '{usuario}' ha ocupado el PC-{id_computador}.")
            else:
                print(f"\n[Error] El PC-{id_computador} ya está ocupado.")
        else:
            print(f"\n[Error] El PC-{id_computador} no existe.")

    # Liberar un computador
    def liberar_pc(self, id_computador):
        indice = id_computador - 1

        if 0 <= indice < len(self.equipos):
            if not self.equipos[indice].esta_disponible:
                self.equipos[indice].esta_disponible = True
                print(f"\n[Exito] El PC-{id_computador} ahora está disponible.")
            else:
                print(f"\n[Error] El PC-{id_computador} ya estaba disponible.")
        else:
            print(f"\n[Error] El PC-{id_computador} no existe.")

    # Mostrar historial
    def mostrar_historial(self):
        print("\nHistorial de Registros")
        if self.historial:
            for registro in self.historial:
                print(f"Usuario: {registro.nombre_usuario} | Equipo: PC-{registro.computador_id} | Hora: {registro.hora}")
        else:
            print("No hay registros aún.")
# Ejecucion#

print("Sistema De Control Sala De Computo")

mi_sala = SalaComputo(5)

while True:
    print("\nMENU")
    print("1. Ver estado de equipos")
    print("2. Ver equipos disponibles")
    print("3. Usar un computador")
    print("4. Liberar un computador")
    print("5. Ver historial")
    print("6. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        mi_sala.mostrar_estado()

    elif opcion == "2":
        mi_sala.mostrar_disponibles()

    elif opcion == "3":
        usuario = input("Ingrese su nombre: ")
        try:
            id_pc = int(input("Ingrese el numero de PC: "))
            mi_sala.registrar_uso(usuario, id_pc)
        except ValueError:
            print("Entrada invalida.")

    elif opcion == "4":
        try:
            id_pc = int(input("Ingrese el numero de PC a liberar: "))
            mi_sala.liberar_pc(id_pc)
        except ValueError:
            print("Entrada invalida.")

    elif opcion == "5":
        mi_sala.mostrar_historial()

    elif opcion == "6":
        print("Saliendo del sistema...")
        break

    else:
        print("Opcion no valida.")