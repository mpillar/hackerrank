#include <iostream>
#include <cstdio>

using namespace std;

int max_of_four(int a, int b, int c, int d)
{
    int result;
    result = max(a, b);
    result = max(result, c);
    result = max(result, d);
    return result;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    std::cout << ans << std::endl;
    return 0;
}
