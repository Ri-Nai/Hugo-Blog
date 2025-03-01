---
title: "函数"
slug: "2025/01/06/《离散数学》复习笔记/集合论/函数"
date: "2025-01-06T13:41:15+08:00"
lastmod: "2025-01-06T13:41:15+08:00"
hidden: true
description:
draft: false
math:
license:
author: "Ri-Nai"
categories: ["学习笔记"]
tags: ["离散数学", "计算机科学"]
---

## 函数的定义
设 $F$ 为 {{< linking "集合论/二元关系/二元关系的性质#二元关系|二元关系" >}}，若 $F$ 满足 $\forall x \in \mathrm{dom}F$ 都存在唯一的 $y \in \mathrm{ran}F$ 使 $xFy$ 成立，则称 $F$ 为**函数** 。
对于函数 $F$，若有 $xFy$，则记作 $y = F(x)$，并称 $y$ 为 $F$ 在 $x$ 处的**值**

### 函数相等
$$F = G \Leftrightarrow F \subseteq G \land G \subseteq F \Leftrightarrow \mathrm{dom}F = \mathrm{dom}G \land \forall x (x \in \mathrm{dom}F \to F(x) = G(x))$$

设 $A$ 和 $B$ 是两个集合，$f$ 为函数， $\mathrm{dom}F = A$，$\mathrm{ran}F \subseteq B$，则称 $f$ 为从 $A$ 到 $B$ 的函数，记作 $f: A \to B$ 。

### 从 $A$ 到 $B$ 的函数的集合

所有从 $A$ 到 $B$ 的函数的集合记作 $B^A$。
$$B^A = \lbrace f \ | \ f: A \to B \rbrace$$
$$\left|B^A\right| = \left|B\right|^{\left|A\right|}$$

特别地：
$A = \varnothing$，则 $B^A = B^\varnothing = \lbrace \varnothing \rbrace$
$A \ne \varnothing$ 且 $B = \varnothing$，则 $B^A = \varnothing^A = \varnothing$

### 函数的像和完全原像
设 $f: A \to B$，$A\_1 \subseteq A$，$B\_1 \subseteq B$，则
1. $A\_1$ 在 $f$ 下的**像**为 $f(A\_1) = \lbrace f(x) \ | \ x \in A\_1 \rbrace$
2. $B\_1$ 在 $f$ 下的**完全原像**为 $f^{-1}(B\_1) = \lbrace x \ | \ f(x) \in B\_1 \rbrace$

像和函数值的区别：
$f(x) \in B$，$f(A\_1) \subseteq B$

$$\begin{aligned}
f^{-1}(f(A\_1)) \neq A\_1, \quad A\_1 \subseteq f^{-1}(f(A\_1)) \newline 
f(f^{-1}(B\_1)) \neq B\_1, \quad f(f^{-1}(B\_1)) \subseteq B\_1
\end{aligned}$$
前者是因为 $f$ 不一定是单射，后者是因为 $f$ 不一定是满射。

### 函数的性质
- **单射**：$\forall x\_1, x\_2 \in \mathrm{dom}F, F(x\_1) = F(x\_2) \Leftrightarrow x\_1 = x\_2$
- **满射**：$\mathrm{ran}F = B$
- **双射**：若 $f$ 既是单射又是满射，则称 $f$ 为**双射**的。

### 某些重要函数
1. **常函数**：$f: A \to B$，$\forall x \in A, f(x) = b$，称 $f$ 为**常函数**。
2. **恒等函数**：$I\_A = \lbrace <x, x> \ | \ x \in A \rbrace$，$I\_A$ 是 $A$ 上的函数，称为**恒等函数**。
3. **单调函数**：$\langle A, \preceq \rangle$ 和 $\langle B, \preceq \rangle$ 是两个偏序集，$f: A \to B$。
    - 若 $\forall x\_1, x\_2 \in A, x\_1 \preceq x\_2 \Rightarrow f(x\_1) \preceq f(x\_2)$，则称 $f$ 为**单调递增函数**。
    - 若 $\forall x\_1, x\_2 \in A, x\_1 \prec x\_2 \Rightarrow f(x\_1) \prec f(x\_2)$，则称 $f$ 为**严格单调递增函数**。
    - 类似的，可以定义**单调递减函数**和**严格单调递减函数**。
