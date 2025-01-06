---
title: "环与域"
slug: "01 06 《离散数学》复习笔记/代数结构/群与环/环与域"
date: "2025-01-06T21:14:24+08:00"
lastmod: "2025-01-06T21:14:24+08:00"
hidden: true
description:
draft: false
math:
license:
author: "Ri-Nai"
categories: ["学习笔记"]
tags: ["离散数学", "计算机科学"]
---

## 环与域
### 环
设 $\langle R, +, \cdot \rangle$ 是一个代数系统，如果满足以下条件：
1. $\langle R, + \rangle$ 是一个**阿贝尔群**
2. $\langle R, \cdot \rangle$ 是一个**半群**
3. $\cdot$ 对 $+$ 满足**分配律**。
则称 $\langle R, +, \cdot \rangle$ 是一个**环**。

通常称 $+$ 为环 $R$ 的**加法**，$\cdot$ 为环 $R$ 的**乘法**。
环中加法单位元 记作 $0$，乘法单位元记作 $1$。

对任何元素 $x$，称其加法逆元为**负元**，记作 $-x$。
若 $x$ 存在乘法逆元，则称之为**逆元**，记作 $x^{-1}$。

$nx$ 表示 $n$ 个 $x$ 相加，$x^n$ 表示 $n$ 个 $x$ 相乘。

#### 环的实例
1. 关于普通加法和乘法封闭的环
    - 整数环 $\mathbb{Z}$
    - 有理数环 $\mathbb{Q}$
    - 实数环 $\mathbb{R}$
    - 复数环 $\mathbb{C}$
2. $oplus$ 和 $otimes$ 分别表示模 $n$ 加法和乘法的环 $\mathbb{Z}\_n$
3. $n$ 阶矩阵环 $M\_n(\mathbb{R})$
4. $P(B)$ 对称差和交的环

#### 环的性质
设 $\langle R, +, \cdot \rangle$ 是一个环
1. $\forall a \in R, 0 \cdot a = a \cdot 0 = 0$
2. $\forall a, b \in R, (-a)b = a(-b) = -ab$
3. $\forall a, b, c \in R, a(b - c) = ab - ac, (a - b)c = ac - bc$
4. $\displaystyle\forall a\_1, a\_2, \cdots, a\_n, b\_1, b\_2, \cdots, b\_m \in R, \sum\_{i=1}^n a\_i \sum\_{j=1}^m b\_j = \sum\_{i=1}^n \sum\_{j=1}^m a\_i b\_j$

#### 特殊的环
- **交换环**：满足乘法交换律的环
- **含幺环**：存在乘法单位元的环
- **无零因子环**：若 $ab = 0 \Rightarrow a = 0 \lor b = 0$ 的环
    - 当且仅当满足乘法消去律时，环是无零因子环
- **整环**：以上三个性质同时满足的环
- **域**：设 $R$ 是整环，且 $R$ 中至少含有两个元素，每个非零元都有乘法逆元，则称 $R$ 是一个**域**。
