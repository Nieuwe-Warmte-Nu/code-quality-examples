
pushd .
cd /D "%~dp0"

cd ..\..\
.\venv\bin\activate
set PYTHONPATH=.\src\;%$PYTHONPATH%
pytest
popd