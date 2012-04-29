set term png font '/usr/share/adobe/simsun.ttc,10' size 1280,800
set output "./plot/42-ica.png"
set output "./plot/42-ica.png"
set size 1,1
set grid
set xlabel "从第一次测量开始的天数"
set ylabel "装载量"
set y2label "温度"
plot "tmpf.tmp" using 1:2 title "装载量" w lines axes x1y1, "tmpf.tmp" using 1:3 title "温度" w lines axes x1y1, "tmpf.tmp" using 1:4 title "独立成分1" w lines axes x1y2, "tmpf.tmp" using 1:5 title "独立成分2" w lines axes x1y2, "tmpf.tmp" using 1:6 title "独立成分3" w lines axes x1y2, "tmpf.tmp" using 1:7 title "独立成分4" w lines axes x1y2;
