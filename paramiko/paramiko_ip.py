import paramiko
import time
import os.path
import sys

n=input("Introduceti un fisier ce contine ip-uri: ")

if os.path.isfile(n):
    print("fisier valid")
else:
    print("fisierul nu exista, va rugam sa introduceti un fisier existent")
    sys.exit()

with open(n) as a:
    lista_ip=a.read().splitlines()
    print(lista_ip)

for i in lista_ip:


    HOST = i
    user ="admin"
    passord ="cisco123"

    sesiune=paramiko.SSHClient()

    sesiune.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sesiune.connect(hostname=HOST, username=user, password=passord)
    print(" ================Conectarea la {} a avut loc cu succes================= " .format(HOST))

    conex=sesiune.invoke_shell()
    conex.send(b"conf t\n")

    for i in range(2,10):
        print("crearea vlanului {} a fost cu succes " .format(i))
        conex.send(b"vlan "+ str(i).encode("ascii")+ b"\n" )
        conex.send(b"name vlan " + str(i).encode("ascii") + b"\n")
        time.sleep(1)


    conex.send(b"end\n")
    time.sleep(1)
    conex.send(b"wr\n")
    conex.send(b"show vlan brief\n")
    time.sleep(1)
    conex.send(b"exit\n")

    output=conex.recv(65535)
    print(output)

    sesiune.close()