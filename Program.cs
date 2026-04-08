using System;
namespace ActividadU1
{
    public class Estudiante
    {
        public string Nombre { get; set; }
        public int Edad { get; set; }
        public double Promedio { get; private set; } 
        // Constructor
        public Estudiante(string nombre, int edad, double promedio)
        {
            Nombre = nombre;
            Edad = edad;
            Promedio = promedio;
        }
        // Método solicitado: mostrarInfo//
        public void MostrarInfo()
        {
            Console.WriteLine($"[Estudiante] Nombre: {Nombre} | Edad: {Edad} | Promedio: {Promedio}");
        }
        // Método solicitado: setPromedio//
        public void SetPromedio(double nuevoPromedio)
        {
            Promedio = nuevoPromedio;
            Console.WriteLine($"\n>> Sistema: El promedio de {Nombre} se actualizó a {Promedio}\n");
        }
    }
    // Ejecucion principal//
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Objetos y Clases\n");
            var estudiante1 = new Estudiante("Juanjo", 20, 8.5);
            var estudiante2 = new Estudiante("Peya", 22, 9.0);
            var estudiante3 = new Estudiante("Messi", 21, 7.5);
            //arreglo//
            Estudiante[] listaEstudiantes = { estudiante1, estudiante2, estudiante3 };
            //Recorrido llamando al metodo mostrarInfo()//
            Console.WriteLine("Datos Originales");
            foreach (var est in listaEstudiantes)
            {
                est.MostrarInfo();
            }
            //Modificación usando el método setPromedio()//
            listaEstudiantes[0].SetPromedio(9.8);
            // Mostramos cómo quedó la lista tras el cambio
            Console.WriteLine("Datos Actualizados");
            foreach (var est in listaEstudiantes)
            {
                est.MostrarInfo();
            }
        }
    }
}