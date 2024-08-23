---
title: "SA(后缀数组)学习笔记"
slug: "07 19 SA(后缀数组)学习笔记"
description:
date: "2024-07-19T02:50:38+08:00"
lastmod: "2024-07-19T02:50:38+08:00"
#image: cover.png
math:
license:
hidden: false
draft: false
categories: ["学习笔记"]
tags: ["算法竞赛"]
---
## 模板
```cpp
#include <bits/stdc++.h>
using namespace std;
struct SA_Array
{
    int n;
    string S;
    vector<int> SA, height, rk, lg2;
    vector<vector<int>> ST;
    SA_Array(string T) : n(T.size()), SA(n + 1), rk(n + 1), height(n + 1),
                         ST(n + 1), lg2(n + 1)

    {
        S = T;
        S.push_back(0);
        for (int i = n; i >= 1; --i)
            S[i] = S[i - 1];
        S[0] = 0;
        init_SA();
        init_height();
        init_ST();
    }
    void init_SA()
    {
        int m = 128;
        vector<int> cnt(m + 1), X(n + 1), Y(n + 1);
        for (int i = 1; i <= n; ++i)
            ++cnt[X[i] = S[i]];
        for (int i = 1; i < m; ++i)
            cnt[i] += cnt[i - 1];
        for (int i = n; i >= 1; --i)
            SA[cnt[X[i]]--] = i;
        for (int l = 1; l < n; l <<= 1)
        {
            int tot = 0;
            for (int i = n - l + 1; i <= n; ++i)
                Y[++tot] = i;
            for (int i = 1; i <= n; ++i)
                if (SA[i] > l)
                    Y[++tot] = SA[i] - l;
            cnt.assign(m + 1, 0);
            for (int i = 1; i <= n; ++i)
                ++cnt[X[i]];
            for (int i = 1; i <= m; ++i)
                cnt[i] += cnt[i - 1];
            for (int i = n; i >= 1; --i)
                SA[cnt[X[Y[i]]]--] = Y[i];
            swap(X, Y);
            m = 0;
            for (int i = 1; i <= n; ++i)
                X[SA[i]] = (m += !(Y[SA[i]] == Y[SA[i - 1]] && Y[SA[i] + l] == Y[SA[i - 1] + l]));
            if (m == n)
                break;
        }
        rk.assign(X.begin(), X.begin() + n + 1);
    }
    void init_height()
    {
        for (int i = 1, k = 0; i <= n; ++i)
        {
            if (rk[i] == 1)
                continue;
            if (k)
                --k;
            int j = SA[rk[i] - 1];
            while (j + k <= n && i + k <= n && S[i + k] == S[j + k])
                ++k;
            height[rk[i]] = k;
        }
    }
    void init_ST()
    {
        lg2[1] = 0;
        for (int i = 2; i <= n; ++i)
            lg2[i] = lg2[i >> 1] + 1;
        for (int i = 1; i <= n; ++i)
            ST[i].resize(lg2[n] + 1 ), ST[i][0] = height[i];
        for (int j = 0; j < lg2[n]; ++j)
            for (int i = 1; i + (1 << j) <= n; ++i)
                ST[i][j + 1] = min(ST[i][j], ST[i + (1 << j)][j]);
    }
    int Query_LCP(int l, int r)
    {
        if (l == r)
            return n - l + 1;
        l = rk[l], r = rk[r];
        if (l > r)
            swap(l, r);
        ++l;
        int p = lg2[r - l + 1];
        return min(ST[l][p], ST[r - (1 << p) + 1][p]);
    }
    int Query_Range(int l1, int r1, int l2, int r2)
    {
        int len = min(r1 - l1, r2 - l2);
        int ans = Query_LCP(l1, l2);
        return min(len, ans);
    }
};
```
## 理解及讲解
待更新
## 例题
### [本质不同的子串的个数](https://ac.nowcoder.com/acm/problem/237304)
所有后缀的**所有前缀**即为所有子串<br>
排序后相邻两个后缀的**最长前缀**就是这两个后缀产生的**重叠子串的个数**<br>
只需要在总的串数目中减去这些就好了<br>
而如果不相邻的后缀的LCP, 必然是在他们之间的LCP里出现过的, 所以是已经被减掉了<br>
```cpp
int main()
{
    string s;
    cin >> s;
    SA_Array S(s);
    int n = s.size();
    typedef long long ll;
    ll ans = n * (n + 1) >> 1;
    for (int i = 1; i <= n; ++i)
        ans -= S.height[i];
    cout << ans << '\n';
}
```
### [两个字符串的LCS（最长公共子串）](https://ac.nowcoder.com/acm/problem/237306)
这里就涉及到后缀数组的一个比较重要的操作了<br>
把两个字符串拼接起来，**并在中间插入一个不存在的字符**<br>
这个不存在很重要，不然height数组会因为**第二个字符串的前缀**的存在而导致错误<br>
然后呢**只需要**将**交接处**的答案统计就好了<br>
**为什么只需要交界处呢？**<br>
交界处后面如果连一堆相同的，那**必然**是交界处的最大<br>
而我们只需要求**最长**<br>
```cpp
int main()
{
    string s, t;
    cin >> s >> t;
    SA_Array S(s + "!" + t);
    int n = s.size(), m = t.size();
    int ans = 0;
    for (int i = 2; i <= n + m + 1; ++i)
        if ((S.SA[i] <= n) ^ (S.SA[i - 1] <= n))
            ans = max(ans, S.height[i]);
    cout << ans << '\n';
}
```
### [两个字符串的本质不同的子串的个数](https://ac.nowcoder.com/acm/problem/237308)
抄了神人的代码👍👍👍<br>
原理还是比较复杂的，可能这道题和上面那道题都更适合用SAM（我还没学😭）<br>
过了两天来重新复习一下这道题发现还是很难理解<br>
注意到一个后缀有相邻的两个后缀<br>
如果我们选择去计算所有height的和去统计共同子串的个数，我们会计算某个后缀的不同的前缀两次，这显然是我们不希望发生的<br>
首先按照height大小**降序**排序，这样可以保证先计算出更长的前缀<br>
然后使用并查集标记使用过的后缀，最后得到的相当于是一段一段区间拼起来<br>
当两个区间拼起来的时候，如果两边都有**统计过答案**，就减去当前的LCP，毕竟这个被算了两次<br>


