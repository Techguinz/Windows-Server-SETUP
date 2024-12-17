#x is starting point for ip
x = 146
#z is variable to how many batch files to create
z = 1

for i in range (0, z):
    if (x == 255):
        break
    x = x + 1
    y = "192.168.221." + str(x)
    f = open("ADHCP" + str(x) + ".bat", "w")
    f.write("@echo off\necho Running command 1\n" + 
            "netsh interface ipv4 set address name=\"Ethernet0\" static " +  
            y + " 255.255.255.0 192.168.221.2\necho Done\necho Running " + 
            "command 2\nnetsh interface ipv4 set dns name=\"Ethernet0\" static " + 
            "192.168.221.145\necho Done")
    f.close()
    filename = "ADHCP" + str(x) + ".bat"
    print(filename + " created successfully.")
