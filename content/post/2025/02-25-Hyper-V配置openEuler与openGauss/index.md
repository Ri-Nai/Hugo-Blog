---
title: "Hyper V 配置 openEuler 与 openGauss"
slug: "2025/02 25 Hyper V配置openEuler与openGauss"
description:
date: "2025-02-25T19:23:12+08:00"
lastmod: "2025-02-25T19:23:12+08:00"
#image: cover.png
math:
license:
hidden: false
draft: false
categories: [""]
tags: [""]
---

## 启用 Hyper-V

Hyper-V 是 Windows 自带的虚拟化软件，可以用来创建虚拟机。（主要是懒得装 VMware）

首先启用 Hyper-V 功能。

## 安装 openEuler

### 下载镜像

openGauss 官网上推荐使用 CentOS 7.6，但是 CentOS 7.6 早就不维护了。我一开始使用的时候出了很多问题（比如 yum 的镜像源设置），所以我决定向华为低头。

{{< linkpage  "https://www.openeuler.org/zh/download/#openEuler%2024.03%20LTS%20SP1" "openEuler 24.03 LTS SP1" "" "https://www.openeuler.org/favicon.ico" >}}

### 导入镜像

按镜像导入 Hyper-V，然后安装 openEuler。自己设置一下内存和硬盘大小。网络连接选 Default Switch，其他基本就默认。

如果你连接虚拟机发现一片黑，点开虚拟机的设置 > 安全，把启用安全启动关掉。

### 安装 openEuler

1. 连接以太网，不然话没法联网。
2. 设置 root 密码和创建用户，据说不建议直接用 root。  
   笑点解析：如果用户未设置密码，没法通过 SSH 连接，所以要设置密码。
3. 安装完成后，重启。

### SSH 连接

可以直接在 Hyper-V 下面的详细信息里面看到 IP 地址，然后用 SSH 连接。

```bash
ssh reina@<your-ip>
```

我这里没配置其他任何的东西了，可以直接 ssh 到虚拟机。

不过据说这样的话，虚拟机的 IP 地址会变，所以可以设置静态 IP。我还没试过。

#### VSCode SSH 连接

由于这个 openEuler 实在是太垃圾了，连 VSCode 的时候都卡了我好久。

1. 安装 `tar`，笑点解析：openEuler 默认没有安装 `tar`，所以要安装。  
    ```bash
    sudo yum install -y tar
    ```
2. 

### 安装 zsh

因为我习惯用 zsh，所以安装了 zsh 和 oh-my-zsh，主要是为了好看。

参考文献：
{{< linkpage "https://blog.csdn.net/qimowei/article/details/119517167" "Centos7-Linux安装zsh和oh-my-zsh(内含国内安装方法)" "" "https://g.csdnimg.cn/static/logo/favicon32.ico">}}
{{< linkpage "https://zhuanlan.zhihu.com/p/265525597" "Oh My Zsh, 『 Powerlevel10k 安装 & 配置 』" "" "https://static.zhihu.com/heifetz/assets/apple-touch-icon-152.81060cab.png">}}

#### zsh
```bash
sudo yum install -y zsh # 安装 zsh
usermod -s /bin/zsh reina # 切换 shell
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
vim ~/.zshrc
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

## 安装 openGauss
参考文档 
{{< linkpage "https://docs.opengauss.org/zh/docs/6.0.0/docs/InstallationGuide/%E6%9E%81%E7%AE%80%E7%89%88%E5%AE%89%E8%A3%85.html" "极简版安装文档" "" "https://docs.opengauss.org/favicon.ico" >}}

### 软件环境

#### 安装了 python3

```bash
sudo yum install -y python3.11
alias python=python3
```

#### 提前建立软件目录

```bash
sudo mkdir -p /opt/software/openGauss
sudo chmod -R 777 /opt/software/openGauss # 不然会有权限问题，我也不知道到底在哪所以就直接 chmod 777 了
```
#### 关闭防火墙

```bash
# 禁用 selinux
vim /etc/selinux/config
SELINUX=disabled
# 重启
reboot
# 关闭防火墙
systemctl disable firewalld.service
systemctl stop firewalld.service
# 查看状态
systemctl status firewalld
```


### 安装 openGauss

下载 openGauss 安装包，我安装的是极简版
{{< linkpage "https://opengauss.org/zh/download/" "openGauss Download" "" "https://opengauss.org/favicon.ico" >}}

```bash
# 下载压缩包
curl -O https://opengauss.obs.cn-south-1.myhuaweicloud.com/6.0.1/openEuler22.03/x86/openGauss-Server-6.0.1-openEuler22.03-x86_64.tar.bz2
# 解压到 /opt/software/openGauss
tar -jxf openGauss-Server-6.0.1-openEuler22.03-x86_64.tar.bz2 -C /opt/software/openGauss 

cd /opt/software/openGauss
# 必须要用 bash，因为他 install.sh 里有一堆 .bashrc 的操作
bash install.sh  -w "xxxx" -p 5432 &&source ~/.bashrc
```
至此，openGauss 安装完成。

不要看着我说起来风轻云淡，我似乎被折磨了两天。（虚拟机网络以及各种权限问题）。

### 检查是否安装成功

```bash
ps ux | grep gaussdb
gs_ctl query -D /opt/software/openGauss/data/single_node
```
理应来说第一个命令会有一个 `gaussdb` 的进程，第二个命令会显示数据库状态。

### 连接数据库

还没学会，就不写了。
