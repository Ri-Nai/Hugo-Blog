@echo off
echo Create-Blog
set /p input= Please input the Slug of the Blog:
hugo new post/%Date:~0,4%/%Date:~5,2%-%Date:~8,2%-%input%/index.md
pause
