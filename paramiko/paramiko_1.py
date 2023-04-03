import paramiko
import time

HOST = "192.168.122.112"
user = "admin"
password = "cisco123"

sesiune = paramiko.SSHClient()

sesiune.set_missing_host_key_policy(paramiko.AutoAddPolicy())

sesiune.connect(hostname=HOST, username=user, password=password)
print("Conectarea la {} a avut loc cu success!".format(HOST))

conex = sesiune.invoke_shell()
conex.send(b"conf t\n")

for i in range(2,10):
    conex.send(b"vlan " + str(i).encode("ascii") + b"\n")
    conex.send(b"name VLAN" + str(i).encode("ascii") + b"\n")
    time.sleep(1)
    conex.send(b"exit\n")
    time.sleep(1)

conex.send(b"end\n")
time.sleep(1)
conex.send(b"wr\n")
time.sleep(1)
conex.send(b"show vlan brief\n")
time.sleep(1)
conex.send(b"exit\n")

output = conex.recv(65535)
print(output.decode())

sesiune.close()