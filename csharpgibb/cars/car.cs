using System;

class car
{
    public string _brand{get; protected set;}              // Marke
    public string _model{get; protected set;}              // Modell
    public string _number{get; protected set;}             // Nummer
    public double _tankCapacity{get; protected set;}       // Tankkapazität [l]
    public double _tankFillingLevel{get; protected set;}   // Tankfüllstand [l]
    public double _consumption{get; protected set;}        // Verbrauch [l / 100 km]
    public double _totalDistance{get; protected set;}      // Tachostand [km]
    public double _range{get; protected set;}              // Reichweite mit dem aktuellen Tankfüllstand [km]

    public car(string brand, string model, string number, double tankCapacity, double consumption)
    {
        _brand = brand;
        _model = model;
        _number = number;
        _tankCapacity = tankCapacity;
        _consumption = consumption;
    }

    public virtual double GetComsumption()     // Ruft den Verbrauch abhängig vom Ladegewicht ab
    {
        return _consumption;
    }

    public void Drive(double distance)  // Bestimmte Strecke fahren
    {
        // total drivable distance in [km]
        _range = (_tankFillingLevel/GetComsumption())*100;
        if(distance <= _range)
        {
            _totalDistance += distance;     // travel distance
            _range -= distance;             // update range
            _tankFillingLevel -= (GetComsumption()/100)*distance; // set new tank level
        }
        else
        {
            _totalDistance += _range;       // drive till tank empty
            _range = 0;                     // no more fuel
            _tankFillingLevel = 0;
        }
    }

    public void TankUp(double fuel)     // Bestimmte Benzinmenge tanken
    {   
        // fuel up tank
        _tankFillingLevel += fuel;
        // if tank is overfueld, set it to max
        if(_tankCapacity <= _tankFillingLevel)
        {
            _tankFillingLevel = _tankCapacity;
        }
        // calculate new drivable range
        _range = (_tankFillingLevel/GetComsumption())*100;
    }

    public virtual string StatsToString()            // Informationen als Zeichenkette abrufen
    {
        return 
            _brand + " " +
            _model + ", " +
            _number + "\n" +
            "   Tank: " + Math.Round(_tankFillingLevel,1).ToString() + "/" + _tankCapacity.ToString() + " Liter\n   at " +
            GetComsumption().ToString() + "l/100km" +
            "\n   We drove already " + _totalDistance.ToString() + "km " +
            "with " + Math.Round(_range,2).ToString() + "km left.\n"; 
    }
}