#Requires -RunAsAdministrator

if (Get-NetFirewallRule -DisplayName 'd2r: block global IPs') {
    Write-Host "reset firewall rule defaults"
    Set-NetFirewallRule -DisplayName "d2r: block global IPs" -RemoteAddress "34.1.1.1-34.116.255.255","34.118.1.1-34.255.255.255","35.1.1.1-35.255.255.255" -Direction Outbound -Profile Any -Action Block
    return
}

New-NetFirewallRule -DisplayName "d2r: block global IPs" -RemoteAddress "34.1.1.1-34.116.255.255","34.118.1.1-34.255.255.255","35.1.1.1-35.255.255.255" -Direction Outbound -Profile Any -Action Block
