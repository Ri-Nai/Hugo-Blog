---
title: "洛伦兹变换"
slug: "2024/12 16 《大学物理AII》复习笔记/近代物理/狭义相对论力学基础/洛伦兹变换"
date: "2024-12-24T19:29:30+08:00"
lastmod: "2024-12-24T19:29:30+08:00"
hidden: true
description:
draft: false
math:
license:
author: "Ri-Nai"
categories: ["学习笔记"]
tags: ["大学物理", "近代物理"]
---
### 洛伦兹变换
一个事件： $S$ 系中的坐标为 $(x, y, z, t)$， $S'$ 系中的坐标为 $(x', y', z', t')$，两个系之间的相对速度为 $u$
满足以下关系：
1. $x$, $y$, $z$ 轴与 $x'$, $y'$, $z'$ 轴平行
2. $S'$ 系相对 $S$ 系沿 $x$ 轴正方向以速度 $u$ 运动
3. 当 $t = t' = 0$ 时，两个系的坐标原点重合

$$\begin{aligned}
\left.
\begin{array}{ll}
x' &=& \frac{x-ut}{\sqrt{1-\frac{u^2}{c^2}}}  \newline 
y' &=& y  \newline 
z' &=& z  \newline 
t' &=& \frac{t-\frac{u}{c^2}x}{\sqrt{1-\frac{u^2}{c^2}}}
\end{array}
\right \rbrace
\quad \leftrightarrows \quad
\left\lbrace
\begin{array}{ll}
x &=& \frac{x' + ut'}{\sqrt{1-\frac{u^2}{c^2}}}  \newline 
y &=& y'  \newline 
z &=& z'  \newline 
t &=& \frac{t' + \frac{u}{c^2}x'}{\sqrt{1-\frac{u^2}{c^2}}}
\end{array}
\right.
\end{aligned}$$

$$\gamma = \frac{1}{\sqrt{1-\frac{u^2}{c^2}}}$$  
称为**洛伦兹因子**。
有
$$x' = \gamma(x-ut)$$
根据爱因斯坦相对性原理，两个系之间除了相对速度相反之外，没有其他差别，因此有
$$x = \gamma(x'+ut')$$

$$x^2 + y^2 + z^2 - c^2t^2 = x'^2 + y'^2 + z'^2 - c^2t'^2 = 0$$

### 同时性的相对性
在 $S$ 系中，两个事件 $A$ 和 $B$ 在 $x$ 轴上的坐标分别为 $x\_A$ 和 $x\_B$，在 $S'$ 系中，两个事件的坐标分别为 $x'\_A$ 和 $x'\_B$，则有
$$x\_A = \gamma(x'\_A + ut'\_A)$$
$$x\_B = \gamma(x'\_B + ut'\_B)$$
两个事件同时发生的条件是 $t\_A = t\_B$，即 $t'\_A = t'\_B$，则有
$$x\_A = \gamma(x'\_A + ut'\_A) = \gamma(x'\_B + ut'\_B) = x\_B$$
即在 $S$ 系中同时发生的两个事件，在 $S'$ 系中不一定同时发生，这就是**同时性的相对性**。

### 因果律
在 $S$ 系中，事件 $A$ 发生在事件 $B$ 之前，即 $t\_A < t\_B$，则有
$$t'\_A = \frac{t\_A - \frac{u}{c^2}x\_A}{\sqrt{1-\frac{u^2}{c^2}}} < \frac{t\_B - \frac{u}{c^2}x\_B}{\sqrt{1-\frac{u^2}{c^2}}} = t'\_B$$
即在 $S'$ 系中，事件 $A$ 同样发生在事件 $B$ 之前，这就是**因果律**。


