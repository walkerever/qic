nnn=0
titletime=2
interval=2
clearscr="clear"


eval "$clearscr";

echo "test/s1.json" && cat test/s1.json | head -35 && sleep 5

eval "$clearscr"; title="by default will show as JSON"
echo $nnn; (( nnn = nnn + 1 )) ;   echo $title;  sleep $titletime; set -x; 
cat test/s1.json | python -mqic 
set +x;  sleep $interval;

eval "$clearscr"; title="_ is the default, the data struture of the whole JSON/YAML/XML"
echo $nnn; (( nnn = nnn + 1 )) ;   echo $title;  sleep $titletime; set -x; 
cat test/s1.json | python -mqic "_"
set +x;  sleep $interval;

eval "$clearscr"; title="show list"
echo $nnn; (( nnn = nnn + 1 )) ;   echo $title;  sleep $titletime; set -x; 
cat test/s1.json | python -mqic "_[]"
set +x;  sleep $interval;

eval "$clearscr"; title="for each list, show specified keys. if there's special char, use <> as safety ."
echo $nnn; (( nnn = nnn + 1 )) ;   echo $title;  sleep $titletime; set -x; 
cat test/s1.json | python -mqic "_[].{quantity,_id.<\$oid>}" 
set +x;  sleep $interval; sleep $interval;

eval "$clearscr"; title="print table"
echo $nnn; (( nnn = nnn + 1 )) ;   echo $title;  sleep $titletime; set -x; 
cat test/s1.json | python -mqic "_l2t(_[].{quantity,_id.<\$oid>})"
set +x;  sleep $interval;


eval "$clearscr";
echo "test/s2.json" && cat test/s2.json | head -35 && sleep 5


eval "$clearscr"; title="for a long list, only show 2 rows. this applies to all lists."
echo $nnn; (( nnn = nnn + 1 )) ;   echo $title;  sleep $titletime; set -x; 
cat test/s2.json  | python -mqic -l2
set +x;  sleep $interval;

eval "$clearscr"; title="shrink+table"
echo $nnn; (( nnn = nnn + 1 )) ;   echo $title;  sleep $titletime; set -x; 
cat test/s2.json  | python -mqic -l2 _.colors | python -mqic _l2t
set +x;  sleep $interval;


eval "$clearscr";
echo "test/s3.json" && cat test/s3.json | head -35 && sleep 5


eval "$clearscr";title="keys selection, can be at different levels."
echo $nnn; (( nnn = nnn + 1 )) ;   echo $title;  sleep $titletime; set -x; 
cat test/s3.json  | python -mqic "_.items[].{kind,id.kind}"
set +x;  sleep $interval;


eval "$clearscr";
echo "test/s4.json" && cat test/s4.json | head -35 && sleep 5

eval "$clearscr";title="show keys for a dict, helpful for following queries"
echo $nnn; (( nnn = nnn + 1 )) ;   echo $title;  sleep $titletime; set -x; 
cat test/s4.json  | python -mqic "_[0].keys()"
set +x;  sleep $interval;

eval "$clearscr";
echo "test/s5.json" && cat test/s5.json | head -35 && sleep 5

eval "$clearscr";title="merge two lists"
echo $nnn; (( nnn = nnn + 1 )) ;   echo $title;  sleep $titletime; set -x; 
cat test/s5.json  | python -mqic "_.batters.batter + _.topping" | python -mqic _l
set +x;  sleep $interval;

eval "$clearscr";
echo "test/s6.json" && cat test/s6.json | head -35 && sleep 5

eval "$clearscr";title="dump user tables"
echo $nnn; (( nnn = nnn + 1 )) ;   echo $title;  sleep $titletime; set -x; 
cat test/s6.json  | python -mqic "_l2t(_.users)"
set +x; 


