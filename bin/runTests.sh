set -x
for directory in tests/*;
do
    if [ -d "${directory}" ]; then
    rm -rf $directory/output
    python3 csvCardParse.py $directory/input $directory/output
    fi
done
