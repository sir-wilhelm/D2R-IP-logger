# requires `pip install pyinstaller`
pyinstaller --onefile D2R_ip.py --version-file version_info.py --exclude-module _bootlocale --add-data "files\diablo-skull_39227.ico;files" --icon "files\diablo-skull_39227-white.ico"
