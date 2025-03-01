---
title: "《大学物理AII》复习笔记"
slug: "2024/12/16/《大学物理AII》复习笔记"
description:
date: "2024-12-16T20:59:12+08:00"
lastmod: "2024-12-16T20:59:12+08:00"
# image: cover.jpg
image: post/2024/12-16-大学物理aii复习笔记/cover.jpg
math:
license:
hidden: false
draft: false
categories: ["学习笔记"]
tags: ["大学物理", "电磁学", "近代物理"]
---

# {{< linking "电磁学" >}} <button onclick="toggleContent('content0')" id="button0"></button>
<div id="content0" style="display:none;">
    {{< include "电磁学/index_.md" >}}
</div>

<!-- # {{< linking "电磁学/常用公式" >}} <button onclick="toggleContent('content2')" id="button2"></button>
<div id="content2" style="display:none;">
    {{< include "电磁学/常用公式/index_.md" >}}
</div> -->


# {{< linking "近代物理" >}} <button onclick="toggleContent('content1')" id="button1"></button>
<div id="content1" style="display:none;">
    {{< include "近代物理/index_.md" >}}
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
