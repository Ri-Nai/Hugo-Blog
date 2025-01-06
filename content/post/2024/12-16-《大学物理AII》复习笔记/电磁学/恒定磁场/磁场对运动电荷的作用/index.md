---
title: "磁场对运动电荷的作用"
slug: "12 16 《大学物理AII》复习笔记/电磁学/恒定磁场/磁场对运动电荷的作用"
date: "2024-12-23T01:33:49+08:00"
lastmod: "2024-12-23T01:33:49+08:00"
hidden: true
description:
draft: false
math:
license:
author: "Ri-Nai"
categories: ["学习笔记"]
tags: ["大学物理", "电磁学"]
---
### 洛伦兹力
导线中的电流在磁场中受到的{{< linking "电磁学/恒定磁场/磁场对载流导线的作用#安培力|安培力" >}}为其中运动电荷所受**洛伦兹力**的宏观表现。

$$\boldsymbol{F} = q\boldsymbol{v} \times \boldsymbol{B}$$

洛伦兹力**垂直于**粒子的速度 $\boldsymbol{v}$ ，故它只改变速度方向，不改变速度大小，即不做功。

### 带电粒子在磁场中的运动
1. $\boldsymbol{v} \parallel \boldsymbol{B}$ 时，粒子做匀速直线运动。
2. $\boldsymbol{v} \perp \boldsymbol{B}$ 时，粒子做匀速圆周运动。
    - **回旋半径** 
        $$R = \frac{mv}{qB}$$
    - **回旋周期** 
        $$T = \frac{2\pi m}{qB}$$
    - **回旋频率**
        $$f = \frac{qB}{2\pi m}$$
3. $\boldsymbol{v}$ 与 $\boldsymbol{B}$ 的夹角为 $\theta$ 时，粒子做螺旋线运动。
    可将 $\boldsymbol{v}$ 分解为 $\boldsymbol{v\_{\parallel}}$ 和 $\boldsymbol{v\_{\perp}}$ 两部分
    - $\boldsymbol{v\_{\parallel}}$ 与 $\boldsymbol{B}$ 平行，不受磁场力作用，做匀速直线运动。
    - $\boldsymbol{v\_{\perp}}$ 与 $\boldsymbol{B}$ 垂直，受到磁场力作用，做匀速圆周运动。
    - **回旋半径**
        $$R = \frac{mv\_{\perp}}{qB} = \frac{mv\sin\theta}{qB}$$
    - **螺距**
        在一个周期内，粒子在磁场中沿轴线方向移动的距离。
        $$L = v\_{\parallel}T = v\_{\parallel} \frac{2\pi m}{qB} =  \frac{2\pi m v\cos\theta}{qB}$$
    - **磁聚焦**
        当 $\theta$ 很小的时候， $v\_{\parallel} \approx v$ ，一批带电粒子的速度分散在一定范围内，但是在磁场中运动后，速度分散减小，使得粒子聚焦在一点上。

### 应用实例

#### 速度选择器
速度选择器是利用带电粒子在电场和磁场中的受力情况，使得只有特定速度的粒子通过的装置。
在速度选择器中，电场和磁场的方向垂直，电场的方向与磁场的方向相同，使得带电粒子在电场中受到的电场力和磁场力相互抵消，从而只有特定速度的粒子通过。
$$qE = qvB$$
$$v = \frac{E}{B}$$

#### 汤姆孙实验
$$evB = \frac{mv^2}{r}$$
$$eE = evB$$
$$\frac{e}{m} = \frac{v}{rB} = \frac{E}{B^2r}$$

#### 质谱仪
$$qvB' = m\frac{v^2}{r}$$
$$m = \frac{qB'r}{v} = \frac{qBB'r}{E}$$

#### 回旋加速器
$$\frac{T}{2} = \frac{\pi m}{qB}$$
$$v = \frac{qBR}{m}$$

#### 霍尔效应
$$U\_H = E\_Hh = v\_DBh$$
$$I = nqv\_Dbh$$
$$U\_H = \frac{IB}{nqb}$$
其中 $U\_H$ 为霍尔电压， $K\_H = \frac{1}{nq}$ 为霍尔系数，只与材料有关。
