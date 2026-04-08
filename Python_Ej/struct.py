from dataclasses import dataclass
@dataclass
class EstudianteStruct:
    nombre: str
    edad: int
    promedio: float
print("Struts y records")
s1 = EstudianteStruct("Juanjo", 20, 8.5)
s2 = EstudianteStruct("Peya", 22, 9.0)
s3 = EstudianteStruct("Messi", 21, 7.5)
# se guardan las instancias en un arreglo#
lista_estudiantes = [s1, s2, s3]
# recorrido#
print("Datos Originales:")
for s in lista_estudiantes:
    print(f"{s.nombre} - Promedio: {s.promedio}")
# modificacion#
lista_estudiantes[0].promedio = 9.5
print("\nDespués de modificar:")
for s in lista_estudiantes:
    print(f"{s.nombre} - Promedio: {s.promedio}")