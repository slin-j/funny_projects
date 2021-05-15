#include <iostream> 
#include <algorithm>
#include "man.h"

// constructor
man::man()
{

}

// deconstructor
man::~man()
{

}

// Methods
void man::print_game_state(void)
{
    // guess-progress
    std::string progress;
    for (char c : this->word_to_find)
    {
        // if the letter in word was guessed already
        if(std::find(this->guessed_letters.begin(), this->guessed_letters.end(), c) != this->guessed_letters.end())
            progress += c;
        else
            progress += '_';

        progress += ' ';
    }
    std::cout << progress << std::endl << std::endl;

    // guessed letters
    std::cout << "You guessed the following letters: ";
    for (unsigned int i = 0; i < this->guessed_letters.size(); i++)
    {
        std::cout << this->guessed_letters.at(i);

        // at the last print endl instead of ','
        if (i + 1 == this->guessed_letters.size())
        {
            std::cout << std::endl;
            break;
        }

        std::cout << ',';
    }

    std::cout << this->animations[hangmanState] << std::endl;
}

void man::new_word(std::string newWord)
{
    this->hangmanState = 0;
    this->word_to_find = newWord;
    this->guessed_letters.clear();
}

bool man::guess_letter(char letter_in)
{
    std::cout << "dbg" << letter_in << std::endl;
    this->guessed_letters.push_back(letter_in);

    // if letter not in word
    if(this->word_to_find.find(letter_in) == std::string::npos)
    {
        this->hangmanState++;
        return false;
    }

    return true;
}
