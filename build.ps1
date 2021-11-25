# requires `pip install pyinstaller`
pyinstaller --onefile D2R_ip.py --version-file version_info.py --exclude-module _bootlocale --add-data "files\diablo-skull_39227.ico;files" --icon "files\diablo-skull_39227-white.ico"

$publishPath = ".\dist\D2R_ip\"
$publishFilesPath = (Join-Path $publishPath "files\")
New-Item -ItemType Directory -Force -Path $publishFilesPath
Copy-Item -Path "D2R_ip.py" -Destination $publishPath
Copy-Item -Path  ".\files\diablo-skull_39227.ico" -Destination $publishFilesPath
Compress-Archive -Path $publishPath -Destination ".\dist\D2R_ip.zip" -Force
Remove-Item $publishPath -Recurse -Force

Get-ChildItem ".\scripts\*.ps1" | Compress-Archive -DestinationPath ".\dist\firewall-scripts.zip" -Force
