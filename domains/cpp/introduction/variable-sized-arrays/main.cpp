#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

int main() {
    int n, q;
    std::cin >> n >> q;

    auto** a = new int*[n];

    for (int i = 0; i < n; i++) {
        int length;
        std::cin >> length;
        a[i] = new int[length];

        for (int j = 0; j < length; j++) {
            std::cin >> a[i][j];
        }
    }

    for (int c = 0; c < q; c++) {
        int i, j;
        std::cin >> i >> j;
        std::cout << a[i][j] << std::endl;
    }

    for (int i = 0; i < n; i++) {
        free(a[i]);
    }
    free(a);

    return 0;
}