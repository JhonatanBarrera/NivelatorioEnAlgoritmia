@echo off
FOR /L %%G IN (0,1,9) DO python MetodosDeOrdenamiento\Metodo\Metodo.ext -f MetodosDeOrdenamiento\DataSet\Archivo%%G.txt >> tiemposOrdenamiento.txt