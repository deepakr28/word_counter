## Description

## Install Instructions
### pre-req
1. install pip https://packaging.python.org/en/latest/tutorials/installing-packages/
2. install pipenv https://pipenv.pypa.io/en/latest/installation.html

### how to install the script
1. `unzip <downloaded_zip_file>`
2. `pipenv shell`

(second command will automatically create a venv with required libs)

## Usage Instructions
After pipenv shell command following command should be executed in virtual env
1. Help option to run script - `python script.py --help`
2. Running the script with the input files - `python3 script.py -c content_file -p predefined_word`

## Sample Run
python3 script.py -c content_file -p predefined_words
content_file contains about 30000 lines of text, predefined_words 

Predefined Word | Match Count 
--- | --- 
Amen | 72
families | 149
Merari | 31
Deepak | 0
Christ | 494
amen | 1

## Assumptions
1. Any special character at the end of the word should be discarded
2. If any word which is present in predefined list but not present is content is shows as 0
3. If there is any special character in predefined list then it is ignored
