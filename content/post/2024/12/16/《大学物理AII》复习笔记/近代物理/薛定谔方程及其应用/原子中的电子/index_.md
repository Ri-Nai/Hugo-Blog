---
title: "原子中的电子"
slug: "2024/12/16/《大学物理AII》复习笔记/近代物理/薛定谔方程及其应用/原子中的电子"
date: "2024-12-31T17:09:14+08:00"
lastmod: "2024-12-31T17:09:14+08:00"
hidden: true
description:
draft: false
math:
license:
author: "Ri-Nai"
categories: ["学习笔记"]
tags: ["大学物理", "近代物理"]
---
### 氢原子
#### 四个量子数
氢原子的波函数由四个量子数确定：主量子数 $n$、角量子数 $l$、磁量子数 $m$ 和自旋量子数 $s$。
#### 主量子数-能量量子化
主量子数 $n$ 决定了{{< linking "近代物理/微观粒子的波粒二象性/氢原子光谱-玻尔的氢原子理论#氢原子的能量公式|能级" >}}的大小，取值范围为 $n = 1, 2, 3, \cdots$。
$$E\_n = -\frac{e^2}{2\left(4\pi\varepsilon\_0\right)r\_n} = -\frac{m\_ee^4}{2\left(4\pi\varepsilon\_0\right)^2\hbar^2} \cdot \frac{1}{n^2} = -\frac{13.6}{n^2} \, \text{eV}$$

#### 角量子数-角动量量子化
角量子数 $l$ 决定了轨道的形状，取值范围为 $l = 0, 1, 2, \cdots, n-1$。  
用 $L$ 表示角动量的大小，有  
$$L = \sqrt{l\left(l+1\right)}\hbar$$

#### 磁量子数-角动量空间取向量子化
磁量子数 $m\_l$ 决定了轨道的空间方向，取值范围为 $m\_l = 0, \pm 1, \pm 2, \cdots, \pm l$。
轨道角动量在 $z$ 方向的投影为
$$L\_z = m\_l\hbar$$

#### 自旋量子数与自旋磁量子数-自旋量子化
自旋量子数 $s$ 决定了电子的自旋方向，只能取 $s = \frac{1}{2}$
$$S = \sqrt{s\left(s+1\right)}\hbar = \frac{\sqrt{3}}{2}\hbar$$
自旋磁量子数 $m\_s$ 决定了自旋在 $z$ 方向的投影，取值范围为 $m\_s = \pm \displaystyle{\frac{1}{2}}$。
$$S\_z = m\_s\hbar$$

##### 总角动量
$$\boldsymbol{J} = \boldsymbol{L} + \boldsymbol{S}$$
$$J = \sqrt{j\left(j+1\right)}\hbar$$
其中 $j = \begin{cases}l+\frac{1}{2}, & \text{当} l = 0, 1, 2, \cdots, n-1 \newline l-\frac{1}{2}, & \text{当} l = 1, 2, \cdots, n-1\end{cases}$

#### 氢原子波函数
氢原子波函数的一般形式为：
$$\varPsi\_{n,l,m} = R\_{n,l}(r) Y\_{l,m\_l}(\theta, \phi)$$
其中 $R\_{n,l}(r)$ 为径向波函数，$Y\_{l,m\_l}(\theta, \phi)$ 为球谐函数。 

### 能量最低原理
原子处于正常状态时，其中电子都要占据最低能级。
判断能级高低的经验公式：
$$n + 0.7l$$
其值越小，能级越低。  

例如：  
- $4s$ ($l=0$) 能级：$n + 0.7l = 4 + 0.7 \times 0 = 4$  
- $3d$ ($l=2$) 能级：$n + 0.7l = 3 + 0.7 \times 2 = 4.4$  
可以解释电子先填充 $4s$ 而不是 $3d$。  

### 泡利不相容原理
一个原子中的电子总是倾向于占据能量最低的轨道，而且每个轨道最多只能容纳**两个电子**，且这两个电子的自旋量子数必须相反。

#### 壳层
$n$ 相同的可能电子态构成一个壳层。  
$n = 1, 2, 3, \cdots$ 表示为 $K, L, M, N, O, P, \cdots  $
$n$ 壳层最多容纳的电子数为 $2n^2$。

#### 支壳层
($n$ 相同), $l$ 相同的可能电子态构成一个支壳层。  
$l = 0, 1, 2, \cdots$ 表示为 $s, p, d, f, g, h, \cdots$  
$l$ 支壳层最多容纳的电子数为 $2(2l+1)$。
