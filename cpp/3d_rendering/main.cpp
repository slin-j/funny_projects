#include <SFML/Graphics.hpp>

// i want to #1:
// place quads on screen (code)
// set player pos and direcrion (+viewport in settings)
// -> create 3d-rendering, what the player would see in a 3d room

int main()
{
    sf::ContextSettings settings;
    settings.antialiasingLevel = 8;

    sf::RenderWindow main2dWindow(sf::VideoMode(800, 600), "3D-Rendering Debug", sf::Style::Close, settings);

    std::vector<sf::Vertex> quad;
    float x_coords[4] = {10.0f, 100.0f, 200.0f, 10.0f};
    float y_coords[4] = {10.0f, 10.0f, 100.0f, 100.0f};

    for(uint8_t i = 0; i < 4; i++){
        quad.push_back(sf::Vertex(sf::Vector2f(x_coords[i], y_coords[i]), sf::Color::Blue));
    }


    while (main2dWindow.isOpen())
    {
        sf::Event event;
        while (main2dWindow.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                main2dWindow.close();
        }

        main2dWindow.clear();
        main2dWindow.draw(&quad[0], quad.size(), sf::Quads);
        main2dWindow.display();
    }

    return 0;
}
