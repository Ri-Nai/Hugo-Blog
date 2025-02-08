---
title: "等价关系"
slug: "2025/01 06 《离散数学》复习笔记/集合论/二元关系/等价关系"
date: "2025-01-06T22:32:26+08:00"
lastmod: "2025-01-06T22:32:26+08:00"
hidden: true
description:
draft: false
math:
license:
author: "Ri-Nai"
categories: ["学习笔记"]
tags: ["离散数学", "计算机科学"]
---

## 等价关系与划分
若 $R$ 是自反的、对称的、传递的，则称 $R$ 是等价关系。
设 $R$ 是一个等价关系，若 $xRy$，则称 $x$ 与 $y$ 是等价的，记作 $x \sim y$.

### 等价类
设 $R$ 是 $A$ 上的等价关系，$x \in A$，则
$$[x]\_R = \lbrace y \ | \ y \in A \land xRy \rbrace$$

$$\forall x \in A, [x]\_R \neq \varnothing, [x]\_R \subseteq A$$
$$\forall x, y \in A, [x]\_R \cap [y]\_R = \begin{cases} \varnothing & x \nsim y \newline [x]\_R & x \sim y \end{cases}$$
$$\bigcup \lbrace [x]\_R | x \in A \rbrace = A$$

### 商集与划分
$$A/R = \lbrace [x]\_R \ | \ x \in A \rbrace$$
实例：$A = \lbrace 1, 2, \cdots 8 \rbrace$，关于模 $3$ 同余的等价关系 $R$ 的商集 $A/R = \lbrace [1]\_R, [2]\_R, [3]\_R \rbrace = \lbrace \lbrace 1, 4, 7 \rbrace, \lbrace 2, 5, 8 \rbrace, \lbrace 3, 6 \rbrace \rbrace$

若 $A$ 的子集族 $\pi(\pi \subseteq P(A))$ 满足
- $\varnothing \notin \pi$
- $\bigcup \pi = A$
则称 $\pi$ 是 $A$ 的一个覆盖。

若 $A$ 的子集族 $\pi$ 是一个**覆盖**，且
- $\forall x \forall y(x, y \in \pi land x \neq y \to x \cap y = \varnothing)$
则称 $\pi$ 是 $A$ 的一个**划分**，$\pi$ 的元素称为 $A$ 的划分块。


集合 $A$ 上的一个等价关系 $R$ , 决定了 $A$ 的一个划分，该划分就是商集 $A/R$ 

集合 $A$ 的一个划分,确定 $A$ 的元素间的一个等价关系
