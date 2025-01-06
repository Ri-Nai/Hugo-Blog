---
title: "恒定电流"
slug: "12 16 《大学物理AII》复习笔记/电磁学/恒定磁场/恒定电流"
date: "2024-12-18T23:45:17+08:00"
lastmod: "2024-12-18T23:45:17+08:00"
hidden: true
description:
draft: false
math:
license:
author: "Ri-Nai"
categories: ["学习笔记"]
tags: ["大学物理", "电磁学"]
---
### 电流
**电流**是由大量带电粒子定向运动形成的，这些形成电流的粒子可以是自由电子、离子、空穴等，被统称为 **载流子** 。

描述电流的物理量是电流强度，用符号$I$表示，它等同于单位时间内通过导体横截面的电荷量，即
$$I = \frac{dq}{dt}$$  
电流的单位是安培（A）。
$$1A = 1C/s$$  
安培是国际单位制的基本单位之一，而电荷量的单位库仑则是导出单位。

电流是 **标量** ，但是为了分析问题方便，习惯将正电荷流动的方向定义为电流的方向。

当通过导体任一截面的电流 $I$ 不随时间变化时，称为 **恒定电流** 。

### 电流密度
实际上大块导体内部的电流并不是均匀分布的，为了更细致地描述电流的分布情况，引入了 **电流密度** 的概念。

$$I = \frac{\delta Q}{\delta t} = neSv\_D$$  
$$J = \frac{I}{S} = nev\_D$$  
一般的，电流密度为 **矢量** ，方向与电流方向一致，大小为单位横截面积上的电流量。故  
$$\boldsymbol{J} = nq\boldsymbol{v}\_D$$  

$$I = \oint\_S \boldsymbol{J} \cdot d\boldsymbol{S} = -\frac{dq\_{\text{内}}}{dt}$$
这一关系式被称为 **电流的连续性方程** 。
当
$$\oint\_S \boldsymbol{J} \cdot d\boldsymbol{S} = 0$$
时，称为 **稳恒电流** 。

### 欧姆定律的微分形式

#### 欧姆定律
$$I = \frac{U}{R}$$

#### 电阻率和电导率
$\rho$ 称为 **电阻率** ，$\sigma = \frac{1}{\rho}$ 称为 **电导率**。  
粗细均匀的导体中，电阻率 $\rho$ 为常数，导体的长度为 $l$ ，横截面积为 $S$ ，则  

$$R = \rho \frac{l}{S}$$

#### 欧姆定律的微分形式
取一段长为 $dl$，横截面积为 $dS$ 的圆柱形体积元，流过截面 $dS$ 的电流为
$$dI = \frac{dU}{R}$$  
当体积元足够短时，可以忽略场强沿圆柱长度方向的变化，所以有 $dU = Edl$，又由 $dI = JdS$，$R = \rho \frac{dl}{dS}$，所以
$$JdS = \frac{1}{\rho} \frac{dS}{dl} Edl = \frac{E}{\rho} dS$$
因此
$$J = \sigma E$$
由于 $\boldsymbol{J}$ 和 $\boldsymbol{E}$ 的方向相同，可以写成矢量形式
$$\boldsymbol{J} = \sigma \boldsymbol{E}$$

### 电源和电动势
用受到的非静电力与电荷量的比值来定义非静电场场强，用 $E\_k$ 表示，即
$$E\_k = \frac{F}{q}$$

非静电力把单位正电荷经电源内部从负极移动到正极的功称为电源的电动势，用符号 $\mathcal{E}$ 表示，即
$$\mathcal{E} = \int\_{-}^{+} \boldsymbol{E} \cdot d\boldsymbol{l}$$

当非静电力存在于整个回路时，整个回路的总电动势为
$$\mathcal{E} = \oint \boldsymbol{E} \cdot d\boldsymbol{l}$$

电动势是标量，但为了便于判断在电流流通时，非静电力是做正功还是负功，常把电源内部电势升高的方向定义为电动势的方向。
