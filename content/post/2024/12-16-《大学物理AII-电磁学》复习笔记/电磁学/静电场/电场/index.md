---
title: "电场"
slug: "12 16 《大学物理AII-电磁学》复习笔记/电磁学/静电场/电场"
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
### 与电荷的关系
$$\text{电荷} \rightleftharpoons \text{电场} \rightleftharpoons \text{电荷}$$

### 电场对外的表现主要有
1. 电场力
2. 做功：具有电场能
3. 静电感应现象和极化现象

### 电场强度
#### 定义
$$\boldsymbol{E} = \frac{\boldsymbol{F}}{q}$$

#### 点电荷产生的电场强度

$$\boldsymbol{E} = \frac{1}{4\pi\varepsilon\_0}\frac{q}{r^2}\boldsymbol{e\_r}$$

#### 电偶极子
{{< linking "电磁学/静电场/电偶极子" >}}

#### 电荷连续分布的带电体产生的电场
$$d\boldsymbol{E} = \frac{1}{4\pi\varepsilon\_0}\frac{dq}{r^2}\boldsymbol{e\_r}$$
$$\boldsymbol{E} = \int d\boldsymbol{E} = \int \frac{1}{4\pi\varepsilon\_0}\frac{dq}{r^2}\boldsymbol{e\_r}$$
可以把矢量分别沿三个坐标轴分解，然后分别积分，最后合成矢量。
$$d\boldsymbol{E} = dE\_x \boldsymbol{i} + dE\_y \boldsymbol{j} + dE\_z \boldsymbol{k}$$
$$E\_x = \int dE\_x, \quad E\_y = \int dE\_y, \quad E\_z = \int dE\_z$$

##### 电荷密度
1. 电荷线密度
$$\lambda\_e = \frac{dq}{dl}$$
2. 电荷面密度
$$\sigma\_e = \frac{dq}{dS}$$
3. 电荷体密度
$$\rho\_e = \frac{dq}{dV}$$

#### 几个模型
1. 点电荷模型
2. 电偶极子
3. 无限长均匀带电直线
$r$ 为距离直线的距离，$\lambda_e$ 为线密度，则当 $r \gg l$ 时 (即 $r$ 远大于线长)
$$E = \frac{1}{4\pi\varepsilon\_0}\frac{2\lambda}{r}$$
等价于一个点电荷产生的电场
4. 均匀带电圆环
$r$ 为距离圆心的距离，$\lambda_e$ 为线密度，则
$$E = \frac{1}{4\pi\varepsilon\_0}\frac{Qr}{(r^2 + R^2)^{\frac{3}{2}}}$$
当 $r \gg R$ 时 (即 $r$ 远大于圆环半径)
$$E = \frac{1}{4\pi\varepsilon\_0}\frac{Q}{r^2}$$
5. 无限大均匀带电平面
$r$ 为距离平面的距离，$\sigma_e$ 为面密度，则当 $r \gg l$ 时 (即 $r$ 远大于平面长)
$$E = \frac{\sigma\_e}{2\varepsilon\_0}$$

6. 均匀带电圆盘
    - $r$ 接近于 $0$ 时，圆盘可看作一个无限大带电平面，即 $E = \frac{\sigma_e}{2\varepsilon_0}$
    - $r$ 远大于圆盘半径时，圆盘可看作一个点电荷，即 $E = \frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}$
7. 无限大带电厚壁
$r$ 为距离平面左端的距离，$\rho_e$ 为体密度，$d$ 为厚度。
可以看作连续的无限大带电平面，即
$$E = \int\_{0}^{d} \frac{\frac{d \rho\_e}{dx}}{2\varepsilon\_0} dx$$

