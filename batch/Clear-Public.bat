@echo off
cd D:\Code\Ri-Nai.github.io\public
setlocal enabledelayedexpansion

rem Define the exclusion directory
set EXCLUDE_DIR=.git

rem Delete all files except those in the exclusion directory
for %%i in (*.*) do (
    if /i not "%%i"=="%EXCLUDE_DIR%" (
        del /q "%%i"
    )
)

rem Delete all directories except the exclusion directory
for /d %%i in (*) do (
    if /i not "%%i"=="%EXCLUDE_DIR%" (
        rd /s /q "%%i"
    )
)

echo Done.
endlocal
cd ..
rmdir .\resources /s /q
hugo
