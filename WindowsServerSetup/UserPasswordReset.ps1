#allows administrator to change their password not specified user

Set-ADAccountPassword -Identity fdanson

#makes user change their password on next log-in
Set-ADUser -Identity fdanson -ChangePasswordAtLogon $true

Write-Output "User's password has been reset for next log-in."