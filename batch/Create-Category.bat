@echo off
cd D:\Code\Ri-Nai.github.io
echo Create-Category
set /p input= Please input the name of the Category:
hugo new categories/%input%/_index.md
pause
