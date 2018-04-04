set -x
for directory in /tests/;
do
    echo "$directory"
    if [ -d "${D}" ]; then
    rm -rf tests/$directory/output
    python3 csvCardParse.py tests/$directory/input tests/$directory/output
    fi
done
