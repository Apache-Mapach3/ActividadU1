using System;
namespace ActividadU1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Structs");
            var s1 = new EstudianteStruct("Juanjo", 20, 8.5);
            var s2 = new EstudianteStruct("Peya", 22, 9.0);
            var s3 = new EstudianteStruct("Messi", 21, 7.5);
            var lista = new[] { s1, s2, s3 };
            foreach (var s in lista)
            {
                Console.WriteLine($"{s.Nombre} - {s.Promedio}");
            }
            lista[0].Promedio = 9.5;
            Console.WriteLine("\nDespués de modificar:");
            foreach (var s in lista)
            {
                Console.WriteLine($"{s.Nombre} - {s.Promedio}");
            }
        }
    }
}