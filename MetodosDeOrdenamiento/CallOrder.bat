@echo off
FOR /L %%G IN (0,1,1) DO python %1 -f %2\Archivo%%G.txt >> %3