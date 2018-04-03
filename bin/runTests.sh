set -x
for directory in 'find tests -  type d'
do
    if [ -d "${D}" ]; then
    rm -rf tests/$directory/output
    python3 csvCardParse.py tests/$directory/input tests/$directory/output
    fi
done
