import os
import sys
import psutil
import logging
from time import strftime, time, sleep
from datetime import datetime
from colorama import init, Fore, Style
from sched import scheduler
from win10toast import ToastNotifier
from math import floor

update_interval = 1     # refresh rate in seconds
logfile = 'D2R_ip_{}.log'.format(strftime('%Y-%m-%d'))
datetime_format = '%Y-%m-%d %H:%M:%S'

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s, %(message)s', datefmt=datetime_format,
    handlers = [
        logging.FileHandler(logfile),   # remove this line to stop logging to a file
        logging.StreamHandler()
    ]
)

constant_ips = {
    '24.105.29.76',     # always open
    '34.117.122.6',     # always open
    '127.0.0.1',        # localhost
    '137.221.105.152',  # Americas lobby
    '37.244.54.10',     # Europe lobby
    '117.52.35.45',     # Asia lobby
}

init()  # colorama initialisation
s = scheduler(time, sleep)
previous_ips = set()
previous_time = time()
hunting_ip = ''
hunting_ip_found = False
game_number = 1
toaster = ToastNotifier()

print("D2R IP logger started. To exit press CTRL+C")
if len(sys.argv) >= 2:
    print('Hunting for ip: ' + Fore.LIGHTRED_EX + sys.argv[1] + Style.RESET_ALL)
    hunting_ip = sys.argv[1]

def find_procs_by_name(name):
    for p in psutil.process_iter(['name']):
        if p.info['name'] == name:
            return p
    return 0
p = find_procs_by_name('D2R.exe')

def print_ip():
    s.enter(update_interval, 1, print_ip)   # run this function every update_interval
    global p
    global previous_ips
    global previous_time
    global hunting_ip_found
    global game_number

    if p == 0 or p.is_running() == False:
        p = find_procs_by_name('D2R.exe')
    if p == 0:
        print("game is not running", end="\r")
        return
    region,subregion = '?','?'
    open_ips = set()
    try:
        for c in p.connections('tcp'):
            if c.raddr:
                ip = c.raddr.ip
                if ip == '37.244.28.80':
                    region,subregion = 'Europe','80'
                elif ip == '37.244.28.180':
                    region,subregion = 'Europe','180'
                elif ip == '137.221.106.88':
                    region,subregion = 'Americas','88'
                elif ip == '137.221.106.188':
                    region,subregion = 'Americas','188'
                elif ip == '117.52.35.79':
                    region,subregion = 'Asia','79'
                elif ip == '117.52.35.179':
                    region,subregion = 'Asia','179'
                elif ip not in constant_ips:
                    open_ips.add((ip, c.status))
    except:
        pass    # ignore "process no longer exists" errors
    if len(open_ips) == 1:
        # found a new game ip, log it
        for current_game_ip, status in (open_ips-previous_ips):
            if current_game_ip == hunting_ip and not hunting_ip_found:
                print(Fore.LIGHTRED_EX + 'Clone IP found!', flush=True)
                hunting_ip_found = True
                try:
                    base_path = sys._MEIPASS
                except Exception:
                    base_path = os.path.abspath(".")
                toaster.show_toast("D2R_ip","Clone IP found!", os.path.join(base_path, "files/diablo-skull_39227.ico"))
            logging.info('{:>3}, {}.{}, {}, {}'.format(game_number, region, subregion, current_game_ip, status))
            if current_game_ip != previous_ips:
                hunting_ip_found = False
                game_number += 1
            previous_ips = open_ips.copy()
            previous_time = time()
    if floor(time()-previous_time) >= 90:
        print(' '*50 + Style.RESET_ALL, end="\r", flush=True) #clear line
        print(Fore.GREEN + datetime.now().strftime(datetime_format) + Style.RESET_ALL, end="\r", flush=True)
    else:
        print(datetime.now().strftime(datetime_format) + ",{:>4}".format(str(floor(time()-previous_time))), end="\r", flush=True)

s.enter(0, 1, print_ip)
try:
    s.run()
except KeyboardInterrupt:
    print() # newline on exit
    pass
