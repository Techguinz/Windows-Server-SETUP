This is set to take place in a Windows Server VM. (Follow Order)
1. First run "ServerIPv4 assigner" as it will set the Server IPv4 and DNS address
2. Next, "RolesandForestCreation" will add Active Directory and DNS Server to the hosted server. After, a domain will be created.
3. "SampleUserCreaiton" occupies the newly created user on the domain
These next steps can occur on any node in the network:
   Info: To allow for quick upscaling the python script "IPAssigner" is created. This script will create "z" amount of executable batch files. The idea of this script is that if the user wants to set the IP of lets say 30 nodes, they can set the "z" value to 30 and 30 batch files will be created. These can then be executed on a Windows Node where the IP settings will be allow for quick addition to the domain.
   1. Run "PythonInstaller". This PowerShell script installs Python 3.12 on the host allowing for python execution
   2. From CMD line run "IPAssigner". Here "z" amount of batch files will be created and saved to desktop for easy accessibility. These files can then be moved to the selected node.
After executing IPAssigner on external Windows node, they can then join the created domain through the credentials of either Administrator or created user. To see these navigate to the directory of the scripts and type "notepad PowerShell.ps1" to view credentials.
A server with active directory, dns, and a domain has now been automatically configured.
