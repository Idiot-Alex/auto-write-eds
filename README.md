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
- windows (use powershell)
```
pip install pyinstaller
pip install playwright
$env:PLAYWRIGHT_BROWSERS_PATH="0"
playwright install chromium
pyinstaller -n auto-write-eds -F main.py
```

打包之后的使用方式：
- windows:
```
call auto-write-eds.exe --name xxx --password xxx
```
