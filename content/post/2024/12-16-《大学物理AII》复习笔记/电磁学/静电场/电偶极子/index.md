---
title: "电偶极子"
slug: "2024/12 16 《大学物理AII》复习笔记/电磁学/静电场/电偶极子"
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
### 定义
电偶极子是由两个相等大小、异种电荷构成的，相距很近的两个点电荷组成的系统。

设电偶极子的两个电荷分别为 $+q$ 和 $-q$，两电荷之间的距离为 $l$，则电偶极矩为
$$\boldsymbol{p} = q\boldsymbol{l}$$ 

电偶极矩是一个矢量，其方向由 $-q$ 指向 $+q$。

### 场强分布
设 $r$ 为点电荷到电偶极子中心的距离，$\theta$ 为 $r$ 与电偶极矩的夹角，则
1. 在电偶极子的延长线上
$$E\_+ = \frac{1}{4\pi\varepsilon\_0}\frac{q}{\left(r-\frac{l}{2}\right)^2}$$
$$E\_- = \frac{1}{4\pi\varepsilon\_0}\frac{q}{\left(r+\frac{l}{2}\right)^2}$$
$$E = E\_+ - E\_- = \frac{q}{4\pi\varepsilon\_0}\frac{2lr}{\left(r^2-\frac{l^2}{4}\right)^2}$$
即有
当 $r \gg l$ 时，有
$$E = \frac{1}{4\pi\varepsilon\_0}\frac{2p}{r^3}$$
2. 在电偶极子的轴线上
$$E\_+ = E\_- = \frac{1}{4\pi\varepsilon\_0}\frac{q}{r^2+\frac{l^2}{4}}$$
由对称性分析，两个点电荷在轴线上产生的场强大小相等，方向相反，仅留下了 $E$ 的 $-\boldsymbol{l}$ 方向的分量，即
$$E = -E\_+ \cos \theta - E\_- \cos \theta = -2 E\_+ \cos \theta = -2 \frac{1}{4\pi\varepsilon\_0}\frac{q}{r^2+\frac{l^2}{4}}\cos \theta$$
由几何关系可得
$$\cos \theta = \frac{l / 2}{\sqrt{r^2 + \left(l / 2\right)^2}} = \frac{1}{2} \frac{l}{\sqrt{r^2 + \frac{l^2}{4}}}$$
代入上式可得
$$E = -\frac{1}{4\pi\varepsilon\_0}\frac{ql}{\left(r^2 + \frac{l^2}{4}\right)^{\frac{3}{2}}}$$
当 $r \gg l$ 时，有
$$E = -\frac{1}{4\pi\varepsilon\_0}\frac{p}{r^3}$$
其中负号代表电场方向与电偶极矩方向相反。  
可以写成矢量式  
$$\boldsymbol{E} = -\frac{1}{4\pi\varepsilon\_0}\frac{\boldsymbol{p}}{r^3}$$
3. 在电偶极子的任意场点处
略，见教材 P23。
### 电偶极子在外电场中所受的力矩
处于匀强电场中的电偶极子，其两个电荷受到的力相等，方向相反，合力为零，但是它们所受的力矩不为零。电偶极子在外电场中所受的力矩为：
$$\boldsymbol{M} = \boldsymbol{p} \times \boldsymbol{E}$$
### 电偶极子在外电场中的电势能
$$W\_{e+} = q \varphi\_+, \quad W\_{e-} = q \varphi\_-$$
$$W\_e = W\_{e+} - W\_{e-} = q(\varphi\_+ - \varphi\_-)$$
$$\varphi\_+ - \varphi\_- = \int\_{+}^{-} \boldsymbol{E} \cdot d\boldsymbol{l}$$
由于$\boldsymbol{E}$是匀强电场
$$\int\_{+}^{-} d \boldsymbol{l} = -\boldsymbol{l}$$
$$W\_e=q\boldsymbol{E}\int\_{+}^{-}d\boldsymbol{l}=-\boldsymbol{p}\cdot\boldsymbol{E} = -\boldsymbol{p}\cdot\boldsymbol{E} = -pE\cos\theta$$
