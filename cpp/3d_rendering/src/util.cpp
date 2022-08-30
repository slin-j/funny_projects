/**
 * @file util.cpp
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

#include "util.h"

float deg_to_rad(float a){
    return (a / 180) * M_PI;
}

float rad_to_deg(float a){
    return (a / M_PI) * 180;
}

/**
 * @brief gives the angle [rad] between the vectors as measured in a counterclockwise direction from vec1=[x1,y1] to vec2=[x2,y2]
 * thus angle ranges from -PI to +PI
 * Result+PI would represent the angle from 0 to 2 PI rad counterclockwise, starting from v1 
 * @param x1 vector1.x
 * @param y1 vector1.y
 * @param x2 vector2.x
 * @param y2 vector2.y
 * @return float 
 */
float angle_between_Vector2f(float x1, float y1, float x2, float y2){
    return std::atan2(x1*y2-y1*x2,x1*x2+y1*y2);
}