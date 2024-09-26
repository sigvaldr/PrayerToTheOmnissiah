@echo off
echo "Compiling and Building..."
pyinstaller --onefile --icon icon.ico --log-level=WARN main.py