```cpp
int main()
{
    string s, t;
    cin >> s >> t;
    int n = s.size();
    int m = t.size();
    int p = n + m + 1;
    SA_Array S(s + "$" + t);
    vector<int> fa(p + 1), state(p + 1);
    for (int i = 1; i <= p; ++i)
        fa[i] = i, state[i] = 1 << (i <= n);
    auto find = [&](int u)
    {
        while (fa[u] ^ u)
        {
            fa[u] = fa[fa[u]];
            u = fa[u];
        }
        return u;
    };
    long long ans = 0;
    vector<vector<int>> E(p + 1);
    for (int i = 2; i <= p; ++i)
        E[S.height[i]].push_back(i);
    for (int i = p; i >= 0; --i)
        for (int x : E[i])
        {
            int u = S.SA[x], v = S.SA[x - 1];
            int val = S.height[x];
            u = find(u), v = find(v);
            if (state[u] == 3 && state[v] == 3)
                ans -= val;
            if (state[u] + state[v] == 3)
                ans += val;
            fa[v] = u;
            state[u] |= state[v];
        }
    cout << ans << '\n';
}

```
另一种方法是直接扫一遍，交界处相加，再减去两交界处同串之间的LCP，因为这些也是被算两次的量<br>
其实和上面那种很类似，还是这种好理解点😋
```cpp
    int now1 = 0, now2 = 0;
    for (int i = 2; i <= p; ++i)
    {
        now1 = min(now1, S.height[i]);
        now2 = min(now2, S.height[i]);
        if (S.SA[i] > n && S.SA[i - 1] <= n)
            ans += (now2 = S.height[i]) - now1, now1 = 0;
        if (S.SA[i] <= n && S.SA[i - 1] > n)
            ans += (now1 = S.height[i]) - now2, now2 = 0;
    }
```
### [循环位移](https://acm.hdu.edu.cn/showproblem.php?pid=7433)
前两天多校打的题，题解在[多校博客](/p/07-20-2024杭电多校第一场/#t1-循环位移httpsacmhdueducnshowproblemphppid7433)里了
