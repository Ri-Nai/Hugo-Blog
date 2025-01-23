---
title: "SAM(后缀自动机)学习笔记"
slug: "2024/08 07 SAM(后缀自动机)学习笔记"
description:
date: "2024-08-07T18:16:28+08:00"
lastmod: "2024-08-07T18:16:28+08:00"
#image: cover.png
math:
license:
hidden: false
draft: false
categories: ["学习笔记"]
tags: ["算法竞赛"]
---
## 模板（抄自**jiangly**）
```cpp
struct SAM
{
    static constexpr int ALPHABET_SIZE = 26;
    struct Node
    {
        int len;
        int link;
        std::array<int, ALPHABET_SIZE> next;
        Node() : len{}, link{}, next{} {}
    };
    std::vector<Node> t;
    SAM()
    {
        init();
    }
    SAM(string s)
    {
        init();
        int p = 1;
        for (char c : s)
            p = extend(p, c);
    }
    void init()
    {
        t.assign(2, Node());
        t[0].next.fill(1);
        t[0].len = -1;
    }
    int newNode()
    {
        t.emplace_back();
        return t.size() - 1;
    }
    int extend(int p, int c)
    {
        if (t[p].next[c])
        {
            int q = t[p].next[c];
            if (t[q].len == t[p].len + 1)
            {
                return q;
            }
            int r = newNode();
            t[r].len = t[p].len + 1;
            t[r].link = t[q].link;
            t[r].next = t[q].next;
            t[q].link = r;
            while (t[p].next[c] == q)
            {
                t[p].next[c] = r;
                p = t[p].link;
            }
            return r;
        }
        int cur = newNode();
        t[cur].len = t[p].len + 1;
        while (!t[p].next[c])
        {
            t[p].next[c] = cur;
            p = t[p].link;
        }
        t[cur].link = extend(p, c);
        return cur;
    }
    int extend(int p, char c, char offset = 'a')
    {
        return extend(p, c - offset);
    }

    int next(int p, int x)
    {
        return t[p].next[x];
    }

    int next(int p, char c, char offset = 'a')
    {
        return next(p, c - 'a');
    }

    int link(int p)
    {
        return t[p].link;
    }

    int len(int p)
    {
        return t[p].len;
    }

    int size()
    {
        return t.size();
    }
};
```
### 基本操作
#### move
用于直接用于子串匹配，跟着后缀自动机的节点走，失配就回到`link`结点，并且重置已匹配的最大长度
```cpp
void move(int &p, int &l, char c)
{
    while (!next(p, c))
        l = len(p = link(p));
    ++l;
    p = next(p, c);
}
```
#### del_head
用于删除头节点，在限制匹配长度的时候使用
```cpp
void del_head(int &p, int &l, int limit)
{
    if (l > limit && --l == len(link(p)))
        p = link(p);
}
```
#### Build_Ord
用于建立拓扑序，显然拓扑序在后面的最大后缀长度肯定大
```cpp
void Build_Ord()
{
    int m = size();
    vector<int> cnt(n + 1);
    ord.resize(m);
    for (int i = 1; i < m; ++i)
        ++cnt[t[i].len];
    for (int i = 1; i <= n; ++i)
        cnt[i] += cnt[i - 1];
    for (int i = 1; i < m; ++i)
        ord[cnt[t[i].len]--] = i;
    for (int i = m - 1; i >= 1; --i)
    {
        int p = ord[i];
        t[t[p].link].sz += t[p].sz;
    }
}
```
#### Build_Edge
建边，用于更直观的dfs遍历后缀树
```cpp
void Build_Edge()
{
    E.resize(size());
    for (int i = 2; i < size(); ++i)
        E[t[i].link].push_back(i);
}
```
## 理解及讲解
待更新
## 例题
### [P2408 不同子串的个数](https://www.luogu.com.cn/problem/P2408)
在插入的过程中加入一段就可以了，最后直接输出ans<br>
后缀树上每个点都代表等价类的子串的数量，`len - link.len`就是这段的包含的子串的数量，不会重复计算
```cpp
SAM(string s)
{
    init();
    int p = 1;
    ans = 0;
    for (char c : s)
    {
        p = extend(p, c);
        ans += t[p].len - t[t[p].link].len;
    }
}
```
### [P3804 【模板】后缀自动机（SAM）](https://www.luogu.com.cn/problem/P3804)
引入一个sz数组，表示这个等价类里有多少个endpos<br>
这个sz的初始化是直接根据字符串原先的前缀赋值的<br>
如果他是一个前缀，那他必定包含一个新的endpos，而不能直接按照常规的dfs一样给叶子结点赋值为1

