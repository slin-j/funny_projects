using System;
using System.IO;

namespace weather_data
{
    class Program
    {
        static void Main(string[] args)
        {
            data_type pressure = new data_type();
            data_type temperature = new data_type();
            data_type moist = new data_type();
            data_type rain = new data_type();
            
            string filePath = "./Wetterdaten2011.csv";
            var reader = new StreamReader(filePath);

            int lineCount = File.ReadAllLines("./Wetterdaten2011.csv").Length;
            for(int i = 0; i < lineCount; i++)
            {
                var values = reader.ReadLine().Split(";");

                pressure.new_instance(Convert.ToDouble(values[0]));
                temperature.new_instance(Convert.ToDouble(values[1]));
                moist.new_instance(Convert.ToDouble(values[2]));
                rain.new_instance(Convert.ToDouble(values[3]));        
            }
            
            
            Console.WriteLine("=== Weather Analyzer 2.0 ===");
            Console.WriteLine("========= Luftdruck =========");
            Console.WriteLine("Mean: " + pressure.get_average() + "hPa");
            Console.WriteLine("Max: " + pressure.get_max_val() + "hPa");
            Console.WriteLine("Min: " + pressure.get_min_val() + "hPa");
            Console.WriteLine("========= Temperatur =========");
            Console.WriteLine("Mean: " + temperature.get_average() + "°C");
            Console.WriteLine("Max: " + temperature.get_max_val() + "°C");
            Console.WriteLine("Min: " + temperature.get_min_val() + "°C");
            Console.WriteLine("========= Rel. Luftfeuchtigkeit =========");
            Console.WriteLine("Mean: " + moist.get_average() + "%");
            Console.WriteLine("Max: " + moist.get_max_val() + "%");
            Console.WriteLine("Min: " + moist.get_min_val() + "%");
            Console.WriteLine("========= Niederschlagsmenge =========");
            Console.WriteLine("Mean: " + rain.get_average() + "mm");
            Console.WriteLine("Max: " + rain.get_max_val() + "mm");
            Console.WriteLine("Min: " + rain.get_min_val() + "mm");
        }
    }

    class data_type
    {
        private double value_cnt = 0;
        private double average = 0;
        private double max_val = 0;
        private double min_val = double.MaxValue;

        public void new_instance(double new_val)
        {
            this.value_cnt++;
            this.average += new_val;
            // Max
            if(new_val > this.max_val)
            {
                this.max_val = new_val;
            }
            // Min
            if(new_val < this.min_val)
            {
                this.min_val = new_val;
            }       
        }
        public double get_average()
        {
            return average/value_cnt;
        }

        public double get_max_val()
        {
            return max_val;
        }

        public double get_min_val()
        {
            return min_val;
        }
    }
}

/// Plebvariante ohne oop
/*
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
}*/
