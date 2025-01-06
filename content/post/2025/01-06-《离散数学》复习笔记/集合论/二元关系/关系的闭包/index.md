---
title: "关系的闭包"
slug: "01 06 《离散数学》复习笔记/集合论/二元关系/关系的闭包"
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

## 关系的闭包
需要改造 $R$ 为一个具有某种性质的关系，$R$ 的闭包是 $A$ 上具有该性质的关系中最小的一个 $R'$。即：
- $R'$ 具有该性质
- $R \subseteq R'$
- 对 $A$ 上任何具有该性质的关系 $S$，$R' \subseteq S$

$R$ 的自反闭包记作 $r(R) = R \cup R^{0} = R \cup I\_A$
$R$ 的对称闭包记作 $s(R) = R \cup R^{-1}$
$R$ 的传递闭包记作 $t(R) = R \cup R^2 \cup R^3 \cup \cdots$

对有穷集 $A(\left|A\right| = n)$，$R$ 的传递闭包 $t(R) = R \cup R^2 \cup \cdots \cup R^n$

### 矩阵表示
分别设 $R, r(R), s(R), t(R)$ 的关系矩阵为 $M, M\_r, M\_s, M\_t$，则
$$\begin{aligned}
M_r &= M + I
M_s &= M + M^T
M_t &= M + M^2 + M^3 + \cdots + M^n
\end{aligned}$$

### 图表示
- $r(R)$：在 $G\_R$ 中添加自环
- $s(R)$：在 $G\_R$ 中添加对称边
- $t(R)$：在 $G\_R$ 中添加传递边


### 闭包的性质
$R$ 是自反的 $\Leftrightarrow$ $r(R) = R$
$R$ 是对称的 $\Leftrightarrow$ $s(R) = R$
$R$ 是传递的 $\Leftrightarrow$ $t(R) = R$

若 $R\_1 \subseteq R\_2$，则
$r(R\_1) \subseteq r(R\_2)$
$s(R\_1) \subseteq s(R\_2)$
$t(R\_1) \subseteq t(R\_2)$

- $r(s(R)) = s(r(R))$
- $r(t(R)) = t(r(R))$
- $s(t(R)) \subseteq t(s(R))$
- $t(s(r(R))) = r(t(s(R))) = t(r(s(R)))$

| R | r(R) | s(R) | t(R) |
| :--: | :--: | :--: | :--: |
| 自反 | $\checkmark$ | $\checkmark$ | $\checkmark$ |
| 对称 | $\checkmark$ | $\checkmark$ | $\checkmark$ |
| 传递 | $\checkmark$ | $\times$ | $\checkmark$ |