这题要求求出$len \times cnt$的最大值，直接在dfs里做就好了
```cpp
string s;
cin >> s;
SAM S(s);
int n = s.size();
int m = S.size();
vector<vector<int>> E(m + 1);
vector<int> sz(m + 1);
for (int i = 0, p = 1; i < n; ++i)
    sz[p = S.next(p, s[i])] = 1;
for (int i = 2; i < m; ++i)
    E[S.t[i].link].push_back(i);
ll ans = 0;
auto dfs = [&](auto self, int u) -> void
{
    for (int v : E[u])
    {
        self(self, v);
        sz[u] += sz[v];
    }
    if (sz[u] > 1)
        ans = max(ans, 1ll * sz[u] * S.t[u].len);
};
dfs(dfs, 1);
cout << ans << '\n';
```
### [两个字符串的LCS（最长公共子串）](https://ac.nowcoder.com/acm/problem/237306)
其实是想做多个字符串的LCS的，但是交在洛谷上UE了🤗<br>
首先先是拿一个最小的字符串来建SAM，然后每个字符串去跑匹配，匹配不到就去link结点（就像AC自动机一样），并且重置当前的长度<br>
我们要对每个endpos的答案求最小值的最大值<br>
注意到我们每次求出的答案是在一个等价类上得到的，所以需要传递给它的link结点，这里写懒了直接dfs了（常数领域大神）
```cpp
void Build_Tree()
{
    E.resize(size());
    for (int i = 2; i < size(); ++i)
        E[t[i].link].push_back(i);
}
void modify(string s)
{
    int p = 1, l = 0;
    vector<int> mx(size());
    for (char c : s)
    {
        while (!next(p, c))
            p = link(p), l = len(p);
        int q = next(p, c);
        mx[q] = max(mx[q], ++l);
        p = q;
    }
    auto dfs = [&](auto self, int u) -> void
    {
        for (int v : E[u])
            self(self, v), mx[u] = max(mx[u], mx[v]);
        t[u].res = min(t[u].res, mx[u]);
    };
    dfs(dfs, 1);
}
int get_res()
{
    int res = 0;
    for (int i = 1; i < size(); ++i)
        res = max(res, t[i].res);
    return res;
}

void solve()
{
    vector<string> S;
    string tmp;
    while (cin >> tmp)
        S.push_back(tmp);
    sort(S.begin(), S.end(),
            [&](string s1, string s2)
            {
                return s1.size() < s2.size();
            });
    SAM str(S[0]);
    for (int i = 1; i < S.size(); ++i)
        str.modify(S[i]);
    int ans = str.get_res();
    cout << ans << '\n';
}
```

