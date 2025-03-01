---
title: "命题逻辑"
slug: "2025/01/06/《离散数学》复习笔记/数理逻辑/命题逻辑"
date: "2025-01-06T12:00:18+08:00"
lastmod: "2025-01-06T12:00:18+08:00"
hidden: true
description:
draft: false
math:
license:
author: "Ri-Nai"
categories: ["学习笔记"]
tags: ["离散数学", "计算机科学"]
---
## 命题逻辑的基本概念
### 命题与真值
- 命题：判断结果唯一的陈述句
- 命题的真值：判断的结果
- 真值的取值：真与假
- 真命题与假命题
注意：
感叹句、祈使句、疑问句都不是命题
陈述句中的悖论，判断结果不唯一确定的不是命题

### 命题分类
简单命题（也称原子命题,不能被分解成更简单的命题）
复合命题（由简单命题通过联结词联结而成的命题）

### 简单命题符号化
- 用小写英文字母 $p,q,r \cdots$ 或 $p\_1,p\_2,p\_3 \cdots$ 表示
- 用 $1$ 表示真（$T$），用 $0$ 表示假（$F$）

### 连接词
- 否定：$\neg p$
- 合取：$p \land q$
- 析取：$p \lor q$
- 蕴含：$p \to q$
- 等价：$p \leftrightarrow q$


### 命题变项
- 命题常项：一个命题标识符表示确定的命题
- 命题变项：一个命题标识符表示不确定的命题

命题常项和变项均由字母表示

### 合式公式
1. 单个命题变项和命题常项是合式公式, 称作原子命题公式
2. 若A是合式公式，则 ($\neg A$)也是
3. 若A, B是合式公式，则($A \land B$), ($A \lor B$), ($A \to B$), ($A \leftrightarrow B$)也是
4. 只有有限次地应用 1. — 3. 形成的符号串才是合式公式

#### 合式公式的层次
1. 单个命题变项为 $0$ 层
2. 称 A 是 $n+1(n \geq 0)$ 层公式是指下面情况之一：
   (a) $A=\neg B$, $B$ 是 $n$ 层公式；
   (b) $A=B \land C$, 其中 $B,C$ 分别为 $i$ 层和 $j$ 层公式，
        且 $n=\max(i,j)$；
   (c) $A=B \lor C$, 其中 $B,C$ 的层次及 $n$ 同 (b)；
   (d) $A=B \to C$, 其中 $B,C$ 的层次及 $n$ 同 (b)；
   (e) $A=B \leftrightarrow C$, 其中 $B,C$ 的层次及 $n$ 同 (b).     
3.  若公式 $A$ 的层次为 $k$, 则称 $A$ 为 $k$ 层公式.

### 公式赋值
设 $p\_1,p\_2,\cdots,p\_n$ 是在 $A$ 中出现的所有命题变项，$A$ 是一个合式公式，$a\_1,a\_2,\cdots,a\_n$ 是 $p\_1,p\_2,\cdots,p\_n$ 的真值，则称 $a\_1,a\_2,\cdots,a\_n$ 是 $A$ 的一个赋值。
- 若使 $A$ 的值为真，则称 $a\_1,a\_2,\cdots,a\_n$ 是 $A$ 的一个真值赋值
- 若使 $A$ 的值为假，则称 $a\_1,a\_2,\cdots,a\_n$ 是 $A$ 的一个假值赋值

### 公式的类型
- **重言式** 或 **永真式**：对任何赋值，公式的值都为真
- **矛盾式** 或 **永假式**：对任何赋值，公式的值都为假

若一个公式不是矛盾式，则称它是可满足式。

### 真值表
将命题公式 $A$ 在所有赋值下取值的情况列成表, 称作 $A$ 的真值表.


## 等值式
若 $A \leftrightarrow B$ 是重言式，则称 $A$ 与 $B$ 等值，记作 $A \Leftrightarrow B$，并称 $A$ 与 $B$ 是等值式。

