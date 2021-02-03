using System;
using System.IO;

namespace weather_data
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Weather Analyzer 1.0 ===");
            Console.WriteLine(args[0]);
            
            var reader = new StreamReader(args[0]);

            double[,] data = { {0,0,99999}, {0,0,99999}, {0,0,99999}, {0,0,99999} };
            
            int length = File.ReadAllLines(args[0]).Length;
            for(int i = 0; i < length; i++)
            {
                var values = reader.ReadLine().Split(";");
                // === Mean values
                for(int j = 0; j < 4; j++)
                {
                    data[j,0] += Convert.ToDouble(values[j]);
                    // max
                    if(data[j,1] < Convert.ToDouble(values[j]))
                    {
                        data[j,1] = Convert.ToDouble(values[j]);
                    }
                    // min
                    if(data[j,2] > Convert.ToDouble(values[j]))
                    {
                        data[j,2] = Convert.ToDouble(values[j]);
                    }
                }
                


            }
            Console.WriteLine("========= Luftdruck =========");
            Console.WriteLine("Mean: " + data[0,0]/length + "hPa");
            Console.WriteLine("Max: " + data[0,1] + "hPa");
            Console.WriteLine("Min: " + data[0,2] + "hPa");
            Console.WriteLine("========= Temperatur =========");
            Console.WriteLine("Mean: " + data[1,0]/length + "°C");
            Console.WriteLine("Max: " + data[1,1] + "°C");
            Console.WriteLine("Min: " + data[1,2] + "°C");
            Console.WriteLine("========= Rel. Luftfeuchtigkeit =========");
            Console.WriteLine("Mean: " + data[2,0]/length + "%");
            Console.WriteLine("Max: " + data[2,1] + "%");
            Console.WriteLine("Min: " + data[2,2] + "%");
            Console.WriteLine("========= Niederschlagsmenge =========");
            Console.WriteLine("Mean: " + data[3,0]/length + "mm");
            Console.WriteLine("Max: " + data[3,1] + "mm");
            Console.WriteLine("Min: " + data[3,2] + "mm");
        }
    }
}
