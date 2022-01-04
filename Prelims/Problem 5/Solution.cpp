#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;

int main() {
    // Take input
    int n;
    cin >> n;
    bool square[n][n];
    for (int i = 0; i < n; i++) {
        string row;
        cin >> row;
        for (int j = 0; j < n; j++) {
            square[i][j] = row[j] == '1';
        }
    }

    // Find the number of ones in each row and column
    int rowOnes[n], colOnes[n];
    fill(rowOnes, rowOnes + n, 0);
    fill(colOnes, colOnes + n, 0);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (square[i][j]) {
                rowOnes[i]++;
                colOnes[j]++;
            }
        }
    }

    // For each row and column if the number of ones is x
    // The number of pairs we can form is x * (x - 1) / 2
    int res = 0;
    for (int ones : rowOnes) {
        res += ones * (ones - 1) / 2;
    }
    for (int ones : colOnes) {
        res += ones * (ones - 1) / 2;
    }

    // Print the result
    cout << res << endl;
}
