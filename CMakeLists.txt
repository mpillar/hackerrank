cmake_minimum_required(VERSION 3.4)
project(advanced_cpp)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

set(0_FOR_LOOP domains/cpp/introduction/for-loop/main.cpp)
add_executable(for-loop ${0_FOR_LOOP})

set(0_FUNCTIONS domains/cpp/introduction/functions/main.cpp)
add_executable(functions ${0_FUNCTIONS})

set(0_INPUT_AND_OUTPUT domains/cpp/introduction/input-and-output/main.cpp)
add_executable(input-and-output ${0_INPUT_AND_OUTPUT})

set(0_VARIABLE_SIZED_ARRAYS domains/cpp/introduction/variable-sized-arrays/main.cpp)
add_executable(variable-sized-arrays ${0_VARIABLE_SIZED_ARRAYS})
