/**
 * @file util.h
 * @author your name (you@domain.com)
 * @brief 
 * @version 0.1
 * @date 2022-08-30
 * 
 * @copyright Copyright (c) 2022
 * 
 */
#ifndef UTIL_H
#define UTIL_H

#include <iostream> 
#include <math.h>
#include <vector> 
#include <SFML/Graphics.hpp>

float deg_to_rad(float a);
float rad_to_deg(float a);
float angle_between_Vector2f(float x1, float y1, float x2, float y2);

#endif // UTIL_H