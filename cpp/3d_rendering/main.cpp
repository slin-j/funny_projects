#include <iostream>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <SFML/Graphics.hpp>

#include "config.h"

#define _USE_MATH_DEFINES // for pi (M_PI)
#define PROJ

// i want to #1:
// place quads on screen (code)
// set player pos and direcrion (+viewport in settings)
// -> create 3d-rendering, what the player would see in a 3d room

void printVector3f(sf::Vector3f v){
    std::cout << "x: " << v.x << std::endl;
    std::cout << "y: " << v.y << std::endl;
    std::cout << "z: " << v.z << std::endl;
}

float dot_product_2f(sf::Vector2f v1, sf::Vector2f v2){
    return v1.x*v2.x + v1.y*v2.y;
}

float dot_product_3f(sf::Vector3f v1, sf::Vector3f v2){
    return v1.x*v2.x + v1.y*v2.y + v1.z*v2.z;
}

float vector_abs_3f(sf::Vector3f v){
    return std::sqrt(std::pow(v.x, 2) + std::pow(v.y, 2) + std::pow(v.z, 2));
}

float vector_abs_2f(sf::Vector2f v){
    return std::sqrt(std::pow(v.x, 2) + std::pow(v.y, 2));
}

void crop_vector_to_length(sf::Vector3f* v, float length){
    float k = std::sqrt((std::pow(v->x,2) + std::pow(v->y,2) + std::pow(v->z,2)) / std::pow(length,2));
    v->x /= k;
    v->y /= k;
    v->z /= k;
    // std::cout << v->x << " / " << v->y << " / " << v->z <<std::endl;
}

