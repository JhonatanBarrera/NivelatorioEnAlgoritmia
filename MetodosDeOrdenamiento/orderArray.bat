@echo off
FOR /L %%G IN (%3,%4,%5) DO python %1 -f %2\Data0%%G.txt >> %6