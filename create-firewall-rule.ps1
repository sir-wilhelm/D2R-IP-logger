#Requires -RunAsAdministrator

if (Get-NetFirewallRule -DisplayName 'd2r: block global IPs') {
    return
}

New-NetFirewallRule -RemoteAddress "34.1.1.1-34.116.255.255","34.118.1.1-34.255.255.255","35.1.1.1-35.255.255.255" -DisplayName "d2r: block global IPs" -Direction outbound -Profile Any -Action Block
