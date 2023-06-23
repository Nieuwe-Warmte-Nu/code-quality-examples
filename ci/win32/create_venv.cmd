rem Short script to initialize virtual environment using venv and pip
rem @echo off

pushd .
cd /D "%~dp0"
python3 -m venv ..\..\venv
call ..\..\venv\bin\activate.bat
python -m pip install pip-tools
popd
