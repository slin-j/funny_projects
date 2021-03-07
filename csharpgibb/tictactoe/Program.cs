using System;

namespace tictactoe
{
    class Program
    {
        static void Main(string[] args)
        {            
            Board bd = new Board();
            string turningPlayer = "X";
            bd.drawBoardToConsole();

            /*
            
            TEST CHECNWININ1

            string[,] tf = new string[3,3] {{" "," "," "},

                                            {" "," "," "},
                                            
                                            {" ","X","X"}};
            NeuralNetwork nn = new NeuralNetwork();
            int asdf = -1;
            asdf = nn.checkWinIn1(tf,"X");
            Console.WriteLine(asdf);
            
            System.Environment.Exit(0); */

            while(bd.isWin() == " ")
            {
                if(bd.isGameDraw() == true)
                {
                    Console.WriteLine("Draw!");
                    break;
                }

                bd.ClearCurrentConsoleLine();
                Console.Write("Player " + turningPlayer + ":");        // tell the user which player is turing next

                // get player input and make the move, if the input is valid
                while(!bd.playerMove(turningPlayer, bd.getPlayerInput())){}
                bd.drawBoardToConsole();
                // toggle player
                if(turningPlayer.IndexOf("X") == 0)
                {
                    turningPlayer = "O";
                }
                else
                {
                    turningPlayer = "X";
                }
            }

            if(bd.isWin() != " ")   // if not draw
            {
                bd.ClearCurrentConsoleLine();
                Console.WriteLine("Player " + bd.isWin() + " won!");
            }
        }
    }
}
