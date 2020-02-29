# Python scraper using selenium

## How to use

1. Run these commands on your teminal

```
pip3 install selenium
python scraper.py
```

or (in case you use python2)

```
pip install selenium
python scraper.py
```

2. Input dealer's name you are searching for.

The result will be saved in `data/result.csv` file

### on Windows

1. You need to install python2 or python3 on your pc.
2. Change the path on line 26 of the `scraper.py` file.

from

```
browser = webdriver.Chrome('./driver/chromedriver')
```

to

```
browser = webdriver.Chrome('./driver/chromedriver.exe')
```

3. Install selenium package

```
pip install selenium
```

4. Run script

```
python scraper.py
```

### Features

1. Remove popup
2. Search all result
3. Save them to csv file
