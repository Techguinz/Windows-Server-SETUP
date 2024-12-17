Import-Module ActiveDirectory

$Attributes = @{

   Enabled = $true
   ChangePasswordAtLogon = $true

   UserPrincipalName = "fdanson@finalproject.com"
   Name = "fdanson"
   GivenName = "Frida"
   Surname = "Danson"
   DisplayName = "Frida Danson"
   Description = "This is Frida's account."
   Office = "None."

   Company = "finalproject.com"
   Department = "IT"
   Title = "IT Master"
   City = "Macon"
   State = "Georgia"

   AccountPassword = "p@ssword@1" | ConvertTo-SecureString -AsPlainText -Force

}

New-ADUser @Attributes

net localgroup Administrators /add finalproject\fdanson