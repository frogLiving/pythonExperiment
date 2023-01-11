import sys
import paramiko

# Variables
device  = ""
ip      = ""
user    = ""
passW   = ""
file    = ""
error   = False
argsLen = len(sys.argv)

def sshconnect(valueA):
    # Load paramiko
    connected = False
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Connect to remote device using DNS
        ssh.connect(valueA, username = user,   password = passW, look_for_keys = False)
        connected = True
    
    except Exception as error_message:
        print(error_message)
        
    return connected

def parseArgs(value):
    for x in range(1, argsLen,  2):
        
        match value[x]:            

            case "-h": 
                print("Welcome to QHC SSH tool\n")
                print("\t-h  Help switch")
                print("\t-u  Username")
                print("\t-u  Username")
                print("\t-p  Password")
                print("\t-d  Hostname")
                print("\t-ip IP address, can be used as a failover")
                print("\t-f  Filename to load a list of devices and IP\n")
                print("\nThe program is written in such a way it will use DNS first and failure over to Ip.")
                print("Do not use -h with an actual command.  -h terminates the program.\n")
                quit();
            
            case "-u":
                x += 1
                global user
                user = value[x]
                print("Your account is: ", user)
            
            case "-p":
                x += 1
                global passW
                passW  = value[x]
                print("Your password is: ", passW)
        
            case "-d":
                x += 1
                global device
                device = value[x]
                print("Hostname is: ", device),
            
            case "-ip":
                x += 1
                global ip
                ip = value[x]
                print("IP addy is: ", ip)
            
            case "-f":
                x += 1
                global file
                file = value[x]
                print("Filename: ", file)
                
            case unknown_command:
                print("Invalid switch: ", value[x])
                global error
                error = True
                

# Help Arg
if argsLen > 1:
    parseArgs(sys.argv)

    if len(user) == 0:
        print("Please use -u swtich to set a user account or -f to load a config file\n")
        quit()

    if len(passW) == 0:
        print("Please use -p switch to set a password or -f to load a config file\n")
        quit()
        
    if len(device) == 0 and len(ip) == 0:
        print("Hostname is: ", device)
        print("\nPlease use the -d switch to set a hostname or -f to load a config file")
        print("Switch -ip can be used to assign IP instead of dns.\n")
        quit()
        
    # Future home of loading the ini file
    
    # Try to connect
    if sshconnect(device) or sshconnect(ip):
        # Home of future commands
        stdin, stdout, stderr = client.exec_command('ls -l')
        
        # Close Conn
        ssh.close()
        
    else:
        print("Unable to connect via IP or DNS.  Please address and try again!")
    
