#include <iostream>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <SFML/Graphics.hpp>

#include "config.h"

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

float dot_product(sf::Vector3f v1, sf::Vector3f v2){
    return v1.x*v2.x + v1.y*v2.y + v1.z*v2.z;
}

float vector_abs(sf::Vector3f v){
    return std::sqrt(std::pow(v.x, 2) + std::pow(v.y, 2) + std::pow(v.z, 2));
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

    sf::RenderWindow main2dWindow(sf::VideoMode(WINDOW_WIDTH_PX, WINDOW_HEIGHT_PX), "3D-Rendering Debug", sf::Style::Close, settings);
    sf::Text testtext;
    testtext.setCharacterSize(30);
    testtext.setStyle(sf::Text::Regular);
    testtext.setString("LOL123");

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

    while (main2dWindow.isOpen())
    {
        sf::Event event;
        while (main2dWindow.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                main2dWindow.close();

            if (event.type == sf::Event::KeyPressed){
                player_view_dir.x /= 2;
                player_view_dir.y /= 2;
                player_view_dir.z /= 2;
                switch(event.key.code){
                    case sf::Keyboard::Q : main2dWindow.close(); break;
                    case sf::Keyboard::A : player_pos.x += 1; break;
                    case sf::Keyboard::D : player_pos.x -= 1; break;
                    case sf::Keyboard::W : player_pos.y -= 1; break;
                    case sf::Keyboard::S : player_pos.y += 1; break;
                    case sf::Keyboard::Space : player_pos.z += 1; break;
                    case sf::Keyboard::LControl : player_pos.z -= 1; break;
                    case sf::Keyboard::Left : player_view_dir.x -= 1; break;
                    case sf::Keyboard::Right : player_view_dir.x += 1; break;
                    case sf::Keyboard::Up : player_view_dir.z -= 1; break;
                    case sf::Keyboard::Down : player_view_dir.z += 1; break;
                    default: break;
                }
                crop_vector_to_length(&player_view_dir, PLAYER_REACH);
            }
        }

        main2dWindow.clear();
        
        std::cout << "\x1B[2J\x1B[H";
        crop_vector_to_length(&player_view_dir, PLAYER_REACH);

        for(sf::Vertex cp : quad){
            lineA.clear();

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
            sf::Vector3f A = sf::Vector3f(cp.position.x, cp.position.y, 0.0f); // create point

            sf::Vector3f vPA = sf::Vector3f(
                A.x - (player_pos.x),
                A.y - (player_pos.y),
                A.z - (player_pos.z)
            );

            sf::Vector3f vDiff = sf::Vector3f(
                vPA.x - (player_pos.x + player_view_dir.x),
                vPA.y - (player_pos.y + player_view_dir.y),
                vPA.z - (player_pos.z + player_view_dir.z)
            );

            //printVector3f(player_view_dir);

            sf::Vector3f xy_axis = sf::Vector3f(1.0f, 1.0f, 0.0f);
            crop_vector_to_length(&xy_axis, PLAYER_REACH);
            float projection_factor = dot_product(player_view_dir, xy_axis) / dot_product(xy_axis, xy_axis);


            if(A.x == 10 && A.y == 10){
                std::cout << "player_pos" << std::endl;
                printVector3f(player_pos);
                std::cout << "player_view_dir" << std::endl;
                printVector3f(player_view_dir);
                std::cout << "A" << std::endl;
                printVector3f(A);
                std::cout << "PA" << std::endl;
                printVector3f(vPA);
                std::cout << vector_abs(vPA) << std::endl;
                std::cout << "vDiff" << std::endl;
                printVector3f(vDiff);
                std::cout << "projection_factor\n" << projection_factor << std::endl;
            }

            // sf::Vector3f coordsIn2d = sf::Vector3f(
            //     vDiff.x * (player_view_dir.x - 1),
            //     vDiff.y * (player_view_dir.y - 1),
            //     vDiff.z * (player_view_dir.z - 1)
            // );

            ///////////////////////

            //std::cout << vDiff.x << " / " << vDiff.y << std::endl; 

            

            lineA.push_back(sf::Vertex(sf::Vector2f((WINDOW_WIDTH_PX/2) + ((vDiff.x*projection_factor)*10), (WINDOW_HEIGHT_PX/2) + ((vDiff.y*projection_factor)*10)), sf::Color::Magenta));
            lineA.push_back(sf::Vertex(sf::Vector2f(WINDOW_WIDTH_PX/2, WINDOW_HEIGHT_PX/2), sf::Color::Magenta));
            
            #endif

            main2dWindow.draw(&lineA[0], lineA.size(), sf::Lines);
        }

        main2dWindow.draw(testtext);

        //main2dWindow.draw(&quad[0], quad.size(), sf::Quads);
        main2dWindow.display();

        // std::cout << "---------------" << std::endl;

        // std::string s;
        // std::cin >> s;

        // player_view_dir.z += 0.01;
    }

    return 0;
}
