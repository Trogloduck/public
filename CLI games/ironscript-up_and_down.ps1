# Last shutdown
$shutdownTime = (Get-EventLog -LogName System -Source USER32 -EntryType Information | Where-Object { $_.EventID -eq 1074 } | Select-Object -First 1).TimeGenerated

# Last startup
$startupTime = (Get-EventLog -LogName System -Source EventLog -EntryType Information | Where-Object { $_.EventID -eq 6005 } | Select-Object -First 1).TimeGenerated

# Down time
$downTime = $startupTime - $shutdownTime

# Current uptime (how long the computer has been running)
$currentUptime = (Get-Date) - (gcim Win32_OperatingSystem).LastBootUpTime

# Computer name
$computerName = $env:COMPUTERNAME

# Name of user who initiated last shutdown
$shutdownUser = (Get-EventLog -LogName System -Source USER32 -EntryType Information | Where-Object { $_.EventID -eq 1074 } | Select-Object -First 1).ReplacementStrings[1]

# Output
Write-Host ""
Write-Host "Computer Name: $computerName"
Write-Host ""
Write-Host "Last Shutdown: $shutdownTime initiated by $shutdownUser"
Write-Host ""
Write-Host "Last Startup: $startupTime"
Write-Host ""
Write-Host "Downtime: $downTime"
Write-Host ""
Write-Host "Current Uptime: $currentUptime"
Write-Host ""