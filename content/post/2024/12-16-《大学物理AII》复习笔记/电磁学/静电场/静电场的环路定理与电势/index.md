---
title: "静电场的环路定理与电势"
slug: "12 16 《大学物理AII》复习笔记/电磁学/静电场/静电场的环路定理与电势"
date: "2024-12-17T01:34:40+08:00"
lastmod: "2024-12-17T01:34:40+08:00"
hidden: true
description:
draft: false
math:
license:
author: "Ri-Nai"
categories: ["学习笔记"]
tags: ["大学物理", "电磁学"]
---
### 静电场的环路定理
#### 引理
$$A\_{ab} = \int\_{a}^{b} d\boldsymbol{A} = \int\_{a}^{b} \boldsymbol{E} \cdot d\boldsymbol{l} = \int\_{a}^{b} E \cdot dl \cdot \cos \theta$$
#### 环路定理
$$\oint \boldsymbol{E} \cdot d\boldsymbol{l} = 0$$
表述为：在静电场电场强度的环流等于零。  

与 **{{< linking "电磁学/静电场/静电场的高斯定理#高斯定理|高斯定理" >}}** 一样，也是表述静电场性质的一个重要定理，可以用环路定理检验一个电场是否是静电场。

### 静电势能
静电力做的功：
$$A\_{ab} = \int\_a^b \boldsymbol{F} \cdot d\boldsymbol{l} = W\_a - W\_b = -\Delta W$$
对于试验电荷 $q$，在电场中移动的过程中，电场力做的功为
$$A\_{ab} = \int\_a^b \boldsymbol{F} \cdot d\boldsymbol{l} = q \int\_a^b \boldsymbol{E} \cdot d\boldsymbol{l} = q \int\_a^b E \cdot dl \cdot \cos \theta$$
将电荷移到电势零点电场力做的功称为电荷在电场中的势能，即
$$\Delta W = W\_a - W\_b = q \int\_a^b E \cdot dl \cdot \cos \theta = q \int\_a^b E \cdot dl = q \Delta U$$
电势能单位为焦耳，符号为 $\text{J}$。

#### 电势与电势差
$$\varphi = \frac{W}{q} = \int\_{a}^{\text{电势零点}} \boldsymbol{E} \cdot d\boldsymbol{l}$$
在理论计算中通常选取无穷远为电势零点，即
$$\varphi = \int\_{P}^{\infty} \boldsymbol{E} \cdot d\boldsymbol{l} \quad (\varphi\_{\infty} = 0)$$
电势差，也称电压，是指两点之间的电势差，即
$$U\_{ab} = \varphi\_a - \varphi\_b = \int\_{a}^{b} \boldsymbol{E} \cdot d\boldsymbol{l}$$
静电力做的功可以表示为
$$A\_{ab} = q U\_{ab}$$
#### 电势能的计算
##### 积分
$$\varphi = \int\_{P}^{\infty} \boldsymbol{E} \cdot d\boldsymbol{l} = -\int\_{\infty}^{P} \boldsymbol{E} \cdot d\boldsymbol{l}$$
##### 点电荷
$$\varphi = \frac{1}{4\pi\varepsilon\_0} \frac{q}{r}$$

##### 叠加法
$$\varphi = \sum\_{i=1}^n \varphi\_i = \sum\_{i=1}^n \frac{1}{4\pi\varepsilon\_0} \frac{q\_i}{r\_i}$$
$$\varphi = \int d\varphi$$

### 等势面
等势面上的法向量与电场强度的方向相同，即
$$\boldsymbol{E} \cdot d\boldsymbol{l} = 0$$
