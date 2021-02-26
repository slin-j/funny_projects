using System;

namespace tictactoe
{
    class Program
    {
        static void Main(string[] args)
        {            
            Board bd = new Board();
            string turningPlayer = "X";
            while(bd.isWin() == " ")
            {
                if(bd.isGameDraw() == true)
                {
                    Console.WriteLine("Draw!");
                    break;
                }

                bd.drawBoardToConsole();
                bd.waitForPlayer(turningPlayer);
                bd.drawBoardToConsole();

                

                if(turningPlayer.IndexOf("X") == 0)
                {
                    turningPlayer = "O";
                }
                else
                {
                    turningPlayer = "X";
                }
            }
            if(bd.isWin() != " ")
                Console.WriteLine("Player " + bd.isWin() + " won!");
        }
    }
}
