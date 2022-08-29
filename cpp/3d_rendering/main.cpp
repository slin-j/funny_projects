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

float deg_to_rad(float a){return (a / 180) * M_PI;}
float rad_to_deg(float a){return (a / M_PI) * 180;}

void printVector3f(std::string prefix, sf::Vector3f v){
    std::cout << prefix << "(" << v.x << ", " << v.y << ", " << v.z << ")" << std::endl;
}

void printVector2f(std::string prefix, sf::Vector3f v){
    std::cout << prefix << v.x << " / " << v.y << std::endl;
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

/**
 * @brief gives the angle in degrees between the vectors as measured in a counterclockwise direction from v1 to v2
 * thus angle ranges from -180° to +180°
 * Result+180° would represent the angle from 0 to 360 degrees counterclockwise, starting from v1 
 * @param v1 Vector 1
 * @param v2 Vector 2
 * @return float angle in °
 */

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

void crop_vector_to_length(sf::Vector3f* v, float length){
    float k = std::sqrt((v->x*v->x + v->y*v->y + v->z*v->z) / (length*length));
    v->x *= (1/k);
    v->y *= (1/k);
    v->z *= (1/k);
    // std::cout << v->x << " / " << v->y << " / " << v->z <<std::endl;
}

void ihatethis(sf::Vector3f* v){
    // Y
    // rotation
    // float rotanglePOS = std::acos(dot_product_2f(sf::Vector2f(1, 0), sf::Vector2f(v->x, v->y)) / 
    //     (vector_abs_2f(sf::Vector2f(1, 0)) * vector_abs_2f(sf::Vector2f(v->x, v->y)))
    // );

    // float rotangleNEG = std::acos(dot_product_2f(sf::Vector2f(-1, 0), sf::Vector2f(v->x, v->y)) / 
    //     (vector_abs_2f(sf::Vector2f(-1, 0)) * vector_abs_2f(sf::Vector2f(v->x, v->y)))
    // );

    float rotangle = angle_between_Vector2f(v->x, v->y, 1, 0);

    // float rotangle = v->y < 0 ? (2*M_PI) - rotanglePOS : rotanglePOS;
    //std::string rottext = rotangle == rotanglePOS ? "POS" : "NEG";  // for debug

    // printVector3f("prepvd = ", pvd);
    // printVector3f("prepp = ", pp);
    // printVector3f("preOP = ", OP);
    // std::cout << "------------------------------------------------------" << std::endl;

    float tempx = (v->x * std::cos(rotangle)) - (v->y * std::sin(rotangle));            
    v->y = (v->x * std::sin(rotangle)) + (v->y * std::cos(rotangle)); 
    v->x = tempx;     

    // printVector3f("postpvd = ", *(v));
    // std::cout << "\nfinalangle (pi - angle) " << rottext+" " << std::to_string(rad_to_deg(rotangle)) << std::endl;
    // std::cout << "\npos angle" << std::to_string(rad_to_deg(rotanglePOS)) << std::endl;
    // std::cout << "\nneg angle" << std::to_string(rad_to_deg(rotangleNEG)) << std::endl;
}

float calculate_y(sf::Vector3f pvd, sf::Vector3f OP, sf::Vector3f pp){
    printVector3f("pvd: ", pvd);
    printVector3f("pp: ", pp);
    printVector3f("OP: ", OP);
    
    ihatethis(&pvd);
    ihatethis(&pp);
    ihatethis(&OP);

    printVector3f("pvd: ", pvd);
    printVector3f("pp: ", pp);
    printVector3f("OP: ", OP);

    pp.x *= -1;

    float anglePvdOp = angle_between_Vector2f(pvd.x, pvd.z, OP.x-pp.x, OP.z-pp.z);
    std::cout << "y: " << rad_to_deg(anglePvdOp) << "°" << std::endl;

    return (anglePvdOp/deg_to_rad(PLAYER_VIEW_ANGLE/2)) * WINDOW_HEIGHT_PX/2;
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
    // set the coordinate-Origon (0,0) to the middle of the window, instead of the top-left corner
    sf::View view;
    view.setSize(WINDOW_WIDTH_PX, WINDOW_HEIGHT_PX);
    view.setCenter(0, 0);
    main3dWindow.setView(view);
    view.setSize(WINDOW_WIDTH_PX, -WINDOW_HEIGHT_PX);
    topview2dWindow.setView(view);

    float speed = PLAYER_SPEED;

    std::vector<sf::Vertex> quad;
    float x_coords[4] = {0.0f, 100.0f, 100.0f, 0.0f};
    float y_coords[4] = {0.0f, 0.0f, 100.0f, 100.0f};

    for(uint8_t i = 0; i < 4; i++){
        quad.push_back(sf::Vertex(sf::Vector2f(x_coords[i], y_coords[i]), i == 0 ? sf::Color::Magenta : sf::Color::Cyan));
    }

    // Playerposistions
    sf::Vector3f player_pos = sf::Vector3f(PLAYER_POS_X, PLAYER_POS_Y, PLAYER_POS_Z);
    sf::Vector3f player_view_dir = sf::Vector3f(PLAYER_VIEW_DIR_X, PLAYER_VIEW_DIR_Y, PLAYER_VIEW_DIR_Z);
    crop_vector_to_length(&player_view_dir, PLAYER_REACH);
    float focalLenH = (WINDOW_HEIGHT_PX/2) / (std::tan(PLAYER_VIEW_ANGLE/2));
    float focalLenW = (WINDOW_WIDTH_PX/2) / (std::tan(PLAYER_VIEW_ANGLE/2));

    std::vector<sf::Vertex> lineBuffer;

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
                    case sf::Keyboard::A : player_pos.x -= speed; break;
                    case sf::Keyboard::D : player_pos.x += speed; break;
                    case sf::Keyboard::W : player_pos.y += speed; break;
                    case sf::Keyboard::S : player_pos.y -= speed; break;
                    case sf::Keyboard::Space : player_pos.z += speed; break;
                    case sf::Keyboard::F : player_pos.z -= speed; break;
                    case sf::Keyboard::Left : player_view_dir.x -= 1; break;
                    case sf::Keyboard::Right : player_view_dir.x += 1; break;
                    case sf::Keyboard::Up : player_view_dir.y += 1; break;
                    case sf::Keyboard::Down : player_view_dir.y -= 1; break;
                    case sf::Keyboard::PageUp : player_view_dir.z += 1; break;
                    case sf::Keyboard::PageDown : player_view_dir.z -= 1; break;
                    case sf::Keyboard::Num1 : speed = 1; break;
                    case sf::Keyboard::Num2 : speed = 3; break;
                    case sf::Keyboard::Num3 : speed = 4; break;
                    case sf::Keyboard::Num4 : speed = 6; break;
                    case sf::Keyboard::Num5 : speed = 10; break;
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
        lineBuffer.clear();
        lineBuffer.push_back(sf::Vertex(sf::Vector2f(player_pos.x, player_pos.y), sf::Color::Green));
        lineBuffer.push_back(sf::Vertex(sf::Vector2f(player_pos.x+player_view_dir.x*10, player_pos.y+player_view_dir.y*10), sf::Color::Red));
        topview2dWindow.draw(&lineBuffer[0], lineBuffer.size(), sf::Lines);
        // for(sf::Vertex v : quad){
        //     lineBuffer.clear();
        //     lineBuffer.push_back(sf::Vertex(sf::Vector2f(v.position.x, v.position.y), sf::Color::Green));
        //     lineBuffer.push_back(sf::Vertex(sf::Vector2f(player_pos.x, player_pos.y), sf::Color::Red));
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
        std::cout << "\x1B[2J\x1B[H";
        crop_vector_to_length(&player_view_dir, PLAYER_REACH);

        // freeze positions for calculation
        sf::Vector3f pvd = sf::Vector3f(player_view_dir.x, player_view_dir.y, player_view_dir.z);
        sf::Vector3f pp = sf::Vector3f(player_pos.x, player_pos.y, player_pos.z);


        /////////////////////////////////////////////////////////
        // currently only showing first corner and 2dy is static -100
        // todo: set focal length (px to m) correctly so the corner is at the scr edge when angle of fov matches OP¦pvd angle
        /////////////////////////////////////////////////////////




        bool first_corner = false;
        for(sf::Vertex cp : quad){
            sf::Vector3f OP = sf::Vector3f(cp.position.x, cp.position.y, 0);
            lineBuffer.clear();

            if (x_coords[0] == OP.x && y_coords[0] == OP.y) {first_corner = true;}

            // if the point is not in the field of view -> skip point
            float anglePvdOp = angle_between_Vector2f(OP.x-pp.x, OP.y-pp.y, pvd.x, pvd.y);
            if(std::abs(anglePvdOp) > deg_to_rad(PLAYER_VIEW_ANGLE/2)) {
                continue;
            } 
            std::cout << "x: " << rad_to_deg(anglePvdOp) << "°" << std::endl;

            // 2d x/y Calculations
            float x = -1.0f;    // x coordinate to calc on the screen
            float y = -1.0f;    // y coordinate to calc on the screen

            // X
            // float t =   (pvd.x*(OP.x-pp.x) + pvd.y*(OP.y-pp.y)) / 
            //             (pvd.x*pvd.x + pvd.y*pvd.y);

            // float x_ghost = std::sqrt(
            //     std::pow(pvd.x*t - (OP.x-pp.x), 2) +
            //     std::pow(pvd.y*t - (OP.y-pp.y), 2)
            // );

            // x = focalLenW * (x_ghost / (focalLenW + vector_abs_3f(pvd)*t));

            x = (anglePvdOp/deg_to_rad(PLAYER_VIEW_ANGLE/2)) * WINDOW_WIDTH_PX/2;

            //if(anglePvdOp > 0) {x *= -1;}
            
            // if(first_corner){
            //     ihatethis(&pvd);
            //     ihatethis(&pp);
            // }
            // ihatethis(&OP);
            y = calculate_y(pvd, OP, pp) * -1;

            // // normal calculation
            // float t =         (pvd.x*(OP.x-pp.x) + pvd.z*(OP.z-pp.z)) / 
            //             (pvd.x*pvd.x + pvd.z*pvd.z);

            // float y_ghost = std::sqrt(
            //     std::pow(pvd.x*t - (OP.x-pp.x), 2) +
            //     std::pow(pvd.z*t - (OP.z-pp.z), 2)
            // );

            // y = -1 * focalLenH/10 * (y_ghost / (focalLenH/10 + vector_abs_3f(pvd)*t));
            // if(angle_between_Vector2f(pvd.x, pvd.z, OP.x-pp.x, OP.z-pp.z) > 0) {y *= -1;}


            lineBuffer.push_back(sf::Vertex(sf::Vector2f(x, y), first_corner ? sf::Color::Magenta : sf::Color::Cyan));
            lineBuffer.push_back(sf::Vertex(sf::Vector2f(0, 0), first_corner ? sf::Color::Magenta : sf::Color::Cyan));
            
            // debug-text in top-left corner, but only for the first point to draw
            if(first_corner){
                std::string debug_output = "";
                // debug_output += "rotP: " + std::to_string(rotanglePOS) + "\n";
                // debug_output += "rotN: " + std::to_string(rotangleNEG) + "\n";
                //debug_output += "rot final: " + rottext + " " + std::to_string(player_view_dir.y) + "\n";
                debug_output += "x: " + std::to_string(x) + "\n";
                debug_output += "y: " + std::to_string(y) + "\n";
                debug_output += "player pos: " + std::to_string(player_pos.x) + " " + std::to_string(player_pos.y) + " " + std::to_string(player_pos.z) + "\n";
                debug_output += "player view dir: " + std::to_string(player_view_dir.x) + " " + std::to_string(player_view_dir.y) + " " + std::to_string(player_view_dir.z) + "\n";
                debug_output += "objecct pos: " + std::to_string(cp.position.x) + " " + std::to_string(cp.position.y) + "\n";
                // debug_output += "t: " + std::to_string(t) + "\n";
                // debug_output += "dist: " + std::to_string(x_ghost) + "\n";
                sf::Text dbg_text = sf::Text(debug_output, font, 24);
                dbg_text.setPosition(sf::Vector2f(-WINDOW_WIDTH_PX/2, -WINDOW_HEIGHT_PX/2));    // topleft corner
                main3dWindow.draw(dbg_text);
            }

            main3dWindow.draw(&lineBuffer[0], lineBuffer.size(), sf::Lines);

            first_corner = false;
            // break;   // only draw first corner
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
