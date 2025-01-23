---
title: "磁场中的磁介质"
slug: "2024/12 16 《大学物理AII》复习笔记/电磁学/恒定磁场/磁场中的磁介质"
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
### 磁介质对磁场的影响
类比{{< linking "电磁学/静电场中的导体和电介质/静电场中的电介质#电极化强度|电介质对电场的影响" >}}，有介质时的磁场可以被表示为  
$$\boldsymbol{B} = \boldsymbol{B\_0} + \boldsymbol{B}'$$

其中，$\boldsymbol{B}$ 是介质中的磁感应强度，$\boldsymbol{B\_0}$ 原磁场，$\boldsymbol{B}'$ 是介质产生的磁场。

根据实验表明，磁介质内的磁感应强度 $\boldsymbol{B}$ 为真空时的 $\mu\_r$ 倍，即
$$\boldsymbol{B} = \mu\_r \boldsymbol{B\_0}$$
式中，$\mu\_r$ 是磁介质的相对磁导率，为无量纲量。

### 磁介质的种类
#### 顺磁质
$$\mu\_r > 1$$

#### 抗磁质
$$\mu\_r < 1$$

#### 铁磁质
顺磁质和抗磁质的混合体的 $\mu\_r$ 接近于1，而铁磁质的 $\mu\_r$ 远大于1。  
$\boldsymbol{B}$ 和 $\boldsymbol{B}'$ 方向相同，内部磁场被大大增强。

### 磁介质的磁化
磁介质内由大量杂乱的 **分子磁矩** 组成，可以用等效的圆电流即 **{{< linking "电磁学/恒定磁场/磁场和磁感应强度#安培分子电流假说|分子电流" >}}** 来描述
有外磁场时，磁介质的状态就会发生变化，这种现象称为 **磁化** 。

- 顺磁质在外磁场的作用下，分子磁矩的方向与外磁场方向一致，磁介质内部的磁场增强。  
- 抗磁质在外磁场的作用下，在原有的磁矩方向上产生一个与外磁场方向相反的磁矩，磁介质内部的磁场减弱。  

这些方向相同的附加磁矩的矢量和就是一个分子在外磁场中产生的 **感生磁矩**。

### 磁化强度
$$\boldsymbol{M} = \frac{\sum \boldsymbol{m}}{V}$$

### 磁化电流
$$I' = \oint\_L \boldsymbol{M} \cdot d\boldsymbol{l}$$

### 有磁介质时的安培环路定理
类似于{{< linking "电磁学/静电场中的导体和电介质/有介质时的高斯定理#|有介质时的高斯定理" >}}，通过引入适当的物理量可以简化问题。

$$\oint\_L \boldsymbol{B} \cdot d\boldsymbol{l} = \mu\_0 (\sum I\_{\text{0内}} + I'\_{\text{内}})$$  
移项得到  
$$\oint\_L \left(\frac{\boldsymbol{B}}{\mu\_0} - \boldsymbol{M}\right) \cdot d\boldsymbol{l} = \sum I\_{\text{0内}}$$

引入**磁场强度** $\boldsymbol{H}$，定义为
$$\boldsymbol{H} = \frac{\boldsymbol{B}}{\mu\_0} - \boldsymbol{M}$$

故安培环路定理可以简化为  
$$\oint\_L \boldsymbol{H} \cdot d\boldsymbol{l} = \sum I\_{\text{0内}}$$

### 磁化强度与磁场强度的关系
$$\boldsymbol{M} = \chi\_m \boldsymbol{H}$$  
式中，$\chi\_m$ 为磁化率，是无量纲量。

代入 $$\boldsymbol{H} = \frac{\boldsymbol{B}}{\mu\_0} - \boldsymbol{M}$$
得到
$$\boldsymbol{B} = \mu\_0 (\boldsymbol{H} + \boldsymbol{M}) = \mu\_0 (1 + \chi\_m) \boldsymbol{H} = \mu\_0 \mu\_r \boldsymbol{H} = \mu \boldsymbol{H}$$  
即
$$\boldsymbol{B} = \mu \boldsymbol{H}$$  

$\mu\_r = 1 + \chi\_m$ 为磁介质的相对磁导率，$\mu = \mu\_0 \mu\_r$ 为磁介质的磁导率。

