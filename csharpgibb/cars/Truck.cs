using System;

class Truck : car
{
    public double _cargoWeight{get; protected set;}        // Aktuelles Ladegewicht [kg]
    public double _maxCargoWeight{get; protected set;}     // Maximales Ladegewicht [kg]

    public Truck(string brand, string model, string number, double tankCapacity, double consumption, int maxCargoWeight) : 
    base(brand, model, number, tankCapacity, consumption)
    {
        _maxCargoWeight = maxCargoWeight;
    }

    public override double GetComsumption()     // Ruft den Verbrauch abhängig vom Ladegewicht ab
    {
        return _consumption + (_cargoWeight*0.002);
    }

    public void Charge(double cargoWeight)      // Fracht mit bestimmten Gewicht laden
    {
        if(cargoWeight > 0)                     // no negative load allowed
        {
            _cargoWeight += cargoWeight;         // add Load

            if(_cargoWeight > _maxCargoWeight)  // overload protection
            {
                _cargoWeight = _maxCargoWeight;
            }
        }
    } 

    public override string StatsToString()      // Informationen als Zeichenkette abrufen
    {
        string carStr = base.StatsToString();
        carStr += "   The Truck us " + _cargoWeight + "/" + _maxCargoWeight + "kg charged.\n";
        return carStr;
    }    
}