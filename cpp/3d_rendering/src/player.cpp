/**
 * @file player.cpp
 * @author your name (you@domain.com)
 * @brief 
 * @version 0.1
 * @date 2022-08-30
 * 
 * @copyright Copyright (c) 2022
 * 
 */
#include <iostream> 
#include <math.h>
#include <vector> 
#include <SFML/Graphics.hpp>

#include "player.h"
#include "config.h"
#include "util.h"

// constructor
Player::Player(){
    this->crop_viewdir_to_reach();
}

// deconstructor
Player::~Player(){
}

/**
 * @brief Set the length of the abs(view_dir) vector to match the reach, without changing direction
 * 
 */
void Player::crop_viewdir_to_reach(void){
    float k = std::sqrt((this->view_dir.x*this->view_dir.x + this->view_dir.y*this->view_dir.y + this->view_dir.z*this->view_dir.z) / (this->reach*this->reach));
    this->view_dir.x *= (1/k);
    this->view_dir.y *= (1/k);
    this->view_dir.z *= (1/k);
}

/**
 * @brief algorithm to calcaulate the point on a 2d surface from the players perspective (pos and viewdir)
 * 
 * @param point Point to draw
 * @return sf::Vector2f
 */
sf::Vector2f Player::perspective_projection_for_point(sf::Vector3f point){
    sf::Vector3f vPointToPlayerPos = sf::Vector3f(  point.x - this->pos.x,
                                                    point.y - this->pos.y,
                                                    point.z - this->pos.z);

    /* X */
    float anglePvdOpX = angle_between_Vector2f(vPointToPlayerPos.x, vPointToPlayerPos.y, this->view_dir.x, this->view_dir.y);
    float x = (anglePvdOpX/deg_to_rad(PLAYER_VIEW_ANGLE/2)) * WINDOW_WIDTH_PX/2;
    // std::cout << "x: " << rad_to_deg(anglePvdOpX) << "°" << std::endl;

    /* rotate around z-axis
     * to calculate the x value we could just view the whole from the top and dont look at the z value
     * BUT to be able to do the same from the side to calc y, we have to rotate it, so its on the x-z-Plane
     * This means y is zero and we can just forget it. thats also why i dont calculate y, bc its 0 anyways
     */
    float angle = angle_between_Vector2f(vPointToPlayerPos.x, vPointToPlayerPos.y, 1, 0);
    vPointToPlayerPos.x = (vPointToPlayerPos.x * std::cos(angle)) - (vPointToPlayerPos.y * std::sin(angle));   

    angle = angle_between_Vector2f(this->view_dir.x, this->view_dir.y, 1, 0);
    float rotated_view_dir_x = (this->view_dir.x * std::cos(angle)) - (this->view_dir.y * std::sin(angle));    

    /* Y */
    float anglePvdOpY = angle_between_Vector2f(vPointToPlayerPos.x, vPointToPlayerPos.z, rotated_view_dir_x, this->view_dir.z);
    float y = (anglePvdOpY/deg_to_rad(PLAYER_VIEW_ANGLE/2)) * WINDOW_HEIGHT_PX/2;
    // std::cout << "y: " << rad_to_deg(anglePvdOpY) << "°" << std::endl;
    // std::cout << "\n";

    return sf::Vector2f(x, y);
}

/**
 * @brief rotate the player view direction vector used to parse mouse inputs
 * 
 * @param pvd Vector to rotate
 * @param z_angle angle in rad to rotate vector counterclockwise around z-axis; pos angle for turning left for player-perspective
 */
void Player::rotate_view_dir(float z_angle){
    float tempx = (this->view_dir.x * std::cos(z_angle)) - (this->view_dir.y * std::sin(z_angle));            
    this->view_dir.y = (this->view_dir.x * std::sin(z_angle)) + (this->view_dir.y * std::cos(z_angle)); 
    this->view_dir.x = tempx;   
}