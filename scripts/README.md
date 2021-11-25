[firewall-scripts.zip](zip) contains PowerShell scripts that can create/enable/disable a firewall rule that is commonly used to block unwanted IPs during a hunt. They have to be run in an Administrative PowerShell window.

You can run the scripts by typing:
```
PS > .\create-firewall-rule.ps1 # only run once
PS > .\enable-firewall-rule.ps1
PS > .\disable-firewall-rule.ps1
```
or just copy/paste the command into an Administrative prompt:
```PowerShell
#only run the New command once
New-NetFirewallRule -RemoteAddress "34.1.1.1-34.116.255.255","34.118.1.1-34.255.255.255","35.1.1.1-35.255.255.255" -DisplayName "d2r: block global IPs" -Direction outbound -Profile Any -Action Block

Enable-NetFirewallRule -DisplayName "d2r: block global IPs"
Disable-NetFirewallRule -DisplayName "d2r: block global IPs"
```

[zip]: https://github.com/sir-wilhelm/D2R-IP-logger/releases/latest/download/firewall-scripts.zip
