@rem IPython Notebook startup file (with pylab activated by default)
@echo off
@echo.
@echo ********************************************************************
@echo.
@echo            Welcome to the IPython Notebook Environment
@echo.
@echo   Please open Chrome or Firefox and open the following address:
@echo.  
@echo                     http://127.0.0.1:8888
@echo.
@echo   When finished, stop the notebook by pressing in this window:
@echo.
@echo                          Control-C
@echo.
@echo ********************************************************************
@echo.
@ipython notebook --pylab inline --no-browser --port 8888 --notebook-dir %~dp0
