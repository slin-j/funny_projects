using System;

namespace tictactoe
{
    class Program
    {
        static void Main(string[] args)
        {            
            Board bd = new Board();
            string playerOnTurn = "X";
            while(bd.isWin() == " ")
            {
                if(bd.isGameDraw() == true)
                {
                    Console.WriteLine("Draw!");
                    break;
                }

                bd.drawBoardToConsole();
                bd.waitForPlayer(playerOnTurn);
                bd.drawBoardToConsole();

                

                if(playerOnTurn.IndexOf("X") == 0)
                {
                    playerOnTurn = "O";
                }
                else
                {
                    playerOnTurn = "X";
                }
            }
            if(bd.isWin() != " ")
                Console.WriteLine("Player " + bd.isWin() + " won!");
        }
    }
}
