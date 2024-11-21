`Rename-LocalUser -Name "vboxuser" -NewName "Alice"`: modify the name of a user

It's possible the "FullName" hasn't been modified accordingly

--> use `Set-LocalUser -Name "Alice" -FullName "Alice"` to modify FullName as well

`Get-LocalUser`: display all users

`Add-LocalGroupMember -Group "Administrators" -Member "Alice"`: give administrative rights to a user