int main()
{
    sf::ContextSettings settings;
    settings.antialiasingLevel = 8;
    
    sf::Font font;
    if (!font.loadFromFile("../fonts/Hack_Regular_font.ttf")){
        std::cout << "Could not load Font!" << std::endl;
        // todo: throw exception
    }


    sf::RenderWindow topview2dWindow(sf::VideoMode(WINDOW_WIDTH_PX, WINDOW_HEIGHT_PX), "Topview", sf::Style::Close, settings);
    sf::RenderWindow main3dWindow(sf::VideoMode(WINDOW_WIDTH_PX, WINDOW_HEIGHT_PX), "Playerview", sf::Style::Close, settings);
    main3dWindow.setPosition(sf::Vector2i(2000,270));
    topview2dWindow.setPosition(sf::Vector2i(200,270));
    //sf::VideoMode::getDesktopMode().width
    sf::View view;
    view.setSize(WINDOW_WIDTH_PX, WINDOW_HEIGHT_PX);
    view.setCenter(0, 0);
    topview2dWindow.setView(view);

    std::vector<sf::Vertex> quad;
    float x_coords[4] = {10.0f, 10.0f, 20.0f, 20.0f};
    float y_coords[4] = {10.0f, -10.0f, -10.0f, 10.0f};

    for(uint8_t i = 0; i < 4; i++){
        quad.push_back(sf::Vertex(sf::Vector2f(x_coords[i], y_coords[i]), sf::Color::Blue));
    }

    // Playerposistions
    sf::Vector3f player_pos = sf::Vector3f(PLAYER_POS_X, PLAYER_POS_Y, PLAYER_POS_Z);
    sf::Vector3f player_view_dir = sf::Vector3f(PLAYER_VIEW_DIR_X, PLAYER_VIEW_DIR_Y, PLAYER_VIEW_DIR_Z);
    crop_vector_to_length(&player_view_dir, PLAYER_REACH);

    std::vector<sf::Vertex> lineA;

    while (main3dWindow.isOpen())
    {
        sf::Event event;
        while (main3dWindow.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                main3dWindow.close();

            if (event.type == sf::Event::KeyPressed){
                // player_view_dir.x /= 2;
                // player_view_dir.y /= 2;
                // player_view_dir.z /= 2;
                switch(event.key.code){
                    case sf::Keyboard::Q : main3dWindow.close(); break;
                    case sf::Keyboard::A : player_pos.x += PLAYER_SPEED; break;
                    case sf::Keyboard::D : player_pos.x -= PLAYER_SPEED; break;
                    case sf::Keyboard::W : player_pos.y -= PLAYER_SPEED; break;
                    case sf::Keyboard::S : player_pos.y += PLAYER_SPEED; break;
                    case sf::Keyboard::Space : player_pos.z += PLAYER_SPEED; break;
                    case sf::Keyboard::F : player_pos.z -= PLAYER_SPEED; break;
                    case sf::Keyboard::Left : player_view_dir.x -= 1; break;
                    case sf::Keyboard::Right : player_view_dir.x += 1; break;
                    case sf::Keyboard::Up : player_view_dir.y -= 1; break;
                    case sf::Keyboard::Down : player_view_dir.y += 1; break;
                    default: break;
                }
                crop_vector_to_length(&player_view_dir, PLAYER_REACH);
            }
        }
        while (topview2dWindow.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                topview2dWindow.close();
        }

        main3dWindow.clear();
        topview2dWindow.clear();

        // topview Window stuff
        topview2dWindow.draw(&quad[0], quad.size(), sf::Quads);
        lineA.clear();
        lineA.push_back(sf::Vertex(sf::Vector2f(player_pos.x, player_pos.y), sf::Color::Green));
        lineA.push_back(sf::Vertex(sf::Vector2f(player_pos.x+player_view_dir.x*10, player_pos.y+player_view_dir.y*10), sf::Color::Red));
        topview2dWindow.draw(&lineA[0], lineA.size(), sf::Lines);
        lineA.clear();
        lineA.push_back(sf::Vertex(sf::Vector2f(-10.0f, -10.0f), sf::Color::Yellow));
        lineA.push_back(sf::Vertex(sf::Vector2f(10.0f, 10.0f), sf::Color::Magenta));
        topview2dWindow.draw(&lineA[0], lineA.size(), sf::Lines);
        lineA.clear();
        lineA.push_back(sf::Vertex(sf::Vector2f(-10.0f, 10.0f), sf::Color::Yellow));
        lineA.push_back(sf::Vertex(sf::Vector2f(10.0f, -10.0f), sf::Color::Magenta));
        topview2dWindow.draw(&lineA[0], lineA.size(), sf::Lines);


        

        // 3d-view stuff
        std::cout << "\x1B[2J\x1B[H";
        crop_vector_to_length(&player_view_dir, PLAYER_REACH);

        bool first_corner = true;
        for(sf::Vertex cp : quad){
            lineA.clear();

/*
            sf::Vector2f vec1 = sf::Vector2f(cp.position.x - player_pos.x, cp.position.y - player_pos.y);
            sf::Vector2f vec2 = sf::Vector2f(player_view_dir.x, player_view_dir.y);
            float angle = std::acos(dot_product_2f(vec1, vec2) / (vector_abs_2f(vec1) * vector_abs_2f(vec2)));
            std::cout << "angle: " << angle << std::endl;
            if(angle > M_PI_4){continue;}
*/

            ///////////////////////

            # ifdef WIKI
            sf::Vector3f a = sf::Vector3f(cp.position.x, cp.position.y, 0); // just a random point we wannt to draw in 2d
            sf::Vector3f c = player_pos;
            sf::Vector3f O = player_view_dir;
            
            float x = a.x - c.x;
            float y = a.y - c.y;
            float z = a.z - c.z;
            float sx = std::sin(O.x);
            float sy = std::sin(O.y);
            float sz = std::sin(O.z);
            float cx = std::cos(O.x);
            float cy = std::cos(O.y);
            float cz = std::cos(O.z);
            sf::Vector3f d = sf::Vector3f(
                cy * (sz*y +  cz*x) - sy*z,
                sx * (cy*z + sy*(sz*y + cz*x)) + cx*(cz*y - sz*x),
                cx * (cy*z + sy*(sz*y + cz*x)) - sx*(cz*y - sz*x)
            );
            std::cout << d.z << std::endl;
            sf::Vector2f b = sf::Vector2f(
                ((O.z) / d.z) * d.x + O.x,
                ((O.z) / d.z) * d.y + O.y
            );

            lineA.push_back(sf::Vertex(sf::Vector2f((WINDOW_WIDTH_PX/2) + ((b.x)*10), (WINDOW_HEIGHT_PX/2) + ((b.y)*10)), sf::Color::Magenta));
            lineA.push_back(sf::Vertex(sf::Vector2f(WINDOW_WIDTH_PX/2, WINDOW_HEIGHT_PX/2), sf::Color::Magenta));
            #endif

            #ifdef PROJ
            sf::Vector3f A = sf::Vector3f(cp.position.x, cp.position.y, 0.0f); // create point and define height

            sf::Vector3f vPA = sf::Vector3f(
                A.x - (player_pos.x),
                A.y - (player_pos.y),
                A.z - (player_pos.z)
            );

            sf::Vector3f vDiff = sf::Vector3f(
                A.x - (player_pos.x + player_view_dir.x),
                A.y - (player_pos.y + player_view_dir.y),
                A.z - (player_pos.z + player_view_dir.z)
            );

            //printVector3f(player_view_dir);

            sf::Vector3f xy_axis = sf::Vector3f(1.0f, 0.0f, 0.0f);
            crop_vector_to_length(&xy_axis, PLAYER_REACH);
            float projection_factor = dot_product_3f(player_view_dir, xy_axis) / dot_product_3f(xy_axis, xy_axis);

            // sf::Vector3f coordsIn2d = sf::Vector3f(
            //     vDiff.x * (player_view_dir.x - 1),
            //     vDiff.y * (player_view_dir.y - 1),
            //     vDiff.z * (player_view_dir.z - 1)
            // );

            ///////////////////////

            //std::cout << vDiff.x << " / " << vDiff.y << std::endl; 

            float x = (vDiff.z * projection_factor);// / vector_abs_3f(vDiff) * 500;
            float y = (vDiff.y * projection_factor);// / vector_abs_3f(vDiff) * 500;

            lineA.push_back(sf::Vertex(sf::Vector2f((WINDOW_WIDTH_PX/2) + (y), (WINDOW_HEIGHT_PX/2) + (x)), first_corner ? sf::Color::Magenta : sf::Color::Cyan));
            lineA.push_back(sf::Vertex(sf::Vector2f(WINDOW_WIDTH_PX/2, WINDOW_HEIGHT_PX/2), first_corner ? sf::Color::Magenta : sf::Color::Cyan));
            
            #endif

            // debug-text in top-left corner, but only for the first point to draw
            if(first_corner){
                std::string debug_output = "";
                debug_output += "player_pos: " + std::to_string(player_pos.x) + " " + std::to_string(player_pos.y) + " " + std::to_string(player_pos.z) + "\n";
                debug_output += "player_view_dir: " + std::to_string(player_view_dir.x) + " " + std::to_string(player_view_dir.y) + " " + std::to_string(player_view_dir.z) + " --> " + std::to_string(std::round(vector_abs_3f(player_view_dir))) + "\n";
                debug_output += "A: " + std::to_string(A.x) + " " + std::to_string(A.y) + " " + std::to_string(A.z) + "\n";
                debug_output += "PA: " + std::to_string(vPA.x) + " " + std::to_string(vPA.y) + " " + std::to_string(vPA.z) + "\n";
                debug_output += "vDiff: " + std::to_string(vDiff.x) + " " + std::to_string(vDiff.y) + " " + std::to_string(vDiff.z) + "\n";
                debug_output += "projection_factor: " + std::to_string(projection_factor) + "\n";
                debug_output += "2d coords: " + std::to_string(x) + " " + std::to_string(y) + "\n";
                sf::Text dbg_text = sf::Text(debug_output, font, 24);
                main3dWindow.draw(dbg_text);
            }

            main3dWindow.draw(&lineA[0], lineA.size(), sf::Lines);

            first_corner = false;
        }


        //main2dWindow.draw(&quad[0], quad.size(), sf::Quads);
        main3dWindow.display();
        topview2dWindow.display();

        // std::cout << "---------------" << std::endl;

        // std::string s;
        // std::cin >> s;

        // player_view_dir.z += 0.01;
    }

    return 0;
}
