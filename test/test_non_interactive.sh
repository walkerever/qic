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
set +x; sleep $interval;

eval "$clearscr";title="convert JSON to YAML or XML. please be noted, YAML or XML is also valid source for qic, just specify -t YAML or -t XML."
echo $nnn; (( nnn = nnn + 1 )) ;   echo $title;  sleep $titletime; set -x; 
echo "# JSON"
cat test/s6.json 
sleep $interval &&  eval "$clearscr"
echo "# to YAML"
cat test/s6.json  | python -mqic _y 
sleep $interval &&  eval "$clearscr"
echo "# to XML"
cat test/s6.json  | python -mqic _x 
set +x; sleep $interval;


eval "$clearscr";title="dump data structure in a 'flat' way. could be eaiser to grep."
echo $nnn; (( nnn = nnn + 1 )) ;   echo $title;  sleep $titletime; set -x; 
cat test/s6.json | python -mqic -s
set +x; sleep $interval;


eval "$clearscr";title="select keys"
echo $nnn; (( nnn = nnn + 1 )) ;   echo $title;  sleep $titletime; set -x; 
python3 -mqic -f test/s6.json "_.users[].{ userid   ,firstname, lastname }"
set +x; sleep $interval;


eval "$clearscr";title="slices"
echo $nnn; (( nnn = nnn + 1 )) ;   echo $title;  sleep $titletime; set -x; 
cat test/s6.json  | python -mqic "_.users[1:3].{firstname,lastname}"
echo $nnn; (( nnn = nnn + 1 )) ;   echo $title;  sleep $titletime; set -x; 
cat test/s6.json  | python -mqic "_.users[1:3].{firstname,lastname}"
echo $nnn; (( nnn = nnn + 1 )) ;   echo $title;  sleep $titletime; set -x; 
cat test/s6.json  | python -mqic "_.users[1:].{firstname,lastname}"
echo $nnn; (( nnn = nnn + 1 )) ;   echo $title;  sleep $titletime; set -x; 
cat test/s6.json  | python -mqic "_.users[:3].{firstname,lastname}"
echo $nnn; (( nnn = nnn + 1 )) ;   echo $title;  sleep $titletime; set -x; 
cat test/s6.json  | python -mqic "_.users[:].{firstname,lastname}"
set +x; sleep $interval;



eval "$clearscr";title="slices special situation"
echo $nnn; (( nnn = nnn + 1 )) ;   echo $title;  sleep $titletime; set -x; 
cat test/s6.json  | python -mqic "_.users[1: 2   ].{firstname,lastname}"
echo $nnn; (( nnn = nnn + 1 )) ;   echo $title;  sleep $titletime; set -x; 
cat test/s6.json  | python -mqic "_.users[-1].{firstname,lastname}" 
set +x; sleep $interval;



eval "$clearscr";title="tee to output file. could be useful when want a text file with colored code. bash redirection cannot gurantee that."
echo $nnn; (( nnn = nnn + 1 )) ;   echo $title;  sleep $titletime; set -x; 
cat test/s1.json | python -mqic -o /tmp/x.txt 
echo "sleep 2"
cat /tmp/x.txt
set +x; sleep $interval;









