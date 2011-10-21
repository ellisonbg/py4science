@rem IPython Notebook startup file (with pylab activated by default)
@echo ***********************************************************************
@echo In order to stop the IPython notebook, press Control-C.
@echo ***********************************************************************
@ipython notebook --pylab inline --no-browser --notebook-dir %~dp0
