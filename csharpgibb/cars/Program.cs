using System;

namespace cars
{
    class Program
    {
        static void Main(string[] args)
        {
            car audiA6 = new car("Audi","A6","BE49025",60,5.6);
            car fiatPanda = new car("Fiat","Panda","BE256854",30,6.7);
            Truck scaniaSCR = new Truck("Scania","SCR","BE52625",850,25.5,40000);
            Truck merzActros = new Truck("Mercedes","Actros","BE263254",1000,35.2,60000);
            
            audiA6.TankUp(9999);
            fiatPanda.TankUp(9999);
            scaniaSCR.TankUp(9999);
            merzActros.TankUp(9999);

            scaniaSCR.Charge(38250);
            merzActros.Charge(55100);

            audiA6.Drive(120);
            fiatPanda.Drive(80);
            scaniaSCR.Drive(190);
            merzActros.Drive(150);

            Console.WriteLine(audiA6.StatsToString());
            Console.WriteLine(fiatPanda.StatsToString());
            Console.WriteLine(scaniaSCR.StatsToString());
            Console.WriteLine(merzActros.StatsToString());
        }
    }
}
