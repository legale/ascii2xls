# ascii2xls
python3 script to convert ascii pseudo table to xls, xlsx or csv format

## System requirements
python3
python3 modules: 
bs4 docutils dashtable pandas openpyxl xlwt

## Syntax
```
./ascii2xls.py SRC_PSEUDO_TABLE_FILE [DST_CSV_FILE]
```
Argument 2 is optional. Default destination format is `xlsx`. If you need
`csv` or `xls` you need to pass destination filename.

## Usage example 
### Simple
Run: 
```
./ascii2xls.py text2.txt
```
to convert pseudo table in `text2.txt` to `xlsx` format to `text2.txt.xlsx`

### To csv
Run: 
```
./ascii2xls.py text2.txt text2.csv
```
to convert pseudo table in `text2.txt` to `csv` format to `text2.csv`
