set -e
set -x
autopep8 --in-place --aggressive --aggressive csvCardParse.py
autopep8 --in-place --aggressive --aggressive classes/*.py
