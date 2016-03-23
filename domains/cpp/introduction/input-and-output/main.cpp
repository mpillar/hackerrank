#include <iostream>
#include <sstream>

int main(int argc, char** argv)
{
    std::string line;

    std::getline(std::cin, line);
    std::stringstream ss(line);

    int a, b, c;
    ss >> a >> b >> c;
    std::cout << a + b + c << std::endl;
}

