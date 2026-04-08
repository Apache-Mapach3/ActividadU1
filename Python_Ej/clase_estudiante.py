class Estudiante:
    #constructor#
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio
    # Metodos#
    def mostrarInfo(self):
        print(f"[Estudiante] Nombre: {self.nombre} | Edad: {self.edad} | Promedio: {self.promedio}")
    def setPromedio(self, nuevo_promedio):
        self.promedio = nuevo_promedio
        print(f"\n>> Sistema: El promedio de {self.nombre} se actualizó a {self.promedio}\n")
# ejecuciuon#
print("Objetoe e instancias en Python\n")
# inicializacion#
est1 = Estudiante("Pepe", 20, 4.5)
est2 = Estudiante("Alvaro el barbaro", 22, 7.0)
est3 = Estudiante("Sergio Perez", 21, 7.9)
# Almacenarla#
lista_estudiantes = [est1, est2, est3]
# Recorrido#
print("Datos Originales")
for est in lista_estudiantes:
    est.mostrarInfo()
# Modificacion#
lista_estudiantes[0].setPromedio(9.8)
print("Datos Actualizados")
for est in lista_estudiantes:
    est.mostrarInfo()