---
title: "二元关系的性质"
slug: "2025/01/06/《离散数学》复习笔记/集合论/二元关系/二元关系的性质"
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
## 有序对与笛卡尔积
### 有序对
由两个元素 $x$ 和 $y$，按照一定的顺序组成的二元组称为有序对，记作 $\langle x,y \rangle$.

有序对性质：
- 有序性：$<x,y> \neq  \langle y,x \rangle$
- 相等性：$<x,y> = <u,v> \Leftrightarrow x = u \land y = v$

### 笛卡尔积
$$A \times B = \lbrace <x,y> \ | \ x \in A \land y \in B \rbrace$$

笛卡尔积的性质：
- 不适合交换律：
- 不适合结合律：
- 对于并和交运算满足分配律：
$$A \times (B \cup C) = (A \times B) \cup (A \times C)$$
$$A \times (B \cap C) = (A \times B) \cap (A \times C)$$
- $A \times \varnothing = \varnothing \times B = \varnothing$
- $\left|A \times B\right| = \left|A\right| \times \left|B\right|$

## 二元关系
### 二元关系的定义
集合 $R$ 称为一个二元关系，当：
- $R$ 是空集
- $R$ 中的所有元素都是有序对
若 $<x,y> \in R$，则称 $x$ 与 $y$ 有关系 $R$，记作 $xRy$.
若 $<x,y> \notin R$，则称 $x$ 与 $y$ 无关系 $R$，记作 $x \cancel{R} y$.

设 $A$ 和 $B$ 是两个集合，$A \times B$ 的任意子集所定义的二元关系称为从 $A$ 到 $B$ 的二元关系.
当 $A = B$ 时，称为 $A$ 上的二元关系.

### 重要关系的实例
设 $A$ 为集合
- **空关系**：$\varnothing$ 是 $A$ 上的关系，称为**空关系**
- **全域关系**：$E\_A = \lbrace <x, y> \ | \ x in A \land y \in A \rbrace = A \times A$ 是 $A$ 上的关系，称为**全域关系**
- **相等关系**：$I\_A = \lbrace <x, x> \ | \ x \in A \rbrace$ 是 $A$ 上的关系，称为**相等关系**
- **小于等于关系**：$L\_A = \lbrace <x, y> \ | \ x, y \in A \land x \leq y \rbrace$ 是 $A$ 上的关系，称为**小于等于关系**
- **整除关系**：$D\_A = \lbrace  <x, y> \ | \ x, y \in A \land x | y  \rbrace$ 是 $A$ 上的关系，称为**整除关系**
- **包含关系**：$R\_\subseteq = \lbrace <x, y> \ | \ x, y \in A \land x \subseteq y \rbrace$ 是 $A$ 上的关系，称为**包含关系**

### 关系的表示
#### 关系矩阵
$A = \lbrace x\_1, x\_2, \cdots, x\_m \rbrace$，$B = \lbrace y\_1, y\_2, \cdots, y\_n \rbrace$，$R$ 是 $A$ 到 $B$ 的关系，$R$ 的关系矩阵是一个 $m \times n$ 的布尔矩阵 $M\_R = [r\_{ij}]\_{m \times n}$，其中
$$r\_{ij} = 1 \Leftrightarrow x\_i R y\_j$$

#### 关系图
$G\_R = (A, R)$，$A$ 是顶点集，$R$ 是边集，$R$ 是 $A$ 到 $A$ 的关系，$G\_R$ 是一个有向图.

关系矩阵适合表示从 $A$ 到 $B$ 的关系或 $A$ 上的关系（ $A$，$B$ 为有穷集）
关系图适合表示有穷集 $A$ 上的关系 

## 关系的运算
- **定义域**：$\mathrm{dom}R = \lbrace x \ | \ \exists y(xRy) \rbrace$
- **值域**：$\mathrm{ran}R = \lbrace y \ | \ \exists x(xRy) \rbrace$
- **域**：$fldR = \mathrm{dom}R \cup \mathrm{ran}R$

- **逆运算**：$R^{-1} = \lbrace <y, x> \ | \ <x, y> \in R \rbrace$
- **复合运算**：$R \circ S = \lbrace <x, z> \ | \ \exists y(xRy \land ySz) \rbrace$
    - $R \circ S \neq S \circ R$
- **幂运算**：
$$R^n = \begin{cases}
{<x, x> \ | \ x \in A} = I\_A & n = 0 \newline 
R \circ R^{n-1} & n > 0
\end{cases}$$

