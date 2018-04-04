# Parsing Images to CSVs

A `Python 3` script that takes in a directory of paired images, joins them in `CSV` fields, and writes the resultig pairs. Intended use is to package flashcard images for importing to `Anki` or `Quizlet`.

# Usage:
`py script.py inputDirectory outputDirectory`

# Arguments:
Input:
A directory containing images n-f.png for front, and n-b.png for back.
```
inputDirectory
├── 0-b.png
└── 0-f.png
```

Result:
A directory contianing placed images and the resulting `CSV` file.
```
outputDirectory:
├── 0912379082173097120987.png
├── 1210983091283091289030.png
└── output.csv
```

# CSV Structure:
Field0 | Field1
--- | ---
 | `<img src='0912379082173097120987.png'/>` | `<img sr='1210983091283091289030.png'/>`
