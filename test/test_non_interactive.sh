set -x
cat test/s1.json | python -mqic 

sleep 1; cat test/s1.json | python -mqic "_"

sleep 1; cat test/s1.json | python -mqic "_[]"

sleep 1; cat test/s1.json | python -mqic "_[].{quantity,_id.<\$oid>}" 

sleep 1; cat test/s1.json | python -mqic "_l2t(_[].{quantity,_id.<\$oid>})"

set +x
