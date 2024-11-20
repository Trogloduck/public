# Century game (underthewire.tech)
These are the solutions for each level of the pedagogic Powershell game found on the website https://underthewire.tech/

*On each line of this file is the password to connect to the next level using `ssh century[n° of the level]@century.underthewire.tech -p 22` and the command used to find that password*

0 --> 1: century1

1 --> 2: 10.0.14393.7254 `$PSVersionTable.BuildVersion`

2 --> 3: invoke-webrequest443

3 --> 4: 123 `(Get-ChildItem -Path . -File | Measure-Object).Count`

4 --> 5: 34182 `cd "path"`

5 --> 6: underthewire3347 `(Get-WmiObject -Class Win32_ComputerSystem).Domain` # the name of the domain is just the part before the dot

6 --> 7: 197 `(Get-ChildItem -Path . -Directory | Measure-Object).Count`

7 --> 8: 7points `Get-ChildItem -Path C:\ -Recurse -Filter "readme*" -ErrorAction SilentlyContinue`

8 --> 9: 696 `(Get-Content .\unique.txt | Sort-Object | Get-Unique).Count`

9 --> 10: pierid `(Get-Content .\Word_File.txt -Raw) -split '\s+' | Select-Object -Index 160`

10 --> 11: windowsupdates110 `(Get-WmiObject -Class Win32_Service -Filter "Name='wuauserv'").Description`

11 --> 12: secret_sauce `Get-ChildItem -Path . -Recurse -Hidden -File`

12 --> 13: i_authenticate_things `Get-ADDomainController -Identity "UTW" | Select-Object Name, Description` ; `get-adcomputer -properties description -filter 'Name -like "UTW"'`

13 --> 14: 755 `(Get-Content -Path .\countmywords | Out-String).Split(' ', [System.StringSplitOptions]::RemoveEmptyEntries).Count`

14 --> 15: 153 `(Get-Content .\countpolos -Raw).Split(' ') | Where-Object { $_ -eq 'polo' } | Measure-Object | Select-Object -ExpandProperty Count`