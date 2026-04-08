class Estudiante:
    # constructor#
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones 
    def mostrar_boleta(self):
        print(f"\nBoleta de: {self.nombre}")
        for i, fila in enumerate(self.calificaciones):
            linea = f"Materia {i + 1}: "
            for nota in fila:
                linea += f"[{nota}] "
            print(linea)
print("miniproyecto en python\n")
notas_juanjo = [
    [8.5, 9.0, 9.5],
    [7.0, 8.0, 7.5]
]
notas_peya = [
    [9.0, 9.5, 10.0],
    [8.5, 8.0, 9.0]
]
# se crean los objetos de la clase Estudiante#
est1 = Estudiante("Juanjo", notas_juanjo)
est2 = Estudiante("Peya", notas_peya)
# se guardan los objetos en un arreglo#
grupo_estudiantes = [est1, est2]
# recorrido para mostrar las boletas de cada estudiante#
for alumno in grupo_estudiantes:
    alumno.mostrar_boleta()