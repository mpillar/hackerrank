#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

int getTotalX(vector<int> a, vector<int> b)
{
    int max_a = *max_element(begin(a), end(a));
    int min_b = *min_element(begin(b), end(b));

    int result = 0;
    for (int i = max_a; i <= min_b; i++) {
        bool match = true;
        for (auto j: a) {
            if (i % j != 0) {
                match = false;
                break;
            }
        }
        if (!match) continue;
        for (auto j: b) {
            if (j % i != 0) {
                match = false;
                break;
            }
        }
        if (!match) continue;
        result++;
    }

    return result;
}

int main()
{
    vector<int> a1 = {2, 4};
    vector<int> b1 = {16, 32, 96};
    int result1 = getTotalX(a1, b1);
    assert(result1 == 3);

    vector<int> a2 = {2};
    vector<int> b2 = {20, 30, 12};
    int result2 = getTotalX(a2, b2);
    assert(result2 == 1);
}
