import subprocess
import re

result = subprocess.run(['netsh', 'interface', 'ipv4', 'show', 'config'], capture_output=True, text=True)

if result.returncode == 0:
    output = result.stdout
else:
    print("Error executing the command:", result.stderr)

pattern = r'Configuration for interface "(.*?)".*?DHCP enabled:'
matches = re.findall(pattern, output, re.DOTALL)

print("Which network adapter would you like to set as starting IP point?")
for match in matches:
    print(match.strip())

foutput = output.replace('"', '')
txt = foutput.split()
txtholder = []
txtholder = txt
x = input(":")

if x in txtholder:
    index = txtholder.index(x)
    separate_array = txtholder[index + 1: index + 50]
else:
    print("Word not found in the array")

separate_array.append("Gateway:")
address_index = separate_array.index('Address:')
address = separate_array[address_index + 1]

last_period_index = address.rfind(".")
if last_period_index != -1:
    result = address[:last_period_index]    
finaladdress = result
finaladdress = finaladdress + "."
result = result + ".2"
separate_array.append(result)

gateway_index = separate_array.index('Gateway:')
mask_index = separate_array.index('(mask')

gateway = separate_array[gateway_index + 1]
submask = separate_array[mask_index + 1]
submask = submask[:-1]
address2 = address[:-1]

print(address + " " + submask + " " + gateway)
dns = address

parts = address.split('.')
new_string = parts[-1]
last_integer = int(new_string)

x = last_integer + 1
z = int(input("How many batch files would you like to create? "))
for i in range (0, z):
    if (x == 255):
        break
    y = finaladdress + str(x)
    f = open("ADHCP" + str(x) + ".bat", "w")
    f.write("@echo off\necho Running command 1\n" + 
            "netsh interface ipv4 set address name='Ethernet0' static " +  
            y + " " + submask + " " + gateway + "\necho Done\necho Running " + 
            "command 2\nnetsh interface ipv4 set dns name='Ethernet0' static" + " " + dns +
            "\necho Done")
    f.close()
    filename = "ADHCP" + str(x) + ".bat"
    print(filename + " created successfully.")
    x = x + 1
