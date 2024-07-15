hugo
cd D:\Code\Ri-Nai.github.io\public
set /p input=input commit message
git init -b main
git remote add origin https://github.com/Ri-Nai/Ri-Nai.github.io.git
git add -A
git commit -m "%input% Updated by %Date:~0,4%-%Date:~5,2%-%Date:~8,2% %Time%"
git push -u -f origin main
cd ..
