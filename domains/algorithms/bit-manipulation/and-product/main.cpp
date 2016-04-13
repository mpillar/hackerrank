#include <iostream>
#include <sstream>
#include <algorithm>
#include <stdint.h>

uint32_t onlyLastBit(uint32_t x)
{
    for (int i = 0; i < 32; i++) {
        if (((x >> i) & 0x00000001) > 0) {
            return 1 << i;
        }
    }

    return 0;
}

uint32_t andOfRange(uint32_t a, uint32_t b)
{
    uint32_t result = 0xffffffff;
    uint32_t counter = std::min(a, b);

    while (counter < std::max(a, b) + 1) {
        result &= counter;
        if (result == 0) {
            return result;
        }
        counter = result + onlyLastBit(result);
    }

    return result;
}

int main(int argc, char** argv)
{
    std::string line;

    std::getline(std::cin, line);
    std::stringstream ssStart(line);

    uint32_t n;
    ssStart >> n;

    for (int i = 0; i < n; i++) {
        std::getline(std::cin, line);
        std::stringstream ssLine(line);

        uint32_t a, b;
        ssLine >> a >> b;
        std::cout << andOfRange(a, b) << std::endl;
    }
}

