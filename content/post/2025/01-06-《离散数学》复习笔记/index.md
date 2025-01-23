---
title: "《离散数学》复习笔记"
slug: "2025/01 06 《离散数学》复习笔记"
description:
date: "2025-01-06T11:13:33+08:00"
lastmod: "2025-01-06T11:13:33+08:00"
image: cover.png
math:
license:
hidden: false
draft: false
categories: ["学习笔记"]
tags: ["离散数学", "计算机科学"]
---

# {{< linking "数理逻辑" >}} <button onclick="toggleContent('content0')" id="button0"></button>
<div id="content0" style="display:none;">
    {{< include "数理逻辑/index.md" >}}
</div>


# {{< linking "集合论" >}} <button onclick="toggleContent('content1')" id="button1"></button>
<div id="content1" style="display:none;">
    {{< include "集合论/index.md" >}}
</div>

# {{< linking "代数结构" >}} <button onclick="toggleContent('content2')" id="button1"></button>
<div id="content2" style="display:none;">
    {{< include "代数结构/index.md" >}}
</div>

# {{< linking "图论" >}} <button onclick="toggleContent('content3')" id="button1"></button>
<div id="content3" style="display:none;">
    {{< include "图论/index.md" >}}
</div>

<style>
    .article-content button {
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
    .article-content button:before {
        content: "显示内容";
    }
    .article-content button:after {
        content: "隐藏内容";
        display: none;
    }
    .article-content button.active {
        background-color: #FF9800; /* Orange when active */
    }
    .article-content button.active:before {
        display: none;
    }
    .article-content button.active:after {
        display: inline;
    }
    .article-content button:hover {
        background-color: #005f73; /* Darker blue on hover */
    }
    .article-content button.active:hover {
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
