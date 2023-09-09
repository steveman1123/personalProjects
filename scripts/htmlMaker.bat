set origDir="%cd%"
@echo off
cls
:start
cd %origDir%
set /p name="Name of page: "

echo ^<!DOCTYPE html^> >>%name%.html
echo.>>%name%.html
echo ^<html^> >>%name%.html
echo.    ^<meta charset="utf-8"^> >>%name%.html
echo.    ^<meta name="description" content=""^> >>%name%.html
echo.    ^<link rel="stylesheet" type="text/css" href="%name%/%name%.css"/^> >>%name%.html
echo.    ^<head^> >>%name%.html
echo.        ^<title^>^</title^> >>%name%.html
echo.    ^</head^> >>%name%.html
echo.    ^<body^> >>%name%.html
echo.        >>%name%.html
echo.    ^</body^> >>%name%.html
echo ^</html^> >>%name%.html

mkdir %name%
cd %name%
mkdir %name%Media
echo. >%name%.css

goto start