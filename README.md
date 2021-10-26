# D2R-IP-logger

A python script that can display the IP of your online game in Diablo II Resurrected, log ip, timestamp and region (EU/NA/Asia) to a csv, and notify when a provided IP is found.

Useful for hunting Diablo Clone and data collection.

![](https://i.imgur.com/yfUxfFu.png)

## How to install

A compiled version for Windows can be downloaded form the [Release Page](https://github.com/sir-wilhelm/D2R-IP-logger/releases), you can download it here:
[D2R_ip.exe](https://github.com/sir-wilhelm/D2R-IP-logger/releases/latest/download/D2R_ip.exe). You can also run the
[D2R_ip.py](https://github.com/sir-wilhelm/D2R-IP-logger/raw/main/D2R_ip.py) script itself by following the steps below:

If you don't have Python installed yet, install it from https://www.python.org/downloads/
On Windows during installation select "Add Python to PATH".

Install required Python libraries, by opening Command Prompt and typing:
`pip install psutil`
`pip install colorama`

Download the [D2R_ip.py](https://raw.githubusercontent.com/sir-wilhelm/D2R-IP-logger/main/D2R_ip.py) file.

## How to use

Run `D2R_ip.py`

On Windows you can either:
- double-click `D2R_ip.py` in File Explorer
- or open PowerShell (`Windows Key + r`, type `powershell`, press enter), navigate to the directory where you downloaded the file (i.e. type `cd C:\Users\YourUsername\Downloads\`) then type `py D2R_ip.py` or `python D2R_ip.py`.

To stop the program press CTRL+C or simply close the console window.

To hunt for a specific ip address:
- Run the script from PowerShell or Command Prompt and add the IP after D2R_ip.py ex: `python D2R_ip.py 4.20.66.69`

## Info

In the last line a clock is displayed, which will turn green after 1 minute since the last game creation (which is, as of now, the cooldown before the servers allow you to create a new game).

The logfiles appear in the same folder, with filenames `D2R_ip_*.log` where * is today's date.
If you don't want any logfiles created then modify the code, the instructions are in comments.

## How it works

The script in essence works the same way as `netstat`, [TCPView](https://docs.microsoft.com/en-us/sysinternals/downloads/tcpview) or `Resource Monitor` (a built-in Windows tool).

It asks your operating system what TCP connections are open by which processes using a standard Python library `psutil`. It doesn't require admin rights, doesn't inject or modify anything, doesn't break TOS.

## Other software

If you don't care about creating logs, you may try:
* [TCPView](https://docs.microsoft.com/en-us/sysinternals/downloads/tcpview) -  for more detailed overview of your system's TCP connections
* [D2R-IPTool](https://github.com/VideoGameRoulette/D2RTools) - for an in-game D2R overlay display of your IP, aimed to help in DClone hunting

## Thanks

Thanks to [nocawy](https://github.com/nocawy) for the original version of the [script](https://github.com/nocawy/D2R-IP-logger).

## License

[MIT License](/LICENSE.txt).