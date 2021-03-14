#include <bits/stdc++.h>

using namespace std;
 

int solve(int n, vector<int> a) {
    // TU PRECIOSO CÓDIGO AQUÍ.
    return 0;
}


int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector<int> a(n);
        for (int& x : a) cin >> x;

        int max = solve(n, a);

        cout << max << "\n";
    }
}
