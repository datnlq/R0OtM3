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

int n;
char plain[100];
int num[300];

int phepthuatwinxenchantic(char x)
{
    if (x >= '0' && x <= '9') return int(x) - 48; else return int(x) - 55;
}

void solve()
{

    int len = strlen(plain);
    for (int i = 0; i < len; i+=2)
    {
        int asc = phepthuatwinxenchantic(plain[i]) * 16 + phepthuatwinxenchantic(plain[i + 1]);
        cout << char(asc);
    }

}

int main()
{
    cout << "Enter: ";
    cin >> plain;
    solve();
    return 0;
}

