#! /bin/csh
setenv REF1 /home/ambmax/base/augpcx_fin
setenv REF2 ../version-60-aug
#
foreach i (li be b c n o f ne na mg al si p s cl ar)
  foreach j (1 2)
    cp $REF1/"$i"-"$j".inp .
  end
  foreach j (3 4)
    cp $REF2/"$i"-"$j".inp .
  end
end
