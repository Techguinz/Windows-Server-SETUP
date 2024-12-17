# Windows-Server-SETUP

Setting Up a Windows Server VM with Active Directory and Domain Configuration
Step 1: Assign Server IPv4 Address and DNS Settings

Run the script "ServerIPv4 assigner".
This script will configure the server’s IPv4 address and set the DNS settings.
Step 2: Add Active Directory and DNS Server Roles

Execute "RolesandForestCreation".
This step will install Active Directory and DNS Server roles on the server.
It will also create a new domain.
Step 3: Create a Sample User on the Domain

Run "SampleUserCreation".
This script will create a sample user on the newly configured domain.
Scaling the Network (To Be Performed on Any Node)
Step 4: Install Python for Script Execution

Run the PowerShell script "PythonInstaller" on the host machine.
This will install Python 3.12, enabling the execution of Python scripts.
Step 5: Generate Batch Files for Node Configuration

Open the Command Prompt and run the Python script "IPAssigner".
Specify the desired number of nodes by setting the variable z.
The script will generate z batch files, each preconfigured to set up the IP settings for a node.
The batch files will be saved to the desktop for easy access.
Step 6: Configure Additional Nodes

Move the generated batch files to the desired nodes.
Execute the appropriate batch file on each node to configure its IP settings.
Step 7: Join Nodes to the Domain

After running the batch files, join each node to the domain using either the Administrator credentials or the sample user credentials created earlier.
To view these credentials, navigate to the directory containing the scripts and open "PowerShell.ps1" using Notepad:
