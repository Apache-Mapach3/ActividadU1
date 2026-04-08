namespace ActividadU1
{
    public struct EstudianteStruct
    {
        public string Nombre;
        public int Edad;
        public double Promedio;
        public EstudianteStruct(string nombre, int edad, double promedio)
        {
            Nombre = nombre;
            Edad = edad;
            Promedio = promedio;
        }
    }
}