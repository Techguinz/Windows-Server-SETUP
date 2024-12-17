import csv

with open('testcsv.csv', 'r', encoding='utf-8-sig') as file:
    csv_reader = csv.reader(file)
    data = []
    for row in csv_reader:
        data.append(row)
#print(data) 
for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "" or data[i][j] is None:
                data[i][j] = "USER"
usernames = []
for d in data:
    temp = d[0][0].lower() + d[1].lower()
    usernames.append(temp)
    
#print(usernames)

onedarray = [item for sublist in data for item in sublist]
#print(onedarray)
for i in range(len(onedarray)):
    if onedarray[i] == "":
        onedarray[i] = "USER"

len_array1 = len(onedarray)
len_array2 = len(usernames)
testarray = []

for i in range(0, len_array1, 2):
    testarray.extend(onedarray[i:i+2])
    if usernames:
        testarray.append(usernames.pop(0))
testarray.extend(usernames)
  
powershelltemplate = """
$Attributes = @firstbracket
    Enabled = $true
    ChangePasswordAtLogon = $true

    UserPrincipalName = "{UserPrincipalName}"
    Name = "{Name}"
    GivenName = "{GivenName}"
    Surname = "{Surname}"
    DisplayName = "{DisplayName}"
    Description = "This is an account."
    Office = "None."

    Company = "finalproject.com"
    Department = "IT"
    Title = "IT Master"
    City = "Macon"
    State = "Georgia"

    AccountPassword = "p@ssword@1" | ConvertTo-SecureString -AsPlainText -Force
secondbracket

New-ADUser @Attributes

net localgroup Administrators /add finalproject\{Name}
"""

MasterSc = []
x = 1
while len(testarray) != 0:    
    Gname = testarray[0]
    testarray.pop(0)
    Sname = testarray[0]
    testarray.pop(0)
    Fname = testarray[0]
    testarray.pop(0)
    email = Fname + "@finalproject.com"
    Dname = Gname + " " + Sname
    #print(Gname + " " + Sname + " " + Fname + " " + email + " " + Dname)
    powershell = powershelltemplate.format(
        UserPrincipalName = email,
        Name = Fname,
        GivenName = Gname,
        Surname = Sname,
        DisplayName = Dname
    )
    finPS = powershell.replace("firstbracket", "{").replace("secondbracket", "}")
    MasterSc.append(finPS)
    #print(finPS)

script = "".join(MasterSc)
#print(script)
f = open("UserScript.ps1", "w")
f.write(script)
f.close()
print("User Script Created.")