- **限制**：$R \upharpoonright A = R \cap (A \times A) = \lbrace <x, y> \ | \ <x, y> \in R \land x \in A \rbrace$
    - $R$ 在 $A$ 上的限制 $R \upharpoonright A$ 是 $R$ 在 $A$ 上的部分，是 $R$ 的子关系，即 $R \upharpoonright A \subseteq R$
- **像**：$R[A] = \lbrace y \ | \ \exists x(x \in A \land xRy) \rbrace = \mathrm{ran}(R \upharpoonright A)$
    - A 在 $R$ 下的像 $R[A]$ 是 $\mathrm{ran}R$ 的子集，即 $R[A] \subseteq \mathrm{ran}R$           

	
#### 关系的运算性质
- 逆运算的逆运算：$(F^{-1})^{-1} = F$
- 逆运算的域：$\mathrm{dom}R^{-1} = \mathrm{ran}R, \quad \mathrm{ran}R^{-1} = \mathrm{dom}R$

- 复合运算的逆运算：$(F \circ G)^{-1} = G^{-1} \circ F^{-1}$
- 复合运算的结合律：$(F \circ G) \circ H = F \circ (G \circ H)$
- 复合运算的分配律：
$$\begin{aligned}
F \circ (G \cup H) = (F \circ G) \cup (F \circ H) & & 
(G \cup H) \circ F = (G \circ F) \cup (H \circ F) \newline 
F \circ (G \cap H) \subseteq (F \circ G) \cap (F \circ H)& & 
F \circ (G \cap H) \supseteq (F \circ G) \cap (F \circ H)
\end{aligned}$$
可以推广到有限个集合的并和交

- 相等关系上的复合运算：$I\_A \circ R = R \circ I\_A = R$

- 限制与像运算的分配律：
$$\begin{aligned}
F \upharpoonright (A \cup B) &= F \upharpoonright A \cup F \upharpoonright B &
F \upharpoonright (A \cap B) &= F \upharpoonright A \cap F \upharpoonright B \newline 
F [A \cup B] &= F[A] \cup F[B] &
F [A \cap B] &\subseteq F[A] \cap F[B]
\end{aligned}$$

#### 幂运算的性质
不同的幂运算只有有限个

$$R^m \circ R^n = R^{m+n}$$
$$(R^m)^n = R^{mn}$$

## 关系的性质
- **自反性**：$R$ 是自反的，当 $\forall x(x \in A \to xRx)$
- **反自反性**：$R$ 是反自反的，当 $\forall x(x \in A \to x \cancel{R} x)$
- **对称性**：$R$ 是对称的，当 $\forall x \forall y(xRy \to yRx)$
- **反对称性**：$R$ 是反对称的，当 $\forall x \forall y(xRy \land yRx \to x = y)$

- **传递性**：$R$ 是传递的，当 $\forall x \forall y \forall z(xRy \land yRz \to xRz)$

| 表示 | 自反 | 反自反 | 对称 | 反对称 | 传递 |
| :--: | :--: | :----: | :--: | :----: | :--: |
| 集合表达式 | $I\_A \subseteq R$ | $I\_A \cap R = \varnothing$ | $R = R^{-1}$ | $R \cap R^{-1} \subseteq I\_A$ | $R \circ R \subseteq R$ |
| 关系矩阵 | 对角线全为 1 | 对角线全为 0 | 对称 | $r\_{ij} + r\_{ji} \leq 1$ | $r\_{ij} = 1 \land r\_{jk} = 1 \Rightarrow r\_{ik} = 1$ |
| 关系图 | 每个顶点都有自环 | 没有自环 | 无向图对称 | 有向图 | 有向图传递 |

|       运算        |      自反      |     反自反      |      对称      |     反对称      |      传递      |
| :-------------: | :----------: | :----------: | :----------: | :----------: | :----------: |
|   $R\_1^{-1}$    | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ |
| $R\_1 \cap R\_2$  | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ |
| $R\_1 \cup R\_2$  | $\checkmark$ | $\checkmark$ | $\checkmark$ |   $\times$   |   $\times$   |
|   $R\_1 - R\_2$   |   $\times$   | $\checkmark$ | $\checkmark$ | $\checkmark$ |   $\times$   |
| $R\_1 \circ R\_2$ |   $\checkmark$   |   $\times$   |   $\times$   |   $\times$   | $\checkmark$ |
