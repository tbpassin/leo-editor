echo off
cls
rem -a: write all files  (make clean)
cd C:\Repos\leo-editor\doc\html
echo.
echo sphinx-build -a (make clean)
echo.
sphinx-build -M html . _build -a
