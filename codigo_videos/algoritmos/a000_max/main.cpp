#include <bits/stdc++.h>

using namespace std;
 

int solve(int n, vector<int> a) {
    int max = a[0];
    for (int i=1; i<n; i++) {
        if (a[i] > max) {
            max = a[i];
        }
    }
    return max;
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
