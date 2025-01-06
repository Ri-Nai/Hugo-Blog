---
title: "薛定谔方程"
slug: "12 16 《大学物理AII》复习笔记/近代物理/薛定谔方程及其应用/薛定谔方程"
date: "2024-12-31T16:45:50+08:00"
lastmod: "2024-12-31T16:45:50+08:00"
hidden: true
description:
draft: false
math:
license:
author: "Ri-Nai"
categories: ["学习笔记"]
tags: ["大学物理", "近代物理"]
---
### 一般形式的薛定谔方程
$$\hat{H}\varPsi=i\hbar\frac{\partial\varPsi}{\partial t}$$  
其中 $\hat{H}$ 是哈密顿算符，$\hat{H}=-\frac{\hbar^2}{2m}\nabla^2+U$ ， $U$ 是势能函数。    
对于一维情况，薛定谔方程的一般形式为  
$$-\frac{\hbar^2}{2m}\frac{\partial^2\varPsi}{\partial x^2}+U\varPsi=i\hbar\frac{\partial\varPsi}{\partial t}$$  
  
### 定态薛定谔方程  
对于定态，即 $\varPsi(x,t)=\psi(x)e^{-iEt/\hbar}$ ，概率密度 $|\varPsi|^2=\varPsi^*\varPsi = |\psi|^2$ 不随时间变化。    
代入薛定谔方程得到    
$$-\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2}+U\psi=E\psi$$    
即    
$$\hat{H}\psi=E\psi$$    
称为 $\hat{H}$ 的本征方程， $\psi$ 为本征函数， $E$ 为本征值。  

$E=\displaystyle{\frac{p^2}{2m}} + U$ ， $p$ 为动量。
即能量为动能和势能之和。  
  
### 一维无限深势阱  
一维无限深势阱的势能函数为  
$$U(x)=\begin{cases}0, & 0<x<a \newline +\infty, & \text{其他}\end{cases}$$    
波函数为    
$$\psi(x)=\begin{cases}\displaystyle{\sqrt{\frac{2}{a}}\sin\frac{n\pi x}{a}}, & 0<x<a \newline 0, & \text{其他}\end{cases}$$    
由定态薛定谔方程得到能量本征值    
$$-\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2}=E\psi$$  
$$E\_n=\frac{n^2\pi^2\hbar^2}{2ma^2}$$    
由    
$$E\_n=\frac{p\_n^2}{2m}$$  
得到动量本征值  
$$p\_n=\frac{n\pi\hbar}{a} = \frac{h}{2a}n$$  
故波长为  
$$\lambda\_n=\frac{h}{p\_n}=\frac{2a}{n}$$  
  
### 一维谐振子  
一维谐振子的势能函数为  
$$U(x)=\frac{1}{2}kx^2=\frac{1}{2}m\omega^2x^2$$  
求得能级公式为  
$$E\_n=\left(n+\frac{1}{2}\right)=\left(n+\frac{1}{2}\right)h\nu$$  
  
其中基态能量为  
$$E\_0=\frac{1}{2}h\nu$$  
称为**零点能**。  

谐振子的最低能量不等于零，即它永远不能静止不动。

### 势垒穿透
在势能有限的情况下,微观粒子可以穿过势垒到达另一侧，称“隧道效应”。
