---
title: "康普顿效应"
slug: "12 16 《大学物理AII》复习笔记/近代物理/微观粒子的波粒二象性/康普顿效应"
date: "2024-12-25T14:28:28+08:00"
lastmod: "2024-12-25T14:28:28+08:00"
hidden: true
description:
draft: false
math:
license:
author: "Ri-Nai"
categories: ["学习笔记"]
tags: ["大学物理", "近代物理"]
---
### 康普顿效应
1923年，美国物理学家 阿瑟·康普顿 在观察X射线被石墨等物质散射时，发现在散射线中除有与入射波长相同的射线外，还有波长**比入射波长更长的射线**，这种有波长改变的散射现象称为**康普顿效应**。

#### 康普顿散射公式
实验给出的波长偏移量 $\Delta\lambda$ 与散射角 $\varphi$ 之间的关系为
$$\Delta\lambda = \lambda\_c(1 - \cos\varphi)$$  
式中的 $\lambda\_c$ 称为**康普顿波长**，其表达式为  
$$\lambda\_c = \frac{h}{m\_ec} = 2.43\times10^{-12}\,\text{m}$$

#### 康普顿效应与经典理论的矛盾
经典波动理论无法解释上述波长改变了的康普顿效应。 
按照经典波动理论，在X射线的照射下，物质中的带电粒子将从入射光中吸收能量，做同频率的受迫振动，所辐射的电磁波的频率也应与入射光的频率**相同**，因而不会发生波长改变。

### 光量子解释
在光子射到散射体上并和某一原子中的外层电子发生碰撞过程中，电子会吸收一部分能量，脱离原子而反冲出去，称为**反冲电子**；所以散射光子的能量就要比入射光子的能量小，因而散射光的频率会变小，而波长会变长。

设碰撞前入射光子的频率为 $\nu\_0$ ，则其能量为 $h\nu\_0$ ，动量为 $p = \frac{h\nu\_0}{c}$ ，其中， $\boldsymbol{e}\_0$ 为入射光方向上的单位矢量； 
静止的自由电子能量为 $m\_ec^2$ ，动量为零。 

碰撞后，散射角为 $\varphi$ 的散射光子的能量为 $h\nu$ ，动量为 $p' = \frac{h\nu}{c} \boldsymbol{e}$ ，其中， $\boldsymbol{e}$ 为散射光方向上的单位矢量。
反冲速度为 $v$ 的电子质量为
$$m = \frac{m\_e}{\sqrt{1 - \frac{v^2}{c^2}}} \tag{1}$$  
能量为 $mc^2$ ，动量为 $mv$ 。

由动量守恒和能量守恒可得
$$h\nu\_0 + m\_ec^2 = h\nu + mc^2 \tag{2}$$
$$\frac{h\nu\_0}{c}\boldsymbol{e}\_0 = \frac{h\nu}{c}\boldsymbol{e} + m\boldsymbol{v} \tag{3}$$

其中下式可以写成两个分量方程
$$\frac{h\nu\_0}{c} = \frac{h\nu}{c}\cos\varphi + mv\cos\theta \tag{4}$$
$$\frac{h\nu}{c}\sin\varphi = mv\sin\theta \tag{5}$$
联立$(4)(5)$，消去 $\theta$ 可得
$$m^2v^2c^2 = h^2 \left(\nu\_0^2 + \nu^2 - 2\nu\_0\nu\cos\varphi\right) \tag{6}$$
又因为
$$m^2c^4 = h^2\left(\nu\_0^2+\nu^2-2\nu\_0\nu\right)+m\_e^2c^4+2hm\_ec^2\left(\nu\_0-\nu\right) \tag{7}$$

$(6)$ 式减去 $(7)$ 式，代入 $(1)$ 式可得
$$2h\nu\_0\nu(1-\cos\varphi) = 2hm\_ec^2(nu\_0-\nu)$$

于是有
$$\Delta\lambda = \lambda - \lambda\_0 = \frac{c}{\nu} - \frac{c}{\nu\_0} = \frac{h}{m\_ec}(1-\cos\varphi) = \lambda\_c(1-\cos\varphi)$$
与实验结果一致。

### 散射电子不能吸收光子
假设自由电子能够完全吸收光子，则由能量守恒定律和动量守恒定律可得
$$h\nu\_0 + m\_ec^2 = mc^2$$
$$\frac{h\nu\_0}{c}\boldsymbol{e}\_0 = mv\boldsymbol{e\_0}$$
上式与
$$m = \frac{m\_e}{\sqrt{1 - \frac{v^2}{c^2}}}$$
联立可得到
$$v = c$$
违背了相对论。
