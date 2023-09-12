# auto-write-eds
auto write eds

## usage
```
cd {{project directory}}

python main.py --name xxx --password xxx
```

## build 

```
pip install playwright
set PLAYWRIGHT_BROWSERS_PATH=0
playwright install chromium
pyinstaller -n auto-write-eds -F main.py
```