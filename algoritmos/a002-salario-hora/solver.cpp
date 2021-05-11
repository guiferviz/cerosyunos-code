#include <bits/stdc++.h>

using namespace std;
 

double solve(int salario_anual) {
    double salario_mensual = salario_anual / 12.0;
    double salario_dia = salario_mensual / 20.0;
    double salario_hora = salario_dia / 8.0;
    return salario_hora;
}


int main() {
    int t;
    cin >> t;
    cout << fixed << setprecision(2);

    while (t--) {
        int n;
        cin >> n;

        double salario_hora = solve(n);

        cout << salario_hora << "\n";
    }
}
