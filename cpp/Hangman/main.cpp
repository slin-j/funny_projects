#include <iostream> 
#include <vector>
#include "man.h"

int main()
{
    man hangman;
    std::string word;
    char letter;

    while(true)
    {
        std::cout << "Enter new word to guess: ";
        std::cin >> word;

        // convert to UPPERCASE string
        std::string upperStr;
        for(char c : word)
            upperStr += std::toupper(c);

        hangman.new_word(upperStr);

        // flush console
        std::cout << "\x1B[2J\x1B[H";
        
        while (true)
        {
            std::cout << "Enter letter to guess: ";
            std::cin >> letter;

            // flush console
            std::cout << "\x1B[2J\x1B[H";

            // check entered letter
            if(hangman.is_new_letter(std::toupper(letter)))
                hangman.guess_letter(std::toupper(letter));

            // check game-state
            if(hangman.is_word_correct())
            {
                std::cout << "You survived!" << std::endl;
                break;
            }
            else if(hangman.is_dead())
            {
                std::cout << "You died hahahah!" << std::endl;
                break;
            }
            else 
            {
                hangman.print_game_state();
            }
            
        }
    }

    return 0;
}

//           /|        
//      /\ _/_|_ /\    
//      \.'     './    
//      | (o) (o) |    
//       .       .     
//       / `---´ \     
//     .'         '.   
//   .+-.\   |   /.-+. 
//  ( ## )\  |  /( ## )
//   '--'  ¯¯ˆ¯¯  '--'  