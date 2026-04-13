using System;
namespace ProyectoFinal
{
    //Clase que contine matriz//
    public class Estudiante
    {
        public string Nombre { get; set; }
        // Matriz bidimensional//
        public double[,] Calificaciones { get; set; }
        public Estudiante(string nombre, double[,] calificaciones)
        {
            Nombre = nombre;
            Calificaciones = calificaciones;
        }
        // Metodo para imprimir la matriz de forma ordenada//
        public void MostrarBoleta()
        {
            Console.WriteLine($"\nBoleta de: {Nombre}"); 
            // Recorrer la matriz://
            for (int fila = 0; fila < Calificaciones.GetLength(0); fila++)
            {
                Console.Write($"Materia {fila + 1}: ");
                for (int col = 0; col < Calificaciones.GetLength(1); col++)
                {
                    Console.Write($"[{Calificaciones[fila, col]}] ");
                }
                Console.WriteLine(); // Salto de línea al terminar la materia
            }
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("MiniProyecto: Arreglo de objetos con matriz en C#");
            // se crean las matrices//
            double[,] notasJuanjo = { 
                { 8.5, 9.0, 9.5 }, 
                { 7.0, 8.0, 7.5 }  
            };
            double[,] notasPeya = { 
                { 9.0, 9.5, 10.0 }, 
                { 8.5, 8.0, 9.0 }   
            };
            // se crean los objetos con su respectiva matriz//
            Estudiante est1 = new Estudiante("Juanjo", notasJuanjo);
            Estudiante est2 = new Estudiante("Peya", notasPeya);
            //arreglo de objetos//
            Estudiante[] grupoEstudiantes = { est1, est2 };
            //Recorrer el arreglo y llamar a su metodo//
            foreach (var alumno in grupoEstudiantes)
            {
                alumno.MostrarBoleta();
            }
        }
    }
}