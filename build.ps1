# requires `pip install pyinstaller`
pyinstaller --onefile D2R_ip.py --version-file version_info.py --exclude-module _bootlocale
