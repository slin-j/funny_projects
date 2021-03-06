using System;

class Board
{
    private string[,] _field = new string[3,3] {{" "," "," "},{" "," "," "},{" "," "," "}};

    public Board()
    {

    }

    public void drawBoardToConsole()
    {
        Console.Clear();

        Console.WriteLine("Press QWE|ASD|YXC to place your Figure:\n");
        Console.WriteLine(" " + _field[0,0] + " │ " + _field[0,1] + " │ " + _field[0,2]);
        Console.WriteLine("───┼───┼───");
        Console.WriteLine(" " + _field[1,0] + " │ " + _field[1,1] + " │ " + _field[1,2]);
        Console.WriteLine("───┼───┼───");
        Console.WriteLine(" " + _field[2,0] + " │ " + _field[2,1] + " │ " + _field[2,2]);
    }

    public int getPlayerInput()
    {
        char input = Console.ReadKey().KeyChar;         // read user input (1 key without enter)
        input = char.ToLower(input);                    // ignore Upper/Lower case input
        int pos = "qweasdyxc".IndexOf(input);           // convert to a number
        return pos;
    }

    public bool playerMove(string Player, int pos)
    {   
        // position out of range
        if(pos < 0 || pos > 8)
            return false;

        // convert 0..8 position to x-y positions
        int x = pos / 3;
        int y = pos % 3;
        
        if(_field[x,y] == " ")  // if field is not occupied
        {
            _field[x,y] = Player;   // place player
            return true;
        }
        else
        {
            return false;   // field was occupied
        }   
    }

    public string isWin()
    {
        for(int i = 0; i < 3; i++)
        {
            // check horizontal lines
            if(_field[i,0] == _field[i,1] && _field[i,0] == _field[i,2])
            {
                return _field[i,0];
            }
            // check vertical lines
            if(_field[0,i] == _field[1,i] && _field[0,i] == _field[2,i])
            {
                return _field[0,i];
            }
        }
        // check left to right diagonal
        if(_field[0,0] == _field[1,1] && _field[0,0] == _field[2,2])
        {
            return _field[0,0];
        }
        // check right to left diagonal
        if(_field[0,2] == _field[1,1] && _field[0,2] == _field[2,0])
        {
            return _field[0,2];
        }
        
        return " ";
    }

    public bool isGameDraw()
    {
        string checkFillState = "";
        
        // add all fields to one string
        for(int i = 0; i < 3; i++)
        {
            for(int j = 0; j < 3; j++)
            {
                checkFillState += _field[i,j];
            }
        }

        // check if there are some empty fields available
        if(checkFillState.IndexOf(" ") == -1)
        {
            return true;    // all fields are occupied
        }
        return false;
    }

    public void ClearCurrentConsoleLine()
    {
        int currentLineCursor = Console.CursorTop;
        Console.SetCursorPosition(0, Console.CursorTop);
        Console.Write(new string(' ', Console.WindowWidth)); 
        Console.SetCursorPosition(0, currentLineCursor);
    }
}