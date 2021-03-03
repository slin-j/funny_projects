using System;

class NeuralNetwork
{


    private NeuralNetwork()
    {

    }

    private double sigmoid(double input)
    {
        return 1 / (1 + Math.Pow(Math.E, input * -1));
    }
}