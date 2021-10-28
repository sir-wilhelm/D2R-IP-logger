# D2R-IP-logger

A python script that can display the IP of your online game in Diablo II Resurrected, log ip, timestamp and region (EU/NA/Asia) to a csv, and notify when a provided IP is found.

Useful for hunting Diablo Clone and data collection.

![](https://i.imgur.com/q59EWIL.png)

## How to install

A compiled version for Windows can be downloaded form the [Release Page](https://github.com/sir-wilhelm/D2R-IP-logger/releases), you can download it here:
[D2R_ip.exe](https://github.com/sir-wilhelm/D2R-IP-logger/releases/latest/download/D2R_ip.exe).

You can also run the
[D2R_ip.py](https://github.com/sir-wilhelm/D2R-IP-logger/raw/main/D2R_ip.py) script manually by following the steps below:
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
* Download [D2R_ip.py](https://raw.githubusercontent.com/sir-wilhelm/D2R-IP-logger/main/D2R_ip.py) file.

## How to use

On Windows you can either:
* double-click `D2R_ip.py` or `D2R_ip.exe` in File Explorer
* or open PowerShell (`Windows Key + r`, type `powershell`, press enter), navigate to the directory where you downloaded the file (i.e. type `cd C:\Users\YourUsername\Downloads\`) then type `python D2R_ip.py` or `py D2R_ip.py` or `D2R_ip.exe`.

To stop the program press CTRL+C or simply close the console window.

To hunt for a specific ip address:
* Run the application or script from PowerShell and add the IP after the command ex:
  * `python D2R_ip.py 4.20.66.69` or `py D2r_ip.py 4.20.66.69`
  * `D2R_ip.exe 4.20.66.69`

## Info

In the last line a clock is displayed, which will turn green after 1 minute since the last game creation (which is, as of now, the cooldown before the servers allow you to create a new game).

The logfiles appear in the same folder, with filenames `D2R_ip_*.log` where * is today's date.
If you don't want any logfiles created then modify the code, the instructions are in comments.

It also includes an IP/game counter.

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