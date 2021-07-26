#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;

int main() {
    // Take input
    int n, q;
    cin >> n >> q;
    bool grid[n][n];
    for (int i = 0; i < n; i++) {
        string row;
        cin >> row;
        for (int j = 0; j < n; j++) {
            grid[i][j] = row[j] == '1';
        }
    }

    // Create a prefix sum table
    int prefSum[n + 1][n + 1];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            prefSum[i + 1][j + 1] = (prefSum[i][j + 1] + prefSum[i + 1][j] - prefSum[i][j] + 
                                    grid[i][j]);
        }
    }

    // For each query, print the answer
    for (int i = 0; i < q; i++) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        int res = (prefSum[x2][y2] - prefSum[x1 - 1][y2] - prefSum[x2][y1 - 1] + 
                    prefSum[x1 - 1][y1 - 1]);
        cout << res << endl;
    }
}