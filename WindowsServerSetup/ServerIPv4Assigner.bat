@echo off
echo Running command 1
netsh interface ipv4 set address name="Ethernet0" static 192.168.221.145 255.255.255.0 192.168.221.2
echo Done

echo Running command 2
netsh interface ipv4 set dns name="Ethernet0" static 192.168.221.145
echo Done

echo Running command 3
net user Administrator password@1
echo Done

echo Running command 4
wmic computersystem where caption='%computername%' rename FinalServer
echo Done

shutdown /r