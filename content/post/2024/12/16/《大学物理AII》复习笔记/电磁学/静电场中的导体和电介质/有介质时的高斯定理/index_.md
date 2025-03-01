---
title: "有介质时的高斯定理"
slug: "2024/12/16/《大学物理AII》复习笔记/电磁学/静电场中的导体和电介质/有介质时的高斯定理"
date: "2024-12-18T02:11:57+08:00"
lastmod: "2024-12-18T02:11:57+08:00"
hidden: true
description:
draft: false
math:
license:
author: "Ri-Nai"
categories: ["学习笔记"]
tags: ["大学物理", "电磁学"]
---
有电介质存在时的总场强为：
$$\boldsymbol{E}=\boldsymbol{E\_0}+\boldsymbol{E'}$$
其中，$\boldsymbol{E\_0}$ 是外电场，$\boldsymbol{E'}$ 是极化电场。

即电场 $\boldsymbol{E}$ 由束缚电荷的分布决定，而电介质最后的极化情况即点极化强度 $\boldsymbol{P}$ 和束缚电荷的分布又是由电场 $\boldsymbol{E}$ 决定的。

可见三者之间的关系是相互影响的，可以通过引入适当的物理量来简化问题。

### 电位移和有介质时的高斯定理
有电介质时，高斯定理依然成立，只不过此时 $\boldsymbol{E}$ 通量的计算需要同时考虑自由电荷和束缚电荷的贡献。
即：  
$$\oint\_S \boldsymbol{E} \cdot d\boldsymbol{S} = \frac{1}{\varepsilon\_0} \sum \left( q\_{0内} + q'\_{内} \right)$$  
根据{{< linking "电磁学/静电场中的导体和电介质/静电场中的电介质#极化强度与极化电荷的关系|极化强度与极化电荷的关系" >}}
可知：
$$\oint\_S (\varepsilon\_0 \boldsymbol{E} + \boldsymbol{P}) \cdot d\boldsymbol{S} = \sum q\_{0内}$$  
引入一个物理量 $\boldsymbol{D}$，称为电位移矢量，定义为： 
$$\boldsymbol{D} = \varepsilon\_0 \boldsymbol{E} + \boldsymbol{P}$$  
称为电位移矢量，其单位是 $\mathrm{C/m^2}$。  
则上式可改写成：  
$$\oint\_S \boldsymbol{D} \cdot d\boldsymbol{S} = \sum q\_{0内}$$  

此式证明：通过任意闭合曲面的电位移通量（或称为 $\boldsymbol{D}$ 通量）等于该闭合曲面内的自由电荷之和。
称为有介质时的高斯定理，或称为 **$\boldsymbol{D}$ 的高斯定理**。

### 介电常数
对于各向同性电介质，有：
$$\boldsymbol{D} = \varepsilon\_0 \varepsilon\_r \boldsymbol{E} = \varepsilon \boldsymbol{E}$$ 
式中比例系数 $\varepsilon = \varepsilon\_0 \varepsilon\_r$ 称为电介质的介电常数

### 应用
1. 根据自由电荷的分布求出电位移 $\boldsymbol{D}$ 的分布
2. 根据电位移 $\boldsymbol{D}$ 的分布求出电场强度 $\boldsymbol{E}$
3. 根据 $\boldsymbol{E}$ 求出 $\boldsymbol{P}$
4. 根据 $\boldsymbol{P}$ 求出束缚电荷面密度 $\sigma\_e'$
5. 根据 $\sigma\_e'$ 求出束缚电荷总量 $q'$

### 静电场的边界条件 

#### 电场强度切向分量的连续性
再两种电介质的分界面上，用 $E\_{1t}$ 和 $E\_{2t}$ 分别表示分界面电场强度切向分量大小，由环路定理知：

$$\oint\_L \boldsymbol{E} \cdot d\boldsymbol{l} = E\_{1t} \Delta l + E\_{2t} \Delta l = 0$$  
即：
$$E\_{1t} = E\_{2t}$$

可见，电场强度的切向分量在两种电介质的分界面上是连续的。

#### 电位移法向分量的连续性
在两种电介质的分界面上，用 $D\_{1n}$ 和 $D\_{2n}$ 分别表示分界面电位移法向分量大小，由高斯定理知：

$$\oint\_S \boldsymbol{D} \cdot d\boldsymbol{S} = D\_{1n} \Delta S + D\_{2n} \Delta S = 0$$
即：
$$D\_{1n} = D\_{2n}$$

可见，电位移的法向分量在两种电介质的分界面上是连续的。

以上推出的两个结论称为**静电场的边界条件**。

#### $\boldsymbol{D}$ 线的折射定律

{{< linkingImage "折射定律.png" >}}

$$\frac{\tan \theta\_1}{\tan \theta\_2} = \frac{\varepsilon\_{r1}}{\varepsilon\_{r2}}$$
