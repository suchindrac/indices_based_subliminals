set style line 1 lc rgb '#0060ad' lt 1 lw 2 pt 7 pi -1 ps 1.5
set pointintervalbox 3
set ytics 1
set term png
set output "converted.png"
plot filename with linespoints ls 1
set terminal x11
set output
replot
pause 3

