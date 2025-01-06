---
title: "动生电动势和感生电动势"
slug: "12 16 《大学物理AII》复习笔记/电磁学/电磁感应和电磁场/动生电动势和感生电动势"
date: "2024-12-23T10:34:50+08:00"
lastmod: "2024-12-23T10:34:50+08:00"
hidden: true
description:
draft: false
math:
license:
author: "Ri-Nai"
categories: ["学习笔记"]
tags: ["大学物理", "电磁学"]
---
### 动生电动势
#### 定义
在电磁感应中，单纯由导体在磁场中运动产生的电动势称为 **动生电动势**。

#### 计算方法
在导体棒 $ab$ 中产生的动生电动势应等于将单位正电荷从从导体棒的负极 $b$ 移动到正极 $a$ 时所做的功
$$\boldsymbol{E}\_k = \frac{\boldsymbol{F}}{q} = \boldsymbol{v} \times \boldsymbol{B}$$  
$$d\mathcal{E} = \boldsymbol{E}\_k \cdot d\boldsymbol{l} = \boldsymbol{v} \times \boldsymbol{B} \cdot d\boldsymbol{l}$$  
$$\mathcal{E} = \int \boldsymbol{v} \times \boldsymbol{B} \cdot d\boldsymbol{l} = Blv\sin\theta$$

- 若计算出的电动势为正，则电流方向与选取的方向一致；
- 若计算出的电动势为负，则电流方向与选取的方向相反。

#### 能量起源
产生动生电动势的非静电起源是{{< linking "电磁学/恒定磁场/磁场对运动电荷的作用#洛伦兹力|洛伦兹力" >}}
而洛伦兹力是不做功的，但感应电动势可以输出电功，是否矛盾？
洛伦兹力的功率是
$$\begin{aligned}P\_L = \boldsymbol{F} \cdot \boldsymbol{v} &= \left(\boldsymbol{F}\_L + \boldsymbol{F}\_L' \right) \cdot \left(\boldsymbol{v} + \boldsymbol{v}' \right) \newline  &= e\boldsymbol{v}B\boldsymbol{v}' - e\boldsymbol{v}'B\boldsymbol{v} = 0\end{aligned}$$
洛伦兹力的功率为零

所有电子宏观的运动导致了{{< linking "电磁学/恒定磁场/磁场对载流导线的作用#安培力|安培力" >}}的做功  
由于安培力会阻碍导体棒的运动，要以恒定速度 $v$ 将导体棒移动，需要外力做功

$$P\_{ext} = \boldsymbol{F}\_{ext} \cdot \boldsymbol{v} = \boldsymbol{B} I \times \boldsymbol{L} \cdot \boldsymbol{v} = \mathcal{E} I$$

电动势的功率等于外力做功的功率，电能来源是外力克服安培力做功

### 感生电动势
#### 定义
导体回路静止不动，导体回路中的磁通量随时间变化而产生的电动势称为 **感生电动势**。

#### 计算方法
$$\mathcal{E} = -\frac{d\varPhi}{dt} = \int\_S \frac{\partial \boldsymbol{B}}{\partial t} \cdot d\boldsymbol{S}$$

#### 能量起源
麦克斯韦猜想，变化的磁场会产生电场，感生电动势的能量来源是磁场的变化

$$\mathcal{E} = \oint\_L \boldsymbol{E}\_k \cdot d\boldsymbol{l} = -\frac{d\varPhi}{dt}$$

### 法拉第电磁感应定律的另一种表述
$$\mathcal{E} = \oint\_L \left(\boldsymbol{v} \times \boldsymbol{B} + \boldsymbol{E}\_k \right) \cdot d\boldsymbol{l} = -\frac{d\varPhi}{dt}$$

### 感生电场
$$\oint\_L \boldsymbol{E}\_k \cdot d\boldsymbol{l} = -\int\_S \frac{\partial \boldsymbol{B}}{\partial t} \cdot d\boldsymbol{S}$$
可以看出，感生电场的环流可以不为零。
可以证明，感生电场线是无头无尾的闭合曲线。
因此有
$$\oint\_S \boldsymbol{E}\_k \cdot d\boldsymbol{S} = 0$$
此式称为**感生电场的高斯定理**。

#### 总电场
|      | 静电场 $E\_{\text{静}}$ | 感生电场 $E\_k$ |
| :--- | ----------------- | --------- |
| 场源   | 静止的电荷              | 变化的 磁场     |
| 电场线  | 起始于正电荷，终止于负电荷      | 无头无尾的变化曲线  |
| 环路定理 |  $$\oint\_L \boldsymbol{E}\_{\text{静}} \cdot d\boldsymbol{l} = 0$$ | $$\oint\_L \boldsymbol{E}\_k \cdot d\boldsymbol{l} = -\int\_S \frac{\partial \boldsymbol{B}}{\partial t} \cdot d\boldsymbol{S}$$ |
| 高斯定理 | $$\oint\_S \boldsymbol{E}\_{\text{静}} \cdot d\boldsymbol{S} = \frac{Q\_{\text{内}}}{\varepsilon\_0}$$ | $$\oint\_S \boldsymbol{E}\_k \cdot d\boldsymbol{S} = 0$$ |
| 电场性质 | 保守场，无旋 | 非保守场，有旋 |

可以根据上面的性质推出总电场的环路定理和高斯定理。  
即
$$\oint\_S \boldsymbol{E} \cdot d\boldsymbol{S} = \frac{Q\_{\text{内}}}{\varepsilon\_0}$$
$$\oint\_L \boldsymbol{E} \cdot d\boldsymbol{l} = -\frac{d\varPhi}{dt}$$

以上两式就是麦克斯韦方程组中关于电场的两个基本方程。

#### 感生电场的方向
感生电场的方向就是**感生电动势**和**感生电流**的方向。  
负号代表的含义就是**反抗**磁场的变化。  
满足左手螺旋定则。

### 涡电流及电磁阻尼
当大块金属处在变化的磁场中或在磁场中运动时，在其内部会出现涡旋形状的感生电流，称为**涡电流**。

#### 涡电流的热效应
涡流会产生大量的热，广泛用于电磁炉。

为了避免涡电流的热效应，常常采取多个硅钢片叠加的方法，使涡流被限制在单个绝缘的硅钢片中，从而减小涡电流的热效应。

#### 涡电流的机械效应
常用于电磁阻尼器，如电磁制动器。

也可以用于电磁驱动，当磁场在运动的时候，导体会跟随磁场运动，交流感应电动机就是利用这个原理。

#### 涡电流的电磁效应
金属探测器就是利用涡电流的电磁效应来探测金属的。  
涡流也会产生磁场，这个磁场会反过来影响外部磁场，从而影响感应电动势，达到探测金属的目的。

