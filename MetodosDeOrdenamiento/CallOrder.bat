@echo off
FOR /L %%G IN (0,1,9) DO python %1 -f %2\Archivo%%G.txt >> %3