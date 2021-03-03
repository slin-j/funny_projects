using System;

namespace cars
{
    class Program
    {
        static void Main(string[] args)
        {
            car audiA6 = new car("Audi","A6","BE49025",60,5.6);
            car fiatPanda = new car("Fiat","Panda","BE256854",30,6.7);
            car panzer = new car("Maschine","Traktor Panzer","UDSSR 69420",100,600);
            
            audiA6.TankUp(999);
            fiatPanda.TankUp(999);

            audiA6.Drive(120);
            fiatPanda.Drive(80);

            Console.WriteLine(audiA6.StatsToString());
            Console.WriteLine(fiatPanda.StatsToString());
        }
    }
}
