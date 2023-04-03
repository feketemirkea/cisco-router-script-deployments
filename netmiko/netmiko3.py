from netmiko.ssh_exception import NetmikoTimeoutException
from netmiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import SSHException
from netmiko import ConnectHandler
import getpass

n = input("Dati user-ul: ")
m = getpass.getpass("Parola este: ")
with open("ip_file.txt") as fisier:
    lista_ip = fisier.read().splitlines()
with open("Comenzi.txt") as fisier:
    lista_comenzi = fisier.read().splitlines()

for i in lista_ip:
    switch = {
        "device_type": "cisco_ios",
        "host": i,
        "username": n,
        "password": m
    }
    # print(i)

    try:
        sesiune = ConnectHandler(**switch)
    except(AuthenticationException):
        print("Eroare la autentificare pe: " + i)
        continue
    except(NetmikoTimeoutException):
        print("Timeout la echipament: " + i)
        continue
    except(SSHException):
        print("Problema SSH. Sunteti sigur/a ca SSH este activat pe " + i)
        continue
    except Exception as eroare_necunoscuta:
        print("A aparut o eroare: " + str(eroare_necunoscuta) + " pe " + i)
        continue
    else:
        output1 = sesiune.send_config_set(lista_comenzi)
        print("Totul este in regula", output1)



