---
title: "2024杭电多校第一场"
slug: "07 20 2024杭电多校第一场"
description:
date: "2024-07-20T02:57:29+08:00"
lastmod: "2024-07-20T02:57:29+08:00"
image: cover.png
math:
license:
hidden: false
draft: false
categories: ["学习笔记"]
tags: ["算法竞赛"]
---
## 前言
队友有事所以缺一个人，再加上自己本来就菜<br>
导致这场打的比较不好，于是打算记录一下这几道题目<br>
很多题还是很板子以及很有复学价值的
## 赛时
### [T2 星星](https://acm.hdu.edu.cn/showproblem.php?pid=7434)
最早注意的题目，主要是我怕$n^2$过不了，所以一开始没敲，后来还问了下队友<br>
就是一个简单的背包🎒<br>
这道题还没让我意识到杭电多校评测机的强大👍
```cpp
void solve()
{
    int n = rd();
    int k = rd();
    vector<ll> dp(4 * n + 1, 1e18);
    dp[0] = 0;
    for (int i = 1; i <= n; ++i)
    {
        int a = rd(), b = rd(), c = rd(), d = rd();
        for (int j = min(4 * i, k); j >= 0; --j)
        {
            if (j - 1 >= 0)
                dp[j] = min(dp[j], dp[j - 1] + a);
            if (j - 2 >= 0)
                dp[j] = min(dp[j], dp[j - 2] + b);
            if (j - 3 >= 0)
                dp[j] = min(dp[j], dp[j - 3] + c);
            if (j - 4 >= 0)
                dp[j] = min(dp[j], dp[j - 4] + d);
        }
    }
    cout << dp[k] << '\n';
}
```
### [T1 循环位移](https://acm.hdu.edu.cn/showproblem.php?pid=7433)
第二道注意的题目<br>
因为比赛前一天还在学[后缀数组](/p/07-19-sa后缀数组学习笔记)，所以异常敏感<br>
应该注意到$LCP > n$就可以计入答案<br>
然后敲了很错误的SA的代码，就只计算了交接处的点，应该是交界处直到延申到LCP仍然大于n处<br>

其实我也有想过跳车哈希，但是主要是哈希开map桶的想法有点过于常规了，而且是$nlog(n)$级别的，对于$10^6$级别的数据，我居然不敢这么做<br>
高中的时候有时候觉得STL很慢还觉得是可行的，但是到了这里就不敢搞了是为什么呢，是因为前两场牛客老被卡吗<br>
而且这场比赛的评测机极为强大，我并没有意识到<br>