- **真值表法**
- **等值演算法**


### 基本等值式
$$\begin{aligned}
双重否定律 & & \neg(\neg A) & \Leftrightarrow A \newline \newline 
幂等律 & & A \land A & \Leftrightarrow A \newline 
 & & A \lor A & \Leftrightarrow A \newline \newline 
交换律 & & A \land B & \Leftrightarrow B \land A \newline 
 & & A \lor B & \Leftrightarrow B \lor A \newline \newline 
结合律 & & A \land (B \land C) & \Leftrightarrow (A \land B) \land C \newline 
 & & A \lor (B \lor C) & \Leftrightarrow (A \lor B) \lor C \newline \newline 
分配律 & & A \land (B \lor C) & \Leftrightarrow (A \land B) \lor (A \land C) \newline 
 & & A \lor (B \land C) & \Leftrightarrow (A \lor B) \land (A \lor C) \newline \newline 
吸收律 & & A \land (A \lor B) & \Leftrightarrow A \newline 
 & & A \lor (A \land B) & \Leftrightarrow A \newline \newline 
零律 & & A \land 0 & \Leftrightarrow 0 \newline 
 & & A \lor 1 & \Leftrightarrow 1 \newline \newline 
同一律 & & A \land 1 & \Leftrightarrow A \newline 
 & & A \lor 0 & \Leftrightarrow A \newline \newline 
排中律 & & A \lor \neg A & \Leftrightarrow 1 \newline 
 & & A \land \neg A & \Leftrightarrow 0 \newline \newline 
矛盾律 & & A \land \neg A & \Leftrightarrow 0 \newline 
 & & A \lor \neg A & \Leftrightarrow 1 \newline \newline 
蕴含等值式 & & A \to B & \Leftrightarrow \neg A \lor B \newline 
 & & \neg(A \to B) & \Leftrightarrow A \land \neg B \newline \newline 
德摩根律 & & \neg(A \land B) & \Leftrightarrow \neg A \lor \neg B \newline 
 & & \neg(A \lor B) & \Leftrightarrow \neg A \land \neg B \newline \newline 
等价等值式 & & A \leftrightarrow B & \Leftrightarrow (A \to B) \land (B \to A) \newline 
假言易位 & & A \to B & \Leftrightarrow \neg B \to \neg A \newline 
 & & \neg(A \to B) & \Leftrightarrow A \land \neg B \newline \newline 
等价否定 & & A \leftrightarrow B & \Leftrightarrow \neg A \leftrightarrow \neg B \newline 
归谬论 & & A \to B & \Leftrightarrow \neg B \to \neg A \newline 
\end{aligned}$$

### 析取范式与合取范式
#### 简单析取式与简单合取式
- 文字：命题变项或其否定
- **简单析取式**：有限个文字的析取
  $$p, \neg q, p \lor q, \neg p \lor q, \neg p \lor \neg q$$
- **简单合取式**：有限个文字的合取
  $$p, \neg q, p \land q, \neg p \land q, \neg p \land \neg q$$

单个文字既是析取式又是合取式

一个简单析取式是重言式**当且仅当**它包含一个命题变项和它的否定
一个简单合取式是矛盾式**当且仅当**它包含一个命题变项和它的否定
#### 析取范式与合取范式

**析取范式**：$$A\_1 \lor A\_2 \lor \cdots \lor A\_n$$
其中 $A\_i$ 是简单合取式

**合取范式**：$$A\_1 \land A\_2 \land \cdots \land A\_m$$
其中 $A\_i$ 是简单析取式

一个析取范式是矛盾式**当且仅当**它的每一个合取式都是矛盾式
一个合取范式是重言式**当且仅当**它的每一个析取式都是重言式

任意一个命题公式都可以化为析取范式和合取范式

