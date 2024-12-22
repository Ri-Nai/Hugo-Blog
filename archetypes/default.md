---
title: "{{ replaceRE "-" " " (substr .Name 6) | title }}"
slug: "{{ replaceRE "-" " " .Name | title }}"
description:
date: "{{ .Date }}"
lastmod: "{{ .Date }}"
#image: cover.png
math:
license:
hidden: false
draft: false
categories: [""]
tags: [""]
---
