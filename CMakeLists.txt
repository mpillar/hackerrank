cmake_minimum_required(VERSION 3.4)
project(hackerrank_cpp)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

set(0_FOR_LOOP domains/cpp/introduction/for-loop/main.cpp)
add_executable(0-for-loop ${0_FOR_LOOP})

set(1_FUNCTIONS domains/cpp/introduction/functions/main.cpp)
add_executable(1-functions ${1_FUNCTIONS})

set(2_INPUT_AND_OUTPUT domains/cpp/introduction/input-and-output/main.cpp)
add_executable(2-input-and-output ${2_INPUT_AND_OUTPUT})

set(3_VARIABLE_SIZED_ARRAYS domains/cpp/introduction/variable-sized-arrays/main.cpp)
add_executable(3-variable-sized-arrays ${3_VARIABLE_SIZED_ARRAYS})

set(4_BETWEEN_TWO_SETS domains/algorithms/implementation/between-two-sets/main.cpp)
add_executable(4-between-two-sets ${4_BETWEEN_TWO_SETS})