#### 主析取范式与主合取范式
##### 主析取范式与极小项
**主析取范式**：$$m\_0 \lor m\_1 \lor \cdots \lor m\_{2^n-1}$$
其中 $m\_i$ 被称作**极小项**，是 $n$ 个文字的析取
$m\_i$ 的第 $j$ 个文字是 $p\_j$ 或 $\neg p\_j$
若 $i$ 的二进制表示为 $b\_1b\_2\cdots b\_n$，则 $m\_i$ 为
$$p\_1^{b\_1} \land p\_2^{b\_2} \land \cdots \land p\_n^{b\_n}$$
$p\_j^{b\_j}$ 表示 $p\_j$ 若 $b\_j=1$ 则取 $p\_j$，否则取 $\neg p\_j$

##### 主合取范式与极大项
**主合取范式**：$$M\_0 \land M\_1 \land \cdots \land M\_{2^n-1}$$
其中 $M\_i$ 被称作**极大项**，是 $n$ 个文字的合取
$M\_i$ 的第 $j$ 个文字是 $p\_j$ 或 $\neg p\_j$
若 $i$ 的二进制表示为 $b\_1b\_2\cdots b\_n$，则 $M\_i$ 为
$$p\_1^{b\_1} \lor p\_2^{b\_2} \lor \cdots \lor p\_n^{b\_n}$$
$p\_j^{b\_j}$ 表示 $p\_j$ 若 $b\_j=1$ 则取 $p\_j$，否则取 $\neg p\_j$

任意一个命题公式都可以化为**唯一的**主析取范式和主合取范式

### 连接词完备集
- 不可兼析取：$\overline{\lor}$ 即异或
    - $A \overline{\lor} B \Leftrightarrow (A \lor B) \land \neg (A \land B) \Leftrightarrow (A \land \neg B) \lor (\neg A \land B)$
- 或非：$\downarrow$
    - $A \downarrow B \Leftrightarrow \neg (A \lor B) \Leftrightarrow \neg A \land \neg B$
- 与非：$\uparrow$
    - $A \uparrow B \Leftrightarrow \neg (A \land B) \Leftrightarrow \neg A \lor \neg B$

若任意 $n$ 元真值函数都可以由仅含 $S$ 中的连接词构成的公式表示，则称 $S$ 为**连接词完备集**

#### 部分完备集举例
$$S = \lbrace \neg, \land, \lor \rbrace$$
证明：任意一个 $n$ 元函数都可与唯一的一个主析取范式和主合取范式对应

$$S = \lbrace \neg, \land \rbrace$$
证明：$A \lor B \Leftrightarrow \neg (\neg A \land \neg B)$

$$S = \lbrace \neg, \lor \rbrace$$
证明：$A \land B \Leftrightarrow \neg (\neg A \lor \neg B)$

$$S = \lbrace \neg, \to \rbrace$$
证明：$A \land B \Leftrightarrow \neg A \to B$

$$S = \lbrace \lor, \land, \to, \leftrightarrow \rbrace$$ 不是完备集，恒取 $0$ 的函数无法表示

$$S = \lbrace \uparrow \rbrace$$
证明：$$\begin{aligned}
 \neg A &\Leftrightarrow A \uparrow A \newline 
 A \land B &\Leftrightarrow \neg (A \uparrow B) \newline 
 A \lor B &\Leftrightarrow \neg (\neg A \uparrow \neg B) \newline 
\end{aligned}$$

#### 最小连接词完备集
若 $S$ 是连接词完备集，从 $S$ 中去掉任意一个连接词后 $S$ 不再是完备集，则称 $S$ 为**最小连接词完备集**

### 消解算法与可满足性问题
$$C\_1 \land C\_2 \approx Res(C\_1, C\_2) = C\_1' \lor C\_2'$$
1. 若 $C\_1 \land C\_2 \leftrightarrow (l \lor C\_1') \land (\neg l \lor C\_2')$ 是可满足的，则称 $C\_1' \lor C\_2'$ 也是可满足的
2. 若 $C\_1' \lor C\_2'$ 是可满足的，则称 $C\_1 \land C\_2$ 也是可满足的
故可将 $C\_1 \land C\_2$ 化为 $C\_1' \lor C\_2'$，称作**消解**

