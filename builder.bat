@echo off
rem Replace 'my_icon.ico' with the correct icon file name or path
rem Replace 'MSFS 2020.py' with the correct Python script name or path

rem Create the .exe file using pyinstaller
pyinstaller --onefile --windowed --icon="my_icon.ico" "MSFS 2020.pyw"

rem Pause to see any errors if they occur
pause
