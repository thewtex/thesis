#!/bin/bash

FONT=Verdana
WIDTH=796
LHEIGHT=45

for i in {0..3}
do
  convert -font $FONT -gravity center -size ${WIDTH}x${LHEIGHT} label:'a)' test.png
  convert -append iteration_${i}_metric.png test.png test2.png

  convert -resize ${WIDTH}x iteration${i}_disp_labels.png test3.png
  convert -font $FONT -gravity center -size ${WIDTH}x${LHEIGHT} label:'b)' test4.png
  convert -append test3.png test4.png test5.png

  convert -resize ${WIDTH}x iteration${i}_strain_labels.png test6.png
  convert -font $FONT -gravity center -size ${WIDTH}x${LHEIGHT} label:'c)' test7.png
  convert -append test6.png test7.png test8.png

  convert +append test2.png test5.png test9.png
  convert +append test9.png test8.png test10.png

  cp test10.png iteration_${i}.png
done

rm test*.png

