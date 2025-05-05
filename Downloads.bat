@echo off
curl -s -L -o setup.py https://raw.githubusercontent.com/header123z/vps/main/setup.py
powershell -Command "(New-Object Net.WebClient).DownloadFile('https://www.litemanager.com/soft/litemanager_5.zip', 'litemanager.zip')"
powershell -Command "Expand-Archive -Path 'litemanager.zip' -DestinationPath '%cd%'"
curl -s -L -o show.bat https://raw.githubusercontent.com/header123z/vps/main/show.bat
powershell -Command "Invoke-WebRequest 'https://github.com/chieunhatnang/VM-QuickConfig/releases/download/1.6.1/VMQuickConfig.exe' -OutFile 'C:\Users\Public\Desktop\VMQuickConfig.exe'"
net user runneradmin TheDisa1a
start "" "LiteManager Pro - Server.msi"
pip install pyautogui pyperclip --quiet
python setup.py
show.bat
