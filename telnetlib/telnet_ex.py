import telnetlib
import time

def ex1():
    HOST = "192.168.122.111"
    user = "admin"
    password = "cisco123"
    tn = telnetlib.Telnet(HOST)
    tn.write(user.encode('ascii') + b"\n")
    tn.write(password.encode('ascii') + b"\n")
    tn.write(b"show users\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))

def ex2():
    tn = telnetlib.Telnet('192.168.122.111')
    tn.read_until(b'Username: ')
    tn.write(b'admin\n')
    tn.read_until(b'Password: ')
    tn.write(b'cisco123\n')
    tn.write('terminal length 0\n'.encode())
    tn.write(b'show ip int brief\n')
    tn.write(b'exit\n')
    time.sleep(1)
    output = tn.read_all().decode('ascii')
    print(output)

def ex3():
    tn = telnetlib.Telnet('192.168.122.111')
    tn.read_until(b'Username: ')
    tn.write(b'admin\n')
    tn.read_until(b'Password: ')
    tn.write(b'cisco123\n')
    tn.write(b'terminal length 0\n')
    tn.write(b'show ip int brief\n')
    tn.write(b'exit\n')
    time.sleep(1)
    output = tn.read_all().decode()
    print(output)

def ex4():
    comenzi = ['conf t','vlan 10','name vlan_10','end','show vlan brief']
    tn = telnetlib.Telnet('192.168.122.111')
    tn.read_until(b'Username: ')
    tn.write(b'admin\n')
    tn.read_until(b'Password: ')
    tn.write(b'cisco123\n')
    tn.write(b"terminal length 0\n")
    for c in comenzi:
        tn.write(c.encode('ascii')+b'\n')
        time.sleep(1)
    tn.write(b'exit\n')
    tn.write(b'show exit\n')
    time.sleep(1)
    output = tn.read_until(b'Invalid').decode('ascii')
    print(output)

def ex5():
    echip = input('IP: ')
    tn = telnetlib.Telnet(echip)
    tn.read_until(b'Username: ')
    tn.write(b'admin\n')
    tn.read_until(b'Password: ')
    tn.write(b'cisco123\n')
    tn.write(b'conf t\n')
    tn.write(b'hostname SW1\n')
    tn.write(b'crypto key generate rsa mod 1024\n')
    tn.write(b'username admin secret cisco123\n')
    tn.write(b'line vty 0 15\n')
    tn.write(b'transport input all\n')
    tn.write(b'login local\n')
    tn.write(b'end\n')
    tn.write(b'exit\n')
    time.sleep(1)
    output = tn.read_all().decode()
    print(output)

ex5()