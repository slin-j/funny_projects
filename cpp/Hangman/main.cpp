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
        hangman.new_word(word);

        while (true)
        {
            std::cout << "Enter letter to guess: ";
            std::cin >> letter;
            hangman.guess_letter(letter);
            hangman.print_game_state();
        }
        
    }

    return 0;
}