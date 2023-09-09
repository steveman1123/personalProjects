rem set up UI
title Folder Contents
@echo off & cls
set path=%cd%
if exist common.txt ( del common.txt )
if exist different.txt ( del different.txt )

rem input dirs
set /p lib1="Library 1 path (include drive):"
set /p lib2="Library 2 path (include drive):"

rem move libraries text to batch dir
%lib1:~0,2%
cd %lib1%
dir /ad /b /on >> "lib_1.txt"
move %cd:~0,2%"%cd:~2%\lib_1.txt" "%path%\lib_1.txt"

%lib2:~0,2%
cd %lib2%
dir /ad /b /on >> "lib_2.txt"
move %cd:~0,2%"%cd:~2%\lib_2.txt" "%path%\lib_2.txt"

rem compare files, store to folders, del old dirs
%path:~0,2%
cd %path%
%systemroot%\system32\findstr /ig:"lib_1.txt" "lib_2.txt" >> "Common.txt"


echo These are in %lib1% but not in %lib2%>> "Different.txt"
echo.>> "Different.txt"
%systemroot%\system32\findstr /vig:"lib_2.txt" "lib_1.txt" >> "Different.txt"

del lib_1.txt
del lib_2.txt
pause