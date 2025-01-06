---
title: "《数据结构与算法设计》复习笔记"
slug: "01 06 《数据结构与算法设计》复习笔记"
description:
date: "2025-01-06T11:13:33+08:00"
lastmod: "2025-01-06T11:13:33+08:00"
image: cover.png
math:
license:
hidden: false
draft: false
categories: ["学习笔记"]
tags: ["数据结构与算法设计", "计算机科学", "数据结构", "算法设计", "计算理论"]
---

# {{< linking "数据结构" >}} <button onclick="toggleContent('content0')" id="button0"></button>
<div id="content0" style="display:none;">
    {{< include "数据结构/index.md" >}}
</div>


# {{< linking "计算理论" >}} <button onclick="toggleContent('content1')" id="button1"></button>
<div id="content1" style="display:none;">
    {{< include "计算理论/index.md" >}}
</div>

<style>
    button {
        background-color: #008CBA; /* Blue */
        border: none;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 14px;
        margin-left: 10px;
        cursor: pointer;
        border-radius: 5px;
        transition: background-color 0.3s ease;
        float: right; /* Align to the right */
        align-items: center;
        justify-content: center;
    }
    button:before {
        content: "显示内容";
    }
    button:after {
        content: "隐藏内容";
        display: none;
    }
    button.active {
        background-color: #FF9800; /* Orange when active */
    }
    button.active:before {
        display: none;
    }
    button.active:after {
        display: inline;
    }
    button:hover {
        background-color: #005f73; /* Darker blue on hover */
    }
    button.active:hover {
        background-color: #EF6C00; /* Darker orange on hover when active */
    }
</style>

<script>
    function toggleContent(id) {
        var content = document.getElementById(id);
        var button = document.querySelector(`#button${id.slice(-1)}`);
        if (content.style.display === "none") {
            content.style.display = "block";
            button.classList.add('active');
        } else {
            content.style.display = "none";
            button.classList.remove('active');
        }
    }
</script>
