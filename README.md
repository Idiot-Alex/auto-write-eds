# auto-write-eds
auto write eds

## usage
```
cd {{project directory}}

python main.py --name xxx --password xxx
```

## build 
- Mac OS
```
pip install pyinstaller
pip install playwright
PLAYWRIGHT_BROWSERS_PATH=0 playwright install chromium
pyinstaller -n auto-write-eds -F main.py
```
- windows
```
pip install pyinstaller
pip install playwright
set PLAYWRIGHT_BROWSERS_PATH=0 playwright install chromium
pyinstaller -n auto-write-eds -F main.py
```