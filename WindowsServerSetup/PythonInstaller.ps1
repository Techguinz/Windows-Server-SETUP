Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe" -OutFile "python-3.10.2-amd64.exe"

.\python-3.10.2-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine")+";"+[System.Environment]::GetEnvironmentVariable("Path","User")

#cd .\Desktop\

Write-Output "Python Installed."