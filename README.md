# D2R-IP-logger

A python script that can display the IP of your online game in Diablo II Resurrected, log ip, timestamp and region (EU/NA/Asia) to a csv, and notify when a provided IP is found.

Useful for hunting Diablo Clone or data collection.

![](https://i.imgur.com/q59EWIL.png)

## How to install

A compiled version for Windows can be downloaded form the [Release Page](https://github.com/sir-wilhelm/D2R-IP-logger/releases), you can download it here:
[D2R_ip.exe](https://github.com/sir-wilhelm/D2R-IP-logger/releases/latest/download/D2R_ip.exe).

You can also run the script manually by following the steps below:
* Install Python (If you don't have it)
  * https://www.python.org/downloads/
  * On Windows during installation select "Add Python to PATH"
* Install required Python libraries, by opening PowerShell and typing:
  * `python -m pip install --upgrade pip` (optional)
  * `pip install psutil`
    * If this fails due to `Microsoft Visual C++ 14.0 or greater is required`, install it (large download):
      * https://visualstudio.microsoft.com/visual-cpp-build-tools
      * Select the Individual components tab and select:
        * MSVC v142 - VS 2019 C++ x64/x86 build tools (latest)
        * Windows 10 SDK (any should work, I grabbed the highest version)
  * `pip install colorama`
  * `pip install win10toast`
* Download [D2R_ip.zip](https://github.com/sir-wilhelm/D2R-IP-logger/releases/latest/download/D2R_ip.zip) and extract the contents.

## How to use

On Windows you can either:
* double-click `D2R_ip.py` or `D2R_ip.exe` in File Explorer
* open PowerShell, navigate to the directory where you extracted the files (i.e. type `cd C:\Users\YourUsername\Downloads\D2R_ip\`) then type `python D2R_ip.py` or `py D2R_ip.py` or `D2R_ip.exe`.

To stop the program press `CTRL+C` or simply close the console window.

To hunt for a specific ip address:
* Run the application or script from PowerShell and add the IP after the command ex:
  * `python D2R_ip.py 4.20.66.69` or `py D2r_ip.py 4.20.66.69`
  * `D2R_ip.exe 4.20.66.69`

## Info

In the last line a clock is displayed, followed by the number of seconds that has passed since the last entry. After 90 seconds the clock will go green and the counter stops.

The logfiles appear in the same folder where the program is located, with filenames `D2R_ip_*.log` where `*` is today's date.
If you don't want any logfiles created then modify the code, the instructions are in comments.

It also includes an IP/game counter.

When `Diablo II: Resurrected` is launched and connects to battle.net it begins opening and closing connections to multiple IPs for about 20 seconds. The script might display some of them. If you create or join a game during that period, wait until no new IPs appear, the last (most recent) one will be your current game's IP.

Next to region a number is displayed, e.g. `Asia.79` or `Europe.180`, associated with what some call a *subregion* or a different *lobby*. When `Diablo II: Resurrected` is launched it connects to one of the two possible addresses for each region:
* Americas:
  * `137.221.106.88`
  * `137.221.106.188`
* Europe:
  * `37.244.28.80`
  * `37.244.28.180`
* Asia:
  * `117.52.35.79`
  * `117.52.35.179`

Whether this *subregion* has any significance is yet to be discovered. Some players report problems with joining games across lobbies (e.g. from `.79` to `.179`). Although some game IPs can be found regardless of it (e.g. `34.93.229.25` can be found from both `.79` and `.179`).

## How it works

The script in essence works the same way as `netstat`, [TCPView](https://docs.microsoft.com/en-us/sysinternals/downloads/tcpview) or `Resource Monitor` (a built-in Windows tool).
It asks your operating system what TCP connections are open by which processes using a standard Python library `psutil`. It does not require admin rights, inject or modify anything, or break TOS.

## Other software

If you don't care about creating logs, you may try:
* [TCPView](https://docs.microsoft.com/en-us/sysinternals/downloads/tcpview) -  for more detailed overview of your system's TCP connections
* [D2R-IPTool](https://github.com/VideoGameRoulette/D2RTools) - for an in-game D2R overlay display of your IP, aimed to help in DClone hunting

## Thanks

Thanks to [nocawy](https://github.com/nocawy) for the original version of the [script](https://github.com/nocawy/D2R-IP-logger).

## License

[MIT License](/LICENSE).
