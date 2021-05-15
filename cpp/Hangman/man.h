#ifndef MAN_H
#define MAN_H

#include <iostream> 
#include <vector> 

#define MAX_STATES 10

class man
{
    public:
        // constructor
        man();
        // deconstructor
        ~man();

        // Methods
        void print_game_state(void);
        void new_word(std::string word);
        bool guess_letter(char letter_in);
        bool is_new_letter(char letter_in);
        bool is_word_correct(void);
        bool is_dead(void);

    private:
        std::string word_to_find = "";
        unsigned int hangmanState = 0;
        std::vector<char> guessed_letters;

        char animations[MAX_STATES] = {1,2,3,4,5,6,7,8,9,10};


};

#endif  // MAN_H