### [P3975 [TJOI2015] 弦论](https://www.luogu.com.cn/problem/P3975)
这题要求求第k大的子串，由于从根节点开始，每个结点就直接指向了一个子串<br>
我们这个遍历的路径就实际相当于线段树上二分<br>
如果`t = 0`的话就是给每个点的sz设置成1，否则就为sz<br>
然后我们应该开一个新的dp数组用来存这个结点下面有多少个子串，可以拓扑排序，也可以dfs<br>
细节比较多，譬如根节点不应该有sz，然后最后那里的的`while (k > 0)`不能直接写成`while (k)`， 否则因为`k <= num`，有可能sz会直接把`k`减到0
```cpp
void work(int k)
{
    int m = size();
    vector<ll> num(m);
    for (int i = m - 1; i >= 1; --i)
    {
        int p = ord[i];
        if (p != 1)
            num[p] = t[p].sz;
        for (int j = 0; j < 26; ++j)
        {
            int q = next(p, j);
            if (q)
                num[p] += num[q];
        }
    }
    if (num[1] < k)
        End(-1);
    int now = 1;
    while (k > 0)
    {
        for (int i = 0; i < 26; ++i)
        {
            int nxt = next(now, i);
            if (k <= num[nxt])
            {
                putchar(i + 'a');
                now = nxt;
                k -= t[nxt].sz;
                break;
            }
            k -= num[next(now, i)];
        }
    }
}

void solve()
{
    string s;
    int t, k;
    cin >> s;
    cin >> t >> k;
    SAM S(s);
    S.Build_ord(t);
    S.work(k);
}
```
### [CF235C Cyclical Quest](http://codeforces.com/problemset/problem/235/C)
题目大意是求出主串内有多少个子串是存在于给出的多个循环同构子串的<br>
这nm不是，前几天杭电多校吗，下次请标明出处<br>
~~但是我修改了代码去交杭电多校MLE了，逆天~~<br>
这题还是加强挺多的了感觉，因为有多次询问，hash显得不大现实，然后SA也显得比较难操作<br>
这里用SAM就好了<br>

使用上面给出的删除头节点的操作，我们就可以限制当前匹配串的长度<br>
然后统计答案的时候，只需要标记一下vis就可以了<br>
```cpp
string s;
cin >> s;
SAM S(s);
S.Build_ord();
int q;
cin >> q;
vector<int> vis(S.size());
for (int Q = 1; Q <= q; ++Q)
{
    string t;
    cin >> t;
    int p = 1, l = 0;
    ll ans = 0;
    for (int i = 0; i < t.size(); ++i)
    {
        while (!S.next(p, t[i]))
            p = S.link(p), l = S.len(p);
        ++l;
        p = S.next(p, t[i]);
    }
    for (int i = 0; i < t.size(); ++i)
    {
        if (l >= t.size())
        {
            --l;
            if (l == S.len(S.link(p)))
                p = S.link(p);
        }
        while (!S.next(p, t[i]))
            p = S.link(p), l = S.len(p);
        p = S.next(p, t[i]);
        ++l;
        if (vis[p] < Q && l == t.size())
        {
            vis[p] = Q;
            ans += S.t[p].sz;
        }
    }
    cout << ans << '\n';
}
```
由于这个题我才想起来要把move写到我的模板里<br>
### [[AHOI2013] 差异](https://www.luogu.com.cn/problem/P4248)
求$\displaystyle\sum_{1 \le i < j \le n}{len(T_i) + len(T_j) - 2 \times lcp(T_i, T_j)}$<br>
前两个的值可以直接算，可以直接$n ^ 2$预处理，也可以像我一样偷式子算出来是$\frac{n(n + 1)(n - 1)}{2}$<br>
从而就是算后面的部分了<br>
后面$lcp$的部分肯定是后缀数组相关的比较好写<br>
但是这里是SAM，所以我们就要用SAM的方式去做<br>
引理：反建SAM后的出来的parent树，就是后缀树了<br>
以$u$为$LCA$的点对，其$lcp$也就是$u$的前缀，即$len(u)$<br>
然后只需要dfs求和就好了<br>
```cpp
ll work()
{
    ll res = 0;
    auto dfs = [&](auto self, int u) -> void
    {
        for (auto v : E[u])
        {
            self(self, v);
            res += 1ll * sz(u) * sz(v) * len(u);
            t[u].sz += sz(v);
        }
    };
    dfs(dfs, 1);
    return res;
}

cout << 1ll * n * (n + 1)  * (n - 1) / 2 - ans * 2 << '\n';
```
