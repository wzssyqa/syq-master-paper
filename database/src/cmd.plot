set term png font '/usr/share/fonts/truetype/simsun.ttc,10' size 1280,800
set output "./plot/42.png"
set size 1,1
set grid
set xlabel "从第一次测量开始的天数"
set ylabel "』米毫『 量降沉的比相量测次一第与                                           百分比 量煤装" offset -5
plot "tmpf.tmp" using 1:4 title "1" w lines, "tmpf.tmp" using 1:5 title "2" w lines, "tmpf.tmp" using 1:6 title "7" w lines, "tmpf.tmp" using 1:7 title "8" w lines, "tmpf.tmp" using 1:3 w lines lt rgb "black" title "", "tmpf.tmp" using 1:2 title "装煤量 %" w lines

