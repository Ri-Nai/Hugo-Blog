---
title: "氢原子光谱-玻尔的氢原子理论"
slug: "12 16 《大学物理AII》复习笔记/近代物理/微观粒子的波粒二象性/氢原子光谱-玻尔的氢原子理论"
date: "2024-12-25T15:39:45+08:00"
lastmod: "2024-12-25T15:39:45+08:00"
hidden: true
description:
draft: false
math:
license:
author: "Ri-Nai"
categories: ["学习笔记"]
tags: ["大学物理", "近代物理"]
---
### 氢原子光谱
氢原子的光谱呈现分立离散的线状光谱，称为氢光谱。

用波长的倒数 $\sigma = \frac{1}{\lambda}$ 来代替光谱线的波长

#### 谱系
$$\sigma = R\_{\infty} \left( \frac{1}{2^2} - \frac{1}{n^2} \right)$$

##### 巴尔末系
式中 $R\_{\infty} = 1.097 \times 10^7 \, \text{m}^{-1}$ 称为里德伯常量

##### 莱曼系
$$\sigma = R\_{\infty} \left( \frac{1}{1^1} - \frac{1}{n^2} \right)$$

##### 帕邢系
$$\sigma = R\_{\infty} \left( \frac{1}{3^2} - \frac{1}{n^2} \right)$$

##### 布拉开系
$$\sigma = R\_{\infty} \left( \frac{1}{4^2} - \frac{1}{n^2} \right)$$

##### 普丰德系
$$\sigma = R\_{\infty} \left( \frac{1}{5^2} - \frac{1}{n^2} \right)$$

##### 广义巴尔末系
$$\sigma = R\_{\infty} \left( \frac{1}{m^2} - \frac{1}{n^2} \right), \quad m = 1, 2, 3, \cdots, n - 1$$

### 玻尔的氢原子理论
玻尔突破经典物理学的束缚，结合了经典力学和量子力学的思想，提出了氢原子的理论模型，包含下面三个假设：
1. **定态假设**
    一个原子系统能够并且只能经常的处于一系列特定的能量状态，这些状态称为定态。
    虽然电子在绕核旋转，但是它不会辐射能量，也不会坠入核内。
2. **频率条件**
    电子在不同的能级之间跃迁时，辐射或者吸收的光子的频率满足
    $$h\nu = \left|E\_f - E\_i\right|$$
    其中 $E\_f$ 为最终能级， $E\_i$ 为初始能级。
3. **角动量量子假设**
    电子以速度 $v$ 在半径为 $r$ 的圆周上绕核运动，只有电子的角动量大小 $L$ 等于 $\hbar$ 的整数倍的那些轨道是稳定的，即
    $$L = m\_evr = n\hbar$$
    其中 $\hbar = \frac{h}{2\pi}$ 为约化普朗克常数， $n$ 为量子数， $n = 1, 2, 3, \cdots$

#### 氢原子的能量公式
从这些假设出发，可以推导出氢原子的能量公式
$$\frac{1}{4\pi\varepsilon\_0} \frac{e^2}{r^2} = m\_e \frac{v^2}{r}$$
$$r\_n = \frac{4\pi\varepsilon\_0 \hbar^2}{m\_ee^2}n^2$$
当 $n = 1$ 时，轨道半径最小为 $a\_0 = 0.529 \times 10^{-10} \, \text{m}$，称为玻尔半径。

电子在某一定态轨道上运动时，氢原子系统的总能量即定态能量为
$$E = E\_k + E\_p = \frac{1}{2} m\_e v^2 - \frac{1}{4\pi\varepsilon\_0} \frac{e^2}{r} = -\frac{e^2}{8\pi\varepsilon\_0 r}$$

将 $r\_n$ 代入上式可得
$$E\_n = -\frac{e^2}{2\left(4\pi\varepsilon\_0\right)r\_n} = -\frac{m\_ee^4}{2\left(4\pi\varepsilon\_0\right)^2\hbar^2} \cdot \frac{1}{n^2} = -\frac{13.6}{n^2} \, \text{eV}$$

其中 $n$ 只能取一系列正整数，称为**主量子数**。

$n = 1$ 时，称为**基态**， $n = 2, 3, 4, \cdots$ 时，称为**激发态**。
$E\_1 = -13.6 \, \text{eV}$，氢原子的电离能 $E\_i = E\_{\infty} - E\_1 = 13.6 \, \text{eV}$

#### 类氢离子的能级公式
类氢离子如 $He^+$，$Li^{2+}$ 等的能级公式为
$$E\_n = -\frac{m\_ee^4}{2\left(4\pi\varepsilon\_0\right)^2\hbar^2} \cdot \frac{Z}{n^2} = -\frac{13.6Z}{n^2} \, \text{eV}$$
其中 $Z$ 为核电荷数。

#### 光子的频率与波长
$$\nu = \frac{E\_n - E\_m}{h} = \left(\frac{1}{4\pi\varepsilon\_0}\right)^2 \frac{m\_ee^4}{4\pi\hbar^3} \left(\frac{1}{m^2} - \frac{1}{n^2}\right)$$

$$\sigma = \frac{1}{\lambda} = \frac{\nu}{c} = \left(\frac{1}{4\pi\varepsilon\_0}\right)^2\frac{m\_ee^4}{4\pi\hbar^3c} \left(\frac{1}{m^2} - \frac{1}{n^2}\right)$$
与广义巴尔末系的公式相同。可得里德堡常量
$$R\_{\infty} = \left(\frac{1}{4\pi\varepsilon\_0}\right)^2\frac{m\_ee^4}{4\pi\hbar^3c} = 1.097 \times 10^7 \, \text{m}^{-1}$$
