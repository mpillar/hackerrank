#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int a, b;
    std::cin >> a >> b;
    
    for (int i = a; i <= b; i++) {
        if (i >= 1 && i <= 9) {
            std::string s;
            switch (i) {
                case 1:
                    s = "one";
                    break;
                case 2:
                    s = "two";
                    break;
                case 3:
                    s = "three";
                    break;
                case 4:
                    s = "four";
                    break;
                case 5:
                    s = "five";
                    break;
                case 6:
                    s = "six";
                    break;
                case 7:
                    s = "seven";
                    break;
                case 8:
                    s = "eight";
                    break;
                case 9:
                    s = "nine";
                    break;
            }
            std::cout << s << std::endl;
        } else {
            if (i % 2 == 0) {
                std::cout << "even" << std::endl;
            } else {
                std::cout << "odd" << std::endl;
            }
        }
        
    }
    return 0;
}