队友过完12和8之后也来参与这道题的讨论，开展了一个奇怪的`KMP`的方法，觉得可行就敲了<br>
耗了很多时间，最后还是打了哈希，结果怎么样了呢，我的`vector`TLE了，单哈希被卡了<br>
`vector`可能是因为RE之类的 ~~最近拿`vector`打代码老是爆😭~~<br>
我一直不相信自己单哈希被卡，不相信`vector`出问题，但是改了之后都对了<br>
不知道怎么评价了
```cpp
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> Pr;
#define End(X) return cout << (X) << '\n', void()
bool Nai;
int rd()
{
    int res = 0, f = 1;
    char c;
    do
        (c = getchar()) == '-' && (f = -1);
    while (!isdigit(c));
    while (isdigit(c))
        res = (c ^ 48) + (res << 1) + (res << 3), c = getchar();
    return res * f;
}
bool Ri;
const int M = (1 << 20) + 5;
const int P1 = 19260817, mod1 = 1e9 + 7, P2 = 233, mod2 = 998244353;
int hsh1[M + M], hsh2[M + M], pw1[M], pw2[M], hshb1[M], hshb2[M];
int main()
{
    ios::sync_with_stdio(0);
    // freopen("Data.in", "r", stdin);
    int t;
    cin >> t;
    pw1[0] = 1, pw2[0] = 1;
    for (int i = 1; i < M; ++i)
        pw1[i] = 1ll * P1 * pw1[i - 1] % mod1;
    for (int i = 1; i < M; ++i)
        pw2[i] = 1ll * P2 * pw2[i - 1] % mod2;
    auto solve = [&]()
    {
        string a, b;
        cin >> a >> b;
        string t = a + a;
        int n = a.size(), m = b.size();
        for (int i = 1; i < n + n; ++i)
        {
            hsh1[i] = (1ll * hsh1[i - 1] * P1 % mod1 + t[i]) % mod1;
            hsh2[i] = (1ll * hsh2[i - 1] * P2 % mod2 + t[i]) % mod2;
        }
        map<pair<int, int>, int> has;
        auto get_hash = [&](int l, int r, int *hash1, int *hash2)
        {
            return make_pair((hash1[r] - 1ll * hash1[l - 1] * pw1[r - l + 1] % mod1 + mod1) % mod1,
                             (hash2[r] - 1ll * hash2[l - 1] * pw2[r - l + 1] % mod2 + mod2) % mod2);
        };
        for (int i = 1; i <= n; ++i)
            has[get_hash(i, i + n - 1, hsh1, hsh2)] = 1;
        for (int i = 1; i <= m; ++i)
        {
            hshb1[i] = (1ll * hshb1[i - 1] * P1 % mod1 + b[i - 1]) % mod1;
            hshb2[i] = (1ll * hshb2[i - 1] * P2 % mod2 + b[i - 1]) % mod2;
        }
        int ans = 0;
        for (int i = 1; i <= m; ++i)
        {
            if (i + n - 1 <= m)
            {
                int t = has[get_hash(i, i + n - 1, hshb1, hshb2)];
                ans += t;
            }
        }
        cout << ans << '\n';
    };
    while (t--)
        solve();
}
```
赛后补了SA的代码，因为不知道怎么样求到最近的第一串的$LCP$, 就搞了两个循环
```cpp
void solve()
{
    string a, b;
    cin >> a >> b;
    string s = a.substr(1, a.size() - 1) + a + "-" + b;
    SA_Array S(s);
    int n = a.size(), m = b.size();
    int now = 0;
    int ans = 0;
    S.show();
    vector<int> L(n + n + m + 1), R(n + n + m + 1);
    for (int i = 2; i <= n + n + m; ++i)
    {
        if (S.SA[i - 1] < n + n)
            now = S.height[i];
        else
            now = min(now, S.height[i]);
        L[i] = now;
    }
    now = 0;
    for (int i = n + n + m; i >= 2; --i)
    {
        R[i] = now;
        if (S.SA[i] < n + n)
            now = S.height[i];
        else
            now = min(now, S.height[i]);
    }
    for (int i = 2; i <= n + n + m; ++i)
    {
        if (S.SA[i] > n + n)
            if (max(L[i], R[i]) >= n)
                ++ans;
    }
    cout << ans << '\n';
}
```
### [T8 位运算](https://acm.hdu.edu.cn/showproblem.php?pid=7440)
这道题是赛时过的比较多的，是队友写的<br>
思想大概就是，由于纯位运算是各位不影响的，所以只需要拆开看每位的贡献就可以了<br>
可以枚举出来，12种出1的方式，4种出0的方式<br>
```cpp
void solve()
{
    int n = rd(), k = rd();
    ll ans = 1;
    for (int i = 0; i < k; ++i)
        if (1 << i & n)
            ans *= 12;
        else ans *= 4;
    cout << ans << '\n';
}
```
### [T12 并](https://acm.hdu.edu.cn/showproblem.php?pid=7444)
队友最早注意到的题，并且一开始就做了<br>
可以把所有矩阵切成很多的**小矩阵**(离散化后就是**小正方形**了)，然后计算**小矩阵**被所给矩阵覆盖的**个数**<br>
如果一个矩阵$m$个矩阵覆盖，选择这个矩阵的概率就是$\frac{C_n^i - C_n^{n - m}}{C_n^i}$**(全集-不选)**<br>
其中也用到了差分计数的方式<br>
思路很正确但是队友有个$j$打成$i$了导致WA了两发<br>
代码就贴队友的吧（
```cpp
#include <bits/stdc++.h>
using namespace std;
const int N = 2010, Mod = 998244353;
inline int add(int a, int b) { return a + b >= Mod ? a + b - Mod : a + b; }
inline int sub(int a, int b) { return a - b < 0 ? a - b + Mod : a - b; }
int n, X[N << 1], Y[N << 1], top1, top2;
struct Node
{
    int x1, y1, x2, y2;
} a[N];
int mp[N << 1][N << 1], jie[N], ni[N];
int Pow(int a, int b)
{
    int ret = 1;
    while (b)
    {
        if (b & 1)
            ret = 1ll * ret * a % Mod;
        a = 1ll * a * a % Mod;
        b >>= 1;
    }
    return ret;
}
int m[N << 1][N << 1];
void init()
{
    jie[0] = ni[0] = 1;
    for (int i = 1; i < N; ++i)
        jie[i] = 1ll * jie[i - 1] * i % Mod;
    int tmp = Pow(jie[N - 1], Mod - 2);
    for (int i = N - 1; i >= 1; --i)
        ni[i] = tmp, tmp = 1ll * tmp * i % Mod;
}
int C(int a, int b)
{
    if (a < b)
        return 0;
    return 1ll * jie[a] * ni[b] % Mod * ni[a - b] % Mod;
}
int ans[N];
int main()
{
    ios::sync_with_stdio(0);
    cin >> n;
    for (int i = 1; i <= n; ++i)
        cin >> a[i].x1 >> a[i].y1 >> a[i].x2 >> a[i].y2, X[++top1] = a[i].x1, X[++top1] = a[i].x2, Y[++top2] = a[i].y1, Y[++top2] = a[i].y2;
    sort(X + 1, X + top1 + 1), sort(Y + 1, Y + 1 + top2);
    top1 = unique(X + 1, X + 1 + top1) - X - 1, top2 = unique(Y + 1, Y + 1 + top2) - Y - 1;
    for (int i = 1; i <= n; ++i)
    {
        a[i].x1 = lower_bound(X + 1, X + 1 + top1, a[i].x1) - X;
        a[i].x2 = lower_bound(X + 1, X + 1 + top1, a[i].x2) - X;
        a[i].y1 = lower_bound(Y + 1, Y + 1 + top2, a[i].y1) - Y;
        a[i].y2 = lower_bound(Y + 1, Y + 1 + top2, a[i].y2) - Y;
        m[a[i].x1][a[i].y1]++, m[a[i].x1][a[i].y2]--;
        m[a[i].x2][a[i].y1]--, m[a[i].x2][a[i].y2]++;
    }
    init();
    for (int i = 1; i <= top1; ++i)
        for (int j = 1; j <= top2; ++j)
            m[i][j] += m[i - 1][j] + m[i][j - 1] - m[i - 1][j - 1];
    for (int i = 1; i < top1; ++i)
    {
        for (int j = 1; j < top2; ++j)
        {
            ans[m[i][j]] = add(ans[m[i][j]], 1ll * (X[i + 1] - X[i]) * (Y[j + 1] - Y[j]) % Mod);
        }
    }
    for (int i = 1; i <= n; ++i)
    {
        int tans = 0, inv = Pow(C(n, i), Mod - 2);
        for (int j = 1; j <= n; ++j)
        {
            tans = add(tans, 1ll * ans[j] * sub(C(n, i), C(n - j, i)) % Mod * inv % Mod);
        }
        cout << tans << endl;
    }
    return 0;
}

```
### [T4 树](https://acm.hdu.edu.cn/showproblem.php?pid=7436)
赛时花的最久的题，到最后还没磕出来，一开始想错想法的时候倒是想过**线段树合并**，但是那时比较浅<br>
其次就是对**线段树合并**的感知不够深刻，不知道他可以在合并的时候统计答案，就实际上是一个**分治**的思想吧，但是我把数据结构学的太死了（或者说没怎么学<br>
首先就是化简一下式子，如果我们只算$A_u > A_v$的部分，这样的话得到的就是答案的一半，只需要最后乘个2就可以了（相当于顺序交换即乘2<br>

