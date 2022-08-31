#!/bin/bash

for word in `egrep "bit$" /usr/share/dict/words`; do
   wordbyte=`echo $word|sed 's/bit$/byte/'`
   python3 download-photo-from-google.py $word img/tmp.png
   if [ $? != 0 ];then
      continue
   fi
   convert img/tmp.png -resize x200 img/tmp.png
   magick montage -tile 4x -title $wordbyte img/tmp.png img/tmp.png img/tmp.png img/tmp.png img/tmp.png img/tmp.png img/tmp.png img/tmp.png img/bottom.png
   magick montage -tile 1x -title $word img/tmp.png img/bottom.png -mode Concatenate img/$word.png
done

rm img/tmp.png