## 推理
当 $A\_1 \land A\_2 \land \cdots \land A\_n \to B$ 是重言式时，称 $B$ 由 $A\_1, A\_2, \cdots, A\_n$ 推出，记作 $\lbrace  A\_1, A\_2, \cdots, A\_n  \rbrace \vdash B$
$A\_1, A\_2, \cdots, A\_n$ 称作**前提**，$B$ 称作**结论**
称前提推出结论是有效的或正确的，并称 $B$ 是有效结论。

### 推理的形式结构
1. $\lbrace A\_1, A\_2, \cdots, A\_n \rbrace \vdash B$
    - 若推理正确，记为 $\lbrace A\_1, A\_2, \cdots, A\_n \rbrace \vDash B$
    - 若推理不正确，记为 $\lbrace A\_1, A\_2, \cdots, A\_n \rbrace \nvDash B$
2. $A\_1 \land A\_2 \land \cdots \land A\_n \to B$
    - 若推理正确，记为 $A\_1 \land A\_2 \land \cdots \Rightarrow B$
3. 前提：$A\_1, A\_2, \cdots, A\_n$，结论：$B$

### 推理定律
$$\begin{aligned}
附加律 & & A &\Rightarrow A \land B \newline 
化简律 & & A \land B &\Rightarrow A \newline 
假言推理 & & A \land (A \to B) &\Rightarrow B \newline 
拒取式 & & \neg A \land \neg B &\Rightarrow \neg (A \land B) \newline 
析取三段论 & & A \lor B, \neg A &\Rightarrow B \newline 
假言三段论 & & A \to B, B \to C &\Rightarrow A \to C \newline 
等价三段论 & & A \leftrightarrow B, B \leftrightarrow C &\Rightarrow A \leftrightarrow C \newline 
构造性二难 & & A \to B, C \to D, A \lor C &\Rightarrow B \lor D \newline 
 & & A \to B, \neg A \to B &\Rightarrow B \newline 
破坏性二难 & & A \to B, C \to D, \neg B \lor \neg D &\Rightarrow \neg A \lor \neg C \newline 
 & & A \to B, \neg B \to A &\Rightarrow A \leftrightarrow B \newline 
\end{aligned}$$

### {{< linking "数理逻辑/形式系统" >}}

### 自然推理系统

定义3.3 自然推理系统 $P$ 定义如下:

1. 字母表
    1. 命题变项符号：$p, q, r, \ldots, p\_i, q\_i, r\_i, \ldots$
    2. 联结词符号：$\neg, \land, \lor, \to, \leftrightarrow$
    3. 括号与逗号：$(, ), ,$
2. 合式公式（同定义1.6）
3. 推理规则
    1. 前提引入规则
    2. 结论引入规则
    3. 置换规则


### 构造证明
设前提 $A\_1, A\_2, \ldots, A\_k$，结论 $B$ 及公式序列 $C\_1, C\_2, \ldots, C\_l$，
如果每一个 $C\_i \ (1 \leq i \leq l)$ 是某个 $A\_j \ (1 \leq j \leq k)$，
或者可由序列中前面的公式应用推理规则得到，
并且 $C\_l = B$，
则称这个公式序列是由 $A\_1, A\_2, \ldots, A\_k$ 推出 $B$ 的证明。

#### 附加前提证明法
附加前提证明法适用于结论为蕴涵式

- 欲证
    - 前提：$A\_1, A\_2, \ldots, A\_k$
    - 结论：$C \to B$
- 等价地证明
    - 前提：$A\_1, A\_2, \ldots, A\_k, C$
    - 结论：$B$

#### 归谬法
- 欲证
    - 前提：$A\_1, A\_2, \ldots, A\_k$
    - 结论：$B$
- 等价地证明
    - 前提：$A\_1, A\_2, \ldots, A\_k, \neg B$
    - 结论：$0$


