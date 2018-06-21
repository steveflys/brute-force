from socket import *
from datetime import datetime
import sys, time

"""host address, start and stop port.  These can be changed as needed."""
host = ''
max_port = 8000
min_port = 1

def scan_host(host, port, r_code=1):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        code = s,connect_ex((host, port))

        if code == 0:
            r_code = code
        s.close()
    except Exception, e:
        pass

    return r_code

"""Ask the user for the target address, either URL or IP. Also give the user the option to stop the program with (Ctrl + C)."""
try:
    host = raw_input("[*] Enter target address: ")
except KeyboardInturupt:
    print("\n\n[*] user requested an inturupt.")
    print("[*] app shutting down.")
    sys.exit(1)

hostip = gethostbyname(host)
print("\n[*] Host: %s IP: %s" % (host, host_ip))
print("[*] Scanning started at %s...\n" % (time.strftime("%H:%M:%S")))
start_time = datetime.now()

for port in range(min_port, max_port):
    try:
        response = sacn_host(host, port)

        if response == 0:
            print("[*] Port %d: Open" % (port))
    
    except Exception, e:
        pass

stop_time = datetime.now()
elapsed_time = stop_time - start_time
print("\n[*] Scanning Finished at %s ..." % time.strftime("%H:%M:%S")))
print("[*] Scan durration: %s ..." (elapsed_time))