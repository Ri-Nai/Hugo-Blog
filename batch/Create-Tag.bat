@echo off
cd D:\Code\Ri-Nai.github.io
echo Create-Tag
set /p input= Please input the name of the Tag:
hugo new tags/%input%/_index.md
pause
