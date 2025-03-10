---
title: "《云计算及应用》实验一-云服务体验"
slug: "2025/03/10/《云计算及应用》 实验一 云服务体验"
description:
date: "2025-03-10T13:22:42+08:00"
lastmod: "2025-03-10T13:22:42+08:00"
#image: cover.png
math:
license:
hidden: false
draft: false
categories: 
    - 学习笔记
    - 实验报告
tags: 
    - 云计算及应用
---

## Linux 虚拟机

### 购买服务器

先前在寒假期间购置了一台 腾讯云 的轻量应用服务器，想自己试试把博客搭建在上面，同时学习一下 `docker` 的使用。

配置在图中有显示：

![](imgs/消费记录.png)

### 安装系统

由于目前在上面有我几个比较常用的服务，因此需要先将当前的服务器制作为镜像，以便于后续的使用。

![](imgs/制作镜像.png)

过了大概 10 分钟，镜像制作完成，我们选择

![](imgs/重装系统.png)

个人使用，出于习惯选了 `Ubuntu 24.04` ，然后设置密码

![](imgs/选择系统.png)

![](imgs/设置密码.png)

可以看到正在重装中

![](imgs/正在重装.png)

看到系统盘只剩 `5G` 左右的占用，代表重装完成了

![](imgs/重装完成.png)

### 连接服务器

#### 使用腾讯云终端

腾讯云提供了一个在线的终端 `WebUI` ，可以直接在浏览器中连接服务器

![](imgs/腾讯云终端入口.png)

点击登录，即可连接到服务器

![](imgs/腾讯云终端.png)

#### 使用 `ssh` 连接

输入命令 `ssh ubuntu@<server-ip>`

![](imgs/不配置使用ssh连接.png)

翻阅资料，需要删除旧的配置。

输入命令 `ssh-keygen -R <server-ip>`

![](imgs/删除旧配置.png)

然后再次 `ssh` 连接，输入密码即可

![](imgs/连接成功1.png)

![](imgs/连接成功2.png)

#### 使用 `VSCode-SSH` 连接

对于一些文件操作，我还是更喜欢用图形化的界面，而 `VSCode` 对于远程开发的支持非常好，平时一般都是用它来连接服务器。

![](imgs/新建VSCode窗口.png)

点击左下角的 `打开远程窗口`，然后点击 `连接到主机-Remote-SSH`

![](imgs/VSCode远程连接.png)

点击 `添加新的 SSH 主机`

输入 `ssh ubuntu@<server-ip>`

然后选择存 `ssh` 密钥的文件，我这里选择在用户目录下的

![](imgs/设置配置.png)

然后就可以连接了

选择打开文件夹

![](imgs/打开文件夹.png)

默认打开到 `/home/ubuntu(username)` 目录下，即 `~` 目录 

可以看到侧边栏的文件树已经显示了服务器上的文件

![](imgs/服务器的文件.png)

### 简单的使用

课件内提到的命令有这些
1. 通过 `mkdir` 新建一个以姓名全拼命名的文件夹；
2. 通过 `cd` 进如文件夹，使用 `vim` 在文件夹中新建 "hello" 文件；
3. 在 "hello" 输入中输入 `echo "Hello Cloud Computing"` ；
4. 使用 `ls` 查看文件；
5. 为 "hello" 文件增加执行权限；
6. 执行 "hello" 查看结果；
7. 使用 `rm` 删除文件夹。

以下是我在服务器上的操作

![](imgs/操作打码.png)

![](imgs/vim-use.png)

### 简单的配置


因为我习惯用 zsh，所以安装了 zsh 和 oh-my-zsh，主要是为了好看以及方便使用。（优秀的自动补全和高亮插件）


#### zsh
```bash
sudo apt install -y zsh # 安装 zsh
sudo usermod -s /bin/zsh ubuntu # 切换默认 shell
```

#### oh-my-zsh

```bash
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

#### 插件

```bash
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM:=~/.oh-my-zsh/custom}/plugins/zsh-completions
```


修改 `.zshrc` 文件，添加插件
```bash
sudo vim ~/.zshrc
plugins=(git zsh-syntax-highlighting zsh-autosuggestions zsh-completions)
```

#### 主题:Powerlevel10k

```bash
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

修改 `.zshrc` 文件，添加主题

```bash
ZSH_THEME="powerlevel10k/powerlevel10k"
```
重启终端，根据提示配置主题。

最终效果如下

![](imgs/最终效果.png)
