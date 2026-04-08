from dataclasses import dataclass
from datetime import datetime
# struct: Usamos un dataclass para representar cada computador en la sala#
@dataclass
class ComputadorStruct:
    id_pc: int
    esta_disponible: bool = True
# se usa un dataclass para representar cada registro de uso en el historial (Record)#
@dataclass(frozen=True)
class RegistroRecord:
    nombre_usuario: str
    computador_id: int
    hora: str
# se usa una clase para manejar la lógica de la sala de cómputo, que contiene un arreglo de structs y un arreglo de records#
class SalaComputo:
    def __init__(self, cantidad_equipos):
        # Arreglo (Lista) de Structs
        self.equipos = [ComputadorStruct(i + 1) for i in range(cantidad_equipos)]
        # Arreglo (Lista) de Records
        self.historial = []
    # se muestran equipos disponibles#
    def mostrar_disponibles(self):
        print("\nEquipos Disponibles")
        # Filtro de disponibles#
        disponibles = [pc for pc in self.equipos if pc.esta_disponible]
        if disponibles:
            for pc in disponibles:
                print(f"[PC-{pc.id_pc}] ", end="")
            print() # Salto de línea
        else:
            print("Ninguno, la sala está llena.")
    # se hace el registrode uso#
    def registrar_uso(self, usuario, id_computador):
        indice = id_computador - 1
        # validacion de equipo disponible#
        if 0 <= indice < len(self.equipos) and self.equipos[indice].esta_disponible:
            # usa el struct#
            self.equipos[indice].esta_disponible = False
            # se crea un record para guardar el historial de uso#
            hora_actual = datetime.now().strftime("%H:%M:%S")
            nuevo_registro = RegistroRecord(usuario, id_computador, hora_actual)
            self.historial.append(nuevo_registro)
            print(f"\n[Exito] Usuario '{usuario}' ha ocupado el PC-{id_computador}.")
        else:
            print(f"\n[404 Error] El PC-{id_computador} no existe o ya está ocupado.")
    # muestra el historial de registros (records)#
    def mostrar_historial(self):
        print("\nHistorial de Registros")
        for registro in self.historial:
            print(f"Usuario: {registro.nombre_usuario} | Equipo: PC-{registro.computador_id} | Hora: {registro.hora}")
# ejecucion#
print("Sistema De Control Sala De Computo")
# Instancia de la sala con 5 equipos#
mi_sala = SalaComputo(5)
# se muestra la disponibilidad inicial (todos disponibles)#
mi_sala.mostrar_disponibles()
# se registran algunos usos (validación de disponibilidad)#
mi_sala.registrar_uso("Juanjo", 2)
mi_sala.registrar_uso("Peya", 5)
# se muestra disponibilidad después del registro#
mi_sala.mostrar_disponibles()
# por si intenta ocupar uno que ya está ocupado#
mi_sala.registrar_uso("Carlos", 2)
# se muestra el historial#
mi_sala.mostrar_historial()