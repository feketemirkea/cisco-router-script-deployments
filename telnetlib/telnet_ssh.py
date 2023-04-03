import getpass
import telnetlib

HOST = "192.168.122.112"
user = input("Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: " )

tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: " )
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")
tn.write(b"crypto key generate rsa mod 1024\n")
tn.write(b"line vty 0 15\n")
tn.write(b"transport input all\n")
tn.write(b"login local\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_until(b"Invalid input").decode('ascii'))
print(tn.read_all().decode('ascii'))