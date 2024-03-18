@echo off
setlocal

REM Create the main folder
mkdir temp_project

REM Create the Content folder inside temp_project
mkdir temp_project\Content

REM Create the temp.uproject file inside temp_project
echo. > temp_project\temp.uproject

echo Folder structure created successfully.
pause
