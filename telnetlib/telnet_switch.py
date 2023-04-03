import getpass
import telnetlib

HOST = "192.168.122.111" # pe switch1
user = input("Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")

tn.write(b"vlan 10\n")
tn.write(b"name vlan10\n")
tn.write(b"exit\n")

tn.write(b"vlan 20\n")
tn.write(b"name vlan20\n")
tn.write(b"exit\n")

tn.write(b"vlan 30\n")
tn.write(b"name vlan30\n")
tn.write(b"exit\n")

"""
list = ["vlan 2","vlan 3","vlan 4","vlan 5","vlan 6","vlan 7","vlan 8","vlan 9"]
for i in list:
    tn.write(i.encode("ascii")+b"\n")
    tn.write(b"exit\n")
"""
for i in range(2,10):
    tn.write(b"vlan " + str(i).encode("ascii") + b"\n")
    tn.write(b"name vlan_" + str(i).encode("ascii") + b"\n")
    tn.write(b"exit\n")

tn.write(b"do show vlan brief\n")

tn.write(b"end\n") # SW1(config)#exit
tn.write(b"exit\n") # SW1#exit

print(tn.read_all().decode('ascii'))