4. **特征函数**：$A$ 是集合，对任意的 $A' \subseteq A$，定义 $f: A \to \lbrace 0, 1 \rbrace$，$f(x) = \begin{cases} 1, & x \in A'  \newline  0, & x \notin A' \end{cases}$，称 $f$ 为 $A'$ 的**特征函数**，记为 $\chi\_{A'}$。不同的子集对应不同的特征函数。  
5. **自然映射**：设 $R$ 是集合 $A$ 上的等价关系，$g: A \to A/R$，$g(x) = [x]\_R$，称 $g$ 为 $A$ 到 $A/R$ 的**自然映射**。

不同的等价关系确定不同的自然映射  
恒等关系确定的自然映射是双射  
其他自然映射一般来说只是满射  

## 函数的运算
### 复合运算
若 $f$ 和 $g$ 是函数，则 $h = f \circ g$ 也是函数，满足：
1. $\mathrm{dom}h = \lbrace x \ | \ x \in \mathrm{dom}f \land f(x) \in \mathrm{dom}g \rbrace$
2. $\forall x \in \mathrm{dom}h, h(x) = g(f(x))$

#### 复合运算的性质
1. 若 $f: A \to B$ 是单射的，$g: B \to C$ 是单射的，则 $g \circ f: A \to C$ 是单射的。
2. 若 $f: A \to B$ 是满射的，$g: B \to C$ 是满射的，则 $g \circ f: A \to C$ 是满射的。
3. 若 $f: A \to B$ 是双射的，$g: B \to C$ 是双射的，则 $g \circ f: A \to C$ 是双射的。

上述的逆命题都不一定成立。

设 $f: A \to B$，则 $f = f \circ I\_B = I\_A \circ f$。

### 反函数
1. 函数 $f$ 的逆 $f^{-1}$ 不一定是函数，只是个二元关系
2. 单射函数的逆是函数，且 $f: A \to B$ 的逆函数 $f^{-1}$ 是 $\mathrm{ran}f$ 到 $A$ 的双射函数。
3. 双射函数 $f: A \to B$ 的逆是在 $B$ 到 $A$ 的双射函数。

对双射函数 $f: A \to B$
$$f^{-1} \circ f = I\_A, \quad f \circ f^{-1} = I\_B$$

## 集合的等势
设 $A$ 和 $B$ 是两个集合，若存在双射函数 $f: A \to B$，则称 $A$ 和 $B$ 是**等势**的，记作 $A \approx B$。

1. $A \approx A$
2. 若 $A \approx B$，则 $B \approx A$
3. 若 $A \approx B$ 且 $B \approx C$，则 $A \approx C$

实例：
- $\mathbb{N} \approx \mathbb{Z} \approx \mathbb{Q} \approx \mathbb{N \times N}$
- $a, b \in \mathbb{R}, a < b$，$(a, b) \approx (a, b] \approx [a, b] \approx [a, b) \approx \mathbb{R}$
    - 以 $[0, 1] \approx (0, 1)$ 为例。
    - $A = {0, 1, 1 / 2, 1 / 3, \cdots} \subset [0, 1]$
    - $B = {1 / 2, 1 / 3, 1 / 4, \cdots} \subset (0, 1)$
    - 关键在于构造双射函数 $f: A \to B$，$f(x) = x / (x + 2)$
- $P(A) \approx \lbrace0, 1\rbrace^A$，$P(A)$ 是 $A$ 的幂集，$\lbrace 0, 1 \rbrace^A$ 是 $A$ 到 $\lbrace 0, 1 \rbrace$ 的函数集合。双射函数为 $f: P(A) \to {0, 1}^A$，$f(A') = \chi\_{A'}$


### 康托定理
1. $\mathbb{N} \not\approx \mathbb{R}$
2. $A \not \approx P(A)$

#### 证明
1. **定义基数**：如果两个集合之间存在双射（双向一一对应），则称这两个集合等势，表示为它们的基数相同。我们希望证明 $\mathbb{N}$ 和 $\mathbb{R}$ 不等势，换句话说，$\mathbb{R}$ 的基数大于 $\mathbb{N}$ 的基数。

2. **假设反证法**：假设 $\mathbb{R}$ 和 $\mathbb{N}$ 等势，也就是说，假设存在一个从 $\mathbb{N}$ 到 $\mathbb{R}$ 的双射 $f \colon \mathbb{N} \to \mathbb{R}$。这样，所有实数可以被自然数“列举”出来。

3. **使用康托尔对角线法则**：我们接下来将通过对角线法则，展示出在 $\mathbb{R}$ 中总有一个实数无法通过 $f$ 来与自然数一一对应，从而得出矛盾。

      - 考虑单位区间 $[0, 1]$ 中的实数，可以表示为无限小数（例如：0.123456...）。
      - 假设我们能够通过 $f$ 列出这些实数：$f(1), f(2), f(3), \dots$，其中每个 $f(n)$ 都表示 $[0,1]$ 中的一个实数，其小数部分为 $f(n) = 0.a\_{n1}a\_{n2}a\_{n3}\dots$，其中 $a\_{ni}$ 表示第 $n$ 个数的第 $i$ 位小数。
      - 现在通过对角线法构造一个新的实数 $r$，使得 $r$ 的第 $i$ 位小数 $b\_i$ 与 $f(i)$ 的第 $i$ 位小数 $a\_{ii}$ 不同。例如：可以令 $b\_i$ 取值为 $9$（若 $a\_{ii} \neq 9$），或 $8$（若 $a\_{ii} = 9$）。
      - 由于 $r$ 的每一位与对应的 $f(i)$ 在第 $i$ 位不同，因此 $r \neq f(i)$ 对所有 $i$ 都成立。

4. **矛盾产生**：这个通过对角线法构造出来的 $r$ 在 $[0, 1]$ 中，但根据假设，$f$ 应该是一个双射，也就是说，应该能够“列举”出所有实数。然而，$r$ 不在这列举出来的实数序列中，这与 $f$ 为双射的假设矛盾。

因此，假设 $\mathbb{N}$ 和 $\mathbb{R}$ 等势是错误的，$\mathbb{R}$ 的基数严格大于 $\mathbb{N}$ 的基数。

### 集合的优势
设 $A$ 和 $B$ 是两个集合，若存在单射函数 $f: A \to B$，则称 $B$ **优势于** $A$，记作 $A \preccurlyeq\cdot B$。如果 $B$ 不优势于 $A$，则记作 $B \not\preccurlyeq\cdot A$。

设 $A$ 和 $B$ 是两个集合，若 $A \preccurlyeq\cdot B$ 且 $A \not\approx B$，则称 $B$ **真优势于** $A$，记作 $A \prec\cdot B$。如果 $B$ 不真优势于 $A$，则记作 $B \not\prec\cdot A$。

实例：
- $\mathbb{N} \preccurlyeq\cdot \mathbb{N}, \mathbb{N} \preccurlyeq\cdot \mathbb{R}, A \preccurlyeq\ P(A)$
- $\mathbb{R} \not\preccurlyeq\cdot \mathbb{N}$
- $\mathbb{N} \prec\cdot \mathbb{R}, \mathbb{N} \not\prec\cdot \mathbb{N}, A \prec\cdot P(A)$

#### 性质
1. $A \preccurlyeq\cdot A$
2. $A \preccurlyeq\cdot B \land B \preccurlyeq\cdot C \Rightarrow A \preccurlyeq\cdot C$
3. $A \preccurlyeq\cdot B \land B \preccurlyeq\cdot A \Rightarrow A \approx B$

式 3. 可以用于构造两个单射函数证明两个集合等势。

{{< linkingImage "证明等势1.png" >}}
{{< linkingImage "证明等势2.png" >}}

## 自然数的集合定义
$a^+ = a \cup \lbrace a \rbrace$，称 $a^+$ 为 $a$ 的**后继**。
$$\begin{aligned}
0 &= \varnothing \newline 
1 &= 0^+ = \lbrace 0 \rbrace = \lbrace \varnothing \rbrace \newline 
2 &= 1^+ = \lbrace 0, 1 \rbrace = \lbrace \varnothing, \lbrace 0 \rbrace \rbrace \newline 
3 &= 2^+ = \lbrace 0, 1, 2 \rbrace = \lbrace \varnothing, \lbrace 0 \rbrace, \lbrace 0, 1 \rbrace \rbrace \newline 
\cdots
\end{aligned}$$

### 有穷集与无穷集
一个集合是 **有穷的** 当且仅当它与某个自然数等势。否则，它是 **无穷的**。
实例：
1. $\lbrace a, b, c \rbrace$ 是有穷集，与 $3 = \lbrace 0, 1, 2 \rbrace$ 等势。
2. $\mathbb{N}$ 和 $\mathbb{R}$ 是无穷集。

任何有穷集只与某个自然数等势，而无穷集与任何自然数都不等势。

### 集合基数
1. 对于有穷集 $A$，$A$ 的基数是 $\mathrm{card}A = n \Leftrightarrow A \approx n$，称 $n$ 为集合 $A$ 的**基数**。
2. 自然数集合 $\mathbb{N}$ 的基数是 $\aleph\_0$
3. 实数集 $\mathbb{R}$ 的基数是 $\aleph$

#### 集合基数的性质
1. $\mathrm{card}A = \mathrm{card}B \Leftrightarrow A \approx B$
2. $\mathrm{card}A \le \mathrm{card}B \Leftrightarrow A \preccurlyeq\cdot B$
3. $\mathrm{card}A < \mathrm{card}B \Leftrightarrow A \prec\cdot B$

$$\begin{aligned}
\mathrm{card}\mathbb{Z} = \mathrm{card}\mathbb{N} &= \mathrm{card}\mathbb{Q} = \mathrm{card}\mathbb{N \times N} = \aleph\_0 \newline 
\mathrm{card}\mathbb{R} = \mathrm{card}[a, b] = \mathrm{card}(c, d) &= \mathrm{card} P(N) = \mathrm{card} 2^\mathbb{N} = \aleph \newline 
\end{aligned}$$
有 $\aleph\_0 < \aleph$

若 $\mathrm{card}A \le aleph\_0$，则称 $A$ 是**可数的**，否则称 $A$ 是**不可数的**。

