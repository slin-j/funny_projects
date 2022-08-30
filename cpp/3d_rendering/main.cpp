/**
 * @file main.cpp
 * @author slin (n-jaeggi@gmx.ch)
 * @brief 
 * @version 0.1
 * @date 2022-08-10
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#include <iostream>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <SFML/Graphics.hpp>

#include "config.h"
#include "player.h"
#include "util.h"

#define _USE_MATH_DEFINES // for pi (M_PI)

// i want to #1:
// place quads on screen (code)
// set player pos and direcrion (+viewport in settings)
// -> create 3d-rendering, what the player would see in a 3d room

int main()
{
    sf::ContextSettings settings;
    settings.antialiasingLevel = 8;

    // Font needed to write Text in Windows 
    sf::Font font;
    if (!font.loadFromFile("../fonts/Hack_Regular_font.ttf")){
        std::cout << "Could not load Font!" << std::endl;
        // todo: throw exception
    }

    Player player;

    // Create Windows and set their Origin to the Middle
    sf::RenderWindow topview2dWindow(sf::VideoMode(WINDOW_WIDTH_PX, WINDOW_HEIGHT_PX), "Topview", sf::Style::Close, settings);
    sf::RenderWindow main3dWindow(sf::VideoMode(WINDOW_WIDTH_PX, WINDOW_HEIGHT_PX), "Playerview", sf::Style::Close, settings);
    main3dWindow.setPosition(sf::Vector2i(2000,270));
    topview2dWindow.setPosition(sf::Vector2i(200,270));
    // set the coordinate-Origon (0,0) to the middle of the window, instead of the top-left corner
    sf::View view = sf::View(sf::Vector2f(0, 0), sf::Vector2f(WINDOW_WIDTH_PX, WINDOW_HEIGHT_PX));
    main3dWindow.setView(view);
    view.setSize(WINDOW_WIDTH_PX, -WINDOW_HEIGHT_PX);
    topview2dWindow.setView(view);

    std::vector<sf::Vertex> quad;
    float x_coords[4] = {50.0f, 100.0f, 100.0f, 50.0f};
    float y_coords[4] = {50.0f, 50.0f, 100.0f, 100.0f};

    for(uint8_t i = 0; i < 4; i++){
        quad.push_back(sf::Vertex(sf::Vector2f(x_coords[i], y_coords[i]), i == 0 ? sf::Color::Magenta : sf::Color::Cyan));
    }

    std::vector<sf::Vertex> lineBuffer;

    while (main3dWindow.isOpen())
    {
        sf::Event event;
        while (main3dWindow.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                main3dWindow.close();

            if (event.type == sf::Event::KeyPressed){
                switch(event.key.code){
                    case sf::Keyboard::Q : main3dWindow.close(); break;
                    // movement
                    case sf::Keyboard::A : player.pos.x -= PLAYER_SPEED; break;
                    case sf::Keyboard::D : player.pos.x += PLAYER_SPEED; break;
                    case sf::Keyboard::W : player.pos.y += PLAYER_SPEED; break;
                    case sf::Keyboard::S : player.pos.y -= PLAYER_SPEED; break;
                    case sf::Keyboard::Space : player.pos.z += PLAYER_SPEED; break;
                    case sf::Keyboard::F : player.pos.z -= PLAYER_SPEED; break;
                    // view-dir
                    case sf::Keyboard::Left : player.rotate_view_dir(0.1); break;
                    case sf::Keyboard::Right : player.rotate_view_dir(-0.1); break;
                    case sf::Keyboard::Up : player.view_dir.y += 1; break;
                    case sf::Keyboard::Down : player.view_dir.y -= 1; break;
                    case sf::Keyboard::PageUp : player.view_dir.z += 1; break;
                    case sf::Keyboard::PageDown : player.view_dir.z -= 1; break;
                    // PLAYER_SPEED
                    // case sf::Keyboard::Num1 : PLAYER_SPEED = 1; break;
                    // case sf::Keyboard::Num2 : PLAYER_SPEED = 3; break;
                    // case sf::Keyboard::Num3 : PLAYER_SPEED = 4; break;
                    // case sf::Keyboard::Num4 : PLAYER_SPEED = 6; break;
                    // case sf::Keyboard::Num5 : PLAYER_SPEED = 10; break;
                    default: break;
                }
            }
        }
        while (topview2dWindow.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                topview2dWindow.close();
        }

        main3dWindow.clear();
        topview2dWindow.clear();

        /* topview Window stuff */
        topview2dWindow.draw(&quad[0], quad.size(), sf::Quads);
        lineBuffer.clear();
        lineBuffer.push_back(sf::Vertex(sf::Vector2f(player.pos.x, player.pos.y), sf::Color::Green));
        lineBuffer.push_back(sf::Vertex(sf::Vector2f(player.pos.x+player.view_dir.x*10, player.pos.y+player.view_dir.y*10), sf::Color::Red));
        topview2dWindow.draw(&lineBuffer[0], lineBuffer.size(), sf::Lines);
        // for(sf::Vertex v : quad){
        //     lineBuffer.clear();
        //     lineBuffer.push_back(sf::Vertex(sf::Vector2f(v.position.x, v.position.y), sf::Color::Green));
        //     lineBuffer.push_back(sf::Vertex(sf::Vector2f(player.pos.x, player.pos.y), sf::Color::Red));
        //     topview2dWindow.draw(&lineBuffer[0], lineBuffer.size(), sf::Lines);
        // }
        lineBuffer.clear();
        // mid cross
        lineBuffer.push_back(sf::Vertex(sf::Vector2f(-10.0f, -10.0f), sf::Color::Yellow));
        lineBuffer.push_back(sf::Vertex(sf::Vector2f(10.0f, 10.0f), sf::Color::Blue));
        topview2dWindow.draw(&lineBuffer[0], lineBuffer.size(), sf::Lines);
        lineBuffer.clear();
        lineBuffer.push_back(sf::Vertex(sf::Vector2f(-10.0f, 10.0f), sf::Color::Cyan));
        lineBuffer.push_back(sf::Vertex(sf::Vector2f(10.0f, -10.0f), sf::Color::Green));
        topview2dWindow.draw(&lineBuffer[0], lineBuffer.size(), sf::Lines);


        // 3d-view stuff
        std::cout << "\x1B[2J\x1B[H";   // flush console

        for(sf::Vertex cp : quad){
            sf::Vector3f pToDraw = sf::Vector3f(cp.position.x, cp.position.y, 0);
            lineBuffer.clear();

            // if the point is not in the field of view -> skip point
            if(std::abs(angle_between_Vector2f(pToDraw.x-player.pos.x, pToDraw.y-player.pos.y, player.view_dir.x, player.view_dir.y)) > deg_to_rad(PLAYER_VIEW_ANGLE/2)) {
                continue;
            } 

            // calculate the perspective projection (what the player sees from his angle and position) and create a vertex
            lineBuffer.push_back(
                sf::Vertex(
                    player.perspective_projection_for_point(pToDraw),   // pos
                    sf::Color::Cyan)                    // color
            );
            lineBuffer.push_back(sf::Vertex(sf::Vector2f(0, 0), sf::Color::Cyan));
            main3dWindow.draw(&lineBuffer[0], lineBuffer.size(), sf::Lines);
            
            // debug-text in top-left corner
            if(false){
                std::string debug_output = "";
                // debug_output += "";
                sf::Text dbg_text = sf::Text(debug_output, font, 24);
                dbg_text.setPosition(sf::Vector2f(-WINDOW_WIDTH_PX/2, -WINDOW_HEIGHT_PX/2));    // topleft corner
                main3dWindow.draw(dbg_text);
            }
        }

        main3dWindow.display();
        topview2dWindow.display();
    }

    return 0;
}
