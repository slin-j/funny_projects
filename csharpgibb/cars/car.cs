using System;
class car
{
    private string _brand;              // Marke
    private string _model;              // Modell
    private string _number;             // Nummer
    private double _tankCapacity;       // Tankkapazität [l]
    private double _tankFillingLevel;   // Tankfüllstand [l]
    private double _consumption;        // Verbrauch [l / 100 km]
    private double _totalDistance;      // Tachostand [km]
    private double _range;              // Reichweite mit dem aktuellen Tankfüllstand [km]

    public car(string brand, string model, string number, double tankCapacity, double consumption)
    {
        _brand = brand;
        _model = model;
        _number = number;
        _tankCapacity = tankCapacity;
        _consumption = consumption;
    }

    public void Drive(double distance)  // Bestimmte Strecke fahren
    {
        // total drivable distance in [km]
        this._range = (this._tankFillingLevel/this._consumption)*100;
        if(distance <= this._range)
        {
            this._totalDistance += distance;    // travel distance
            this._range -= distance;            // update range
            this._tankFillingLevel -= (this._consumption/100)*distance; // set new tank level
        }
        else
        {
            this._totalDistance += this._range; // drive till tank empty
            this._range = 0;                    // no more fuel
            this._tankFillingLevel = 0;
        }
    }

    public void TankUp(double fuel)     // Bestimmte Benzinmenge tanken
    {   
        // fuel up tank
        this._tankFillingLevel += fuel;
        // if tank is overfueld, set it to max
        if(this._tankCapacity <= this._tankFillingLevel)
        {
            this._tankFillingLevel = this._tankCapacity;
        }
        // calculate new drivable range
        this._range = (this._tankFillingLevel/this._consumption)*100;
    }

    public string StatsToString()            // Informationen als Zeichenkette abrufen
    {
        return 
            this._brand + " " +
            this._model + ", " +
            this._number + "\n" +
            "   Tank: " + Math.Round(this._tankFillingLevel,1).ToString() + "/" + this._tankCapacity.ToString() + " Liter\n   at " +
            this._consumption.ToString() + "l/100km" +
            "\n   We drove already " + this._totalDistance.ToString() + "km " +
            "with " + Math.Round(this._range,2).ToString() + "km left.\n"; 
    }
}