$$
\begin{aligned}
记录 in(i) &= u \in subtree(i) \newline
small(i, u) &= v \in subtree(i), \ A_u > A_v \newline
count(i, u) &= \sum_{small(i, u)}1 \newline
sum(i, u) &= \sum_{small(i, u)}A_v \newline \newline
\sum_{in(i),\ small(i, u)}^{}{f(u, v)}&= \sum_{in(i),\ small(i, u)}^{}{A_u \cdot (A_u - A_v)} \newline
&= \sum_{in}{count(i, u) \cdot A_u ^2 - sum(i, u) \cdot A_u}
\end{aligned}
$$
我们可以看到一个点的贡献是来源于其他比他小的**平方和**，**和**与**个数**<br>
赛时有两种想法<br>
1. 按照权值大小更新其上的所有父亲结点
2. 在dfs的时候将所有子树答案合并到该点

第一种想法的话瓶颈在于没法直接更新一个链的答案的**同时**统计答案<br>
第二种想法的话瓶颈在于怎么合并两个子树，队友想过平衡树套启发式，但是我不会平衡树👍<br>
然后就干磕了很久<br>
最后也没求出来🥺<br>
赛后补题的时候发现就是在合并线段树的时候更新答案就可以了<br>
代码贴下面了<br>
```cpp
const int M = 1.3e7 + 5;
typedef unsigned long long ull;
int ls[M], rs[M];
ull cnt[M], sum[M], sqr[M];
void solve()
{
    int n = rd();
    vector<vector<int>> E(n + 1);
    for (int i = 1; i < n; ++i)
    {
        int u = rd(), v = rd();
        E[u].push_back(v);
        E[v].push_back(u);
    }
    vector<int> id(n + 1), A(n + 1);
    for (int i = 1; i <= n; ++i)
        A[id[i] = i] = rd();
    sort(id.begin() + 1, id.end(), [&](int x, int y){return A[x] < A[y];});
    vector<int> rk(n + 1);
    for (int i = 1; i <= n; ++i)
        rk[id[i]] = i;
    int num = 0;
    vector<int> rt(n + 1);
    vector<ull> ans(n + 1);
    auto push_up = [&](int p)
    {
        cnt[p] = cnt[ls[p]] + cnt[rs[p]];
        sum[p] = sum[ls[p]] + sum[rs[p]];
        sqr[p] = sqr[ls[p]] + sqr[rs[p]];
    };
    bool flag = 0;
    auto Update = [&](auto self, int &p, int l, int r, int x, ull y) -> void
    {
        if (!p)
            p = ++num;
        if (l == r)
        {
            cnt[p] = 1;
            sum[p] = y;
            sqr[p] = y * y;
            return;
        }
        int mid = l + r >> 1;
        if (x <= mid)
            self(self, ls[p], l, mid, x, y);
        else
            self(self, rs[p], mid + 1, r, x, y);
        push_up(p);
    };
    auto Merge = [&](auto self, int &p, int q, int l, int r, ull has1, ull pre1, ull has2, ull pre2) -> ull
    {
        if (!p || !q || l == r)
        {
            ull L = has1 * sqr[q] - pre1 * sum[q];
            ull R = has2 * sqr[p] - pre2 * sum[p];
            //就是上面推出的那个式子对于两边都算贡献
            if (!p) p = q;
            else cnt[p] += cnt[q], sum[p] += sum[q], sqr[p] += sqr[q];
            return L + R;
        }
        int mid = l + r >> 1;
        //先r后l的原因是先更新左边的话，cnt[ls[q]]可能会变
        ull R = self(self, rs[p], rs[q], mid + 1, r, has1 + cnt[ls[p]], pre1 + sum[ls[p]], has2 + cnt[ls[q]], pre2 + sum[ls[q]]);
        ull L = self(self, ls[p], ls[q], l, mid, has1, pre1, has2, pre2);
        push_up(p);
        return L + R;
    };
    auto dfs = [&] (auto self, int u, int f) -> void
    {
        Update(Update, rt[u], 1, n, rk[u], A[u]);
        for (int v : E[u])
            if (v ^ f)
            {
                self(self, v, u);
                ans[u] += Merge(Merge, rt[u], rt[v], 1, n, 0, 0, 0, 0);
                ans[u] += ans[v];
                flag = 0;
            }
    };
    dfs(dfs, 1, 0);
    ull res = 0;
    for (int i = 1; i <= n; ++i)
        res ^= ans[i] << 1;
    cout << res << '\n';
}
```
### [T5 博弈](https://acm.hdu.edu.cn/showproblem.php?pid=7437)
最后一道A的题目<br>
队友看了，队友和我说了，队友写了，队友过了<br>
大概思路就是，因为是同一轮随机选的，先后的概率是50%，如果剩下超过两个不一样的(即序列里有超过1个的奇数)，那概率就是50%<br>
之后的话只需要判断平局的可能性就可以了，如果最后剩出来一个，那么平局的话就算作是Alice赢，如果没多出这么一个，两人都没赢。<br>
（其实和题解的思想挺像的
## 赛后
### [T3 传送](https://acm.hdu.edu.cn/showproblem.php?pid=7435)
**线段树分治**<br>
好陌生的名词<br>
但是其实挺板子的吧（<br>
线段树分治的话可以把这种加边操作改成加$O(mlog(n))$级别条边<br>
分治的时候会遍历到每一个单点($O(n)$)，并且在向下分治的时候会加入区间拥有的边，出区间的时候需要撤销并查集的操作<br>
因此整体有个启发式的/按秩合并的$log(n)$的复杂度<br>
好像$O(mlog^2(n))$的复杂度有点高，赛后jiangly的代码和标程都TLE了，只能看赛时的神机了👍<br>
统计的时候需要先先减去当前的答案，然后再在合并的时候加回来，相当于无后效性了<br>
然后这题比较阳间只需要计算1通到的地方即可，也就是在线段树叶子结点的时候直接把答案累计到1的联通块那里<br>
```cpp
void solve()
{
    int n = rd(), m = rd();
    vector<vector<pair<int, int>>> E((n + 1) << 2);
    auto Ins = [&](auto self, int l, int r, int L, int R, int p, auto edge) -> void
    {
        if (l == L && R == r)
        {
            E[p].push_back(edge);
            return;
        }
        int mid = L + R >> 1;
        if (r <= mid)
            self(self, l, r, L, mid, p << 1, edge);
        else if (l > mid)
            self(self, l, r, mid + 1, R, p << 1 | 1, edge);
        else
            self(self, l, mid, L, mid, p << 1, edge), self(self, mid + 1, r, mid + 1, R, p << 1 | 1, edge);
    };
    for (int i = 1; i <= m; ++i)
    {
        int u = rd(), v = rd(), l = rd(), r = rd();
        Ins(Ins, l, r, 1, n, 1, make_pair(u, v));
    }
    struct DSU
    {
        int n;
        vector<int> fa, sz;
        vector<ll> tag;
        stack<int> stk;
        DSU(int size) : n(size), fa(n + 1), sz(n + 1, 1), tag(n + 1)
        {
            iota(fa.begin(), fa.end(), 0);
        }
        int find(int u)
        {
            while (u ^ fa[u])
                u = fa[u];
            return u;
        }
        void Merge(int u, int v)
        {
            u = find(u), v = find(v);
            if (u == v)
                return;
            if (sz[u] < sz[v])
                swap(u, v);
            fa[v] = u;
            tag[v] -= tag[u];
            sz[u] += sz[v];
            stk.push(v);
        }
        void roll_back(int state)
        {
            while (stk.size() != state)
            {
                int v = stk.top();
                stk.pop();
                int u = fa[v];
                tag[v] += tag[u];
                sz[u] -= sz[v];
                fa[v] = v;
            }
        }
        int get_state() { return stk.size(); }
        void Update(int x) { tag[find(1)] += x; }
    } D(n);
    auto work = [&](auto self, int L, int R, int p) -> void
    {
        int now = D.get_state();
        for (auto [u, v] : E[p])
            D.Merge(u, v);
        if (L == R)
            D.Update(R);
        else
        {
            int mid = L + R >> 1;
            self(self, L, mid, p << 1);
            self(self, mid + 1, R, p << 1 | 1);
        }
        D.roll_back(now);
    };
    work(work, 1, n, 1);
    ll ans = 0;
    for (int i = 1; i <= n; ++i)
        ans ^= D.tag[i];
    cout << ans << '\n';
}
```
### [T6 序列立方](https://acm.hdu.edu.cn/showproblem.php?pid=7438)
~~抄了jiangly代码~~<br>
赛时没什么思路，还以为和上学期BIT校赛一样需要拆分立方，将他改造成可递推的模式<br>
看到题解中说相当于选三个序列，他们相同的方案数的时候才恍然大悟<br>
因为出现了多少次，就相当于在这么多里面选一次<br>
然后我们只需要求以$A_i, A_j, A_k$之前结尾的序列，方案数就可以了。
```cpp
void solve()
{
    int n = rd();
    const int mod = 998244353;
    vector<int> A(n + 1);
    vector<vector<vector<int>>> dp(n + 1, vector<vector<int>>(n + 1, vector<int>(n + 1)));
    for (int i = 1; i <= n; ++i)
        A[i] = rd();
    auto Add = [&](int &x, int y)
    {
        x += y;
        if (x >= mod)
            x -= mod;
        if (x < 0)
            x += mod;
    };
    dp[0][0][0] = 1;
    for (int i = 0; i <= n; ++i)
        for (int j = 0; j <= n; ++j)
            for (int k = 0; k <= n; ++k)
            {
                if (!i || !j || !k)
                    dp[i][j][k] = 1;
                else
                {
                    if (A[i] == A[j] && A[j] == A[k])
                        dp[i][j][k] = dp[i - 1][j - 1][k - 1];
                    Add(dp[i][j][k], dp[i - 1][j][k]);
                    Add(dp[i][j][k], dp[i][j - 1][k]);
                    Add(dp[i][j][k], dp[i][j][k - 1]);
                    Add(dp[i][j][k], -dp[i - 1][j - 1][k]);
                    Add(dp[i][j][k], -dp[i][j - 1][k - 1]);
                    Add(dp[i][j][k], -dp[i - 1][j][k - 1]);
                    Add(dp[i][j][k], dp[i - 1][j - 1][k - 1]);
                }
            }
    cout << dp[n][n][n] - 1 << '\n';
}
```
