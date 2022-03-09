/*
    author: gnudnaod
    create: ..............
*/

#include <bits/stdc++.h>
#define F(i,a,b) for (int i = a; i <= b; i++)
#define _F(i,a,b) for (int i = a; i >= b; i--)
#define ll long long
#define push_back pb

using namespace std;

const int maxn = 100;

int base = 32;
char cipher[200];

void solve()
{
    int n = strlen(cipher);
    int c = 0;
    for (int i = 1; i < n; i += 4)
    {
        char x, y, z;
        x = ((cipher[i] - base) << 2) + ((cipher[i + 1] - base) >> 4);
        y = ((cipher[i + 1] - base) << 4) + ((cipher[i + 2] - base) >> 2);
        z = ((cipher[i + 2] - base) << 6) + ((cipher[i + 3] - base));

        cout << x << y << z;
        c += 3;
        if (c > (cipher[0] - base)) return;
    }
}

int main()
{
    // please remove all space in ciphertext before decode 

    cout << "Enter ciphertext to decode: ";
    cin >> cipher;
    solve();
    return 0;
}

