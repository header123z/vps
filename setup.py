import pyautogui as pag
import time
import pyperclip
import subprocess

password = "TheDisa1a"

actions = [
    (610, 531, 3),  # next
    (286, 459, 3),  # Accept terms
    (610, 531, 3),  # next
    (610, 531, 3),  # next
    (610, 531, 3),  # next
    (610, 531, 3),  # install
    (387, 253, 10), # type pass
    (387, 298, 3),  # type pass
    (564, 598, 3),  # ok
    (610, 531, 2),  # finish + start
    (849, 746, 10), # open litemanager
    (522, 388, 3),  # click connect
    (522, 388, 1),  # click connect
    (460, 321, 3),  # right click
    (506, 387, 3),  # copy
]

time.sleep(10)
for x, y, duration in actions:
    if (x, y) in [(387, 253), (387, 298)]:
        pag.click(x, y, duration=duration)
        pag.typewrite(password)
    elif (x, y) == (460, 321):
        pag.rightClick(x, y, duration=duration)
    elif (x, y) == (610, 531) and duration == 2:
        pag.click(x, y, duration=duration)
        subprocess.run(r'"C:\Program Files (x86)\LiteManager Pro - Server\ROMServer.exe" /start', shell=True)
    else:
        pag.click(x, y, duration=duration)

def save_echo(file, text):
    with open(file, 'a') as f:
        f.write(f'\necho {text}')

def save_info():
    clipboard = pyperclip.paste()
    save_echo('show.bat', f'LiteManager ID: {clipboard}')
    save_echo('show.bat', f'LiteManager Password: {password}')

save_info()
