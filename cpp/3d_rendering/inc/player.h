/**
 * @file player.hpp
 * @author your name (you@domain.com)
 * @brief 
 * @version 0.1
 * @date 2022-08-30
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#ifndef PLAYER_H
#define PLAYER_H

#include <iostream> 
#include <math.h>
#include <vector> 
#include <SFML/Graphics.hpp>

#include "config.h"

#define MAX_STATES 10

class Player
{
    public:
        /* constructor */
        Player();
        /* deconstructor */
        ~Player();

        sf::Vector3f pos = sf::Vector3f(PLAYER_POS_X, PLAYER_POS_Y, PLAYER_POS_Z);
        sf::Vector3f view_dir = sf::Vector3f(PLAYER_VIEW_DIR_X, PLAYER_VIEW_DIR_Y, PLAYER_VIEW_DIR_Z);

        /* Methods */
        void crop_viewdir_to_reach(void);

        void rotate_view_dir(float z_angle);

        sf::Vector2f perspective_projection_for_point(sf::Vector3f point);

    private:
        /* Attributes */
        const float reach = PLAYER_REACH;
        
        float speed = PLAYER_SPEED;
        float focalLenH = (WINDOW_HEIGHT_PX/2) / (std::tan(PLAYER_VIEW_ANGLE/2));
        float focalLenW = (WINDOW_WIDTH_PX/2) / (std::tan(PLAYER_VIEW_ANGLE/2));

};

#endif  // PLAYER_H