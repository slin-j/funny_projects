cmake_minimum_required(VERSION 3.10)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

project("3d_rendering" VERSION 0.1)

# add src-files
file(GLOB_RECURSE SRC_FILES src/*.cpp)
add_executable("${PROJECT_NAME}" main.cpp ${SRC_FILES})

# include header-files
target_include_directories("${PROJECT_NAME}" PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/inc)

# add sfml
find_package(SFML REQUIRED system window graphics)
target_link_libraries("${PROJECT_NAME}" sfml-graphics sfml-audio)