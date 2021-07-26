#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;

int main() {
    // Initialize position
    int x = 0, y = 0;

    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        // Take input
        string dir;
        int delta;
        cin >> dir >> delta;

        // Update position
        if (dir == "U") {
            y += delta;
        }
        else if (dir == "D") {
            y -= delta;
        }
        else if (dir == "L") {
            x -= delta;
        }
        else if (dir == "R") {
            x += delta;
        }
    }

    // Print the final position
    cout << x << ' ' << y << endl;
}