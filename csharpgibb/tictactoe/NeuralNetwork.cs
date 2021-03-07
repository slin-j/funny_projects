using System;

class NeuralNetwork
{
    public NeuralNetwork()
    {

    }

    public int checkWinIn1(string[,] field, string player)
    {
        string checkData = "";
        int count = 0;

        // check COLUMNS
        for(int i = 0; i < 3; i++)
        {
            checkData = "";
            checkData += field[i,0];
            checkData += field[i,1];
            checkData += field[i,2];

            if(checkData.IndexOf(" ") == -1) {continue;}       // datarow filled eg. no valid fields to place in this row/column

            count = 0;      // reset count
            // count the players pices in this row
            for(int j = 0; j < 3; j++)
            {
                if(checkData[j].ToString() == player.ToString())
                    count++;
            }

            if(count == 2)
            {
                return (checkData.IndexOf(" ") + (i*3));        // found winning field for "player" ( 0..8 )
            }
        }

        // check ROWS
        for(int i = 0; i < 3; i++)
        {
            checkData = "";
            checkData += field[0,i];
            checkData += field[1,i];
            checkData += field[2,i];

            if(checkData.IndexOf(" ") == -1) {continue;}       // datarow filled eg. no valid fields to place in this row/column

            count = 0;      // reset count
            // count the players pices in this row
            for(int j = 0; j < 3; j++)
            {
                if(checkData[j].ToString() == player.ToString())
                    count++;
            }

            if(count == 2)
            {
                return (checkData.IndexOf(" ")*3 + i);        // found winning field for "player" ( 0..8 )
            }
        }

        // todo: check diagonal

        return -1; // no winnning position found
    }
}