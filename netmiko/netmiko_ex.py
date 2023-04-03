from netmiko import ConnectHandler
import time
import getpass

def ex1():
    def tabela_arp(echip):
        cisco={
        'device_type': 'cisco_ios',
        'host': echip,
        'username': 'admin',
        'password': 'cisco123',
        }
        sesiune = ConnectHandler(**cisco)
        output = sesiune.send_command('show arp')
        print(output)

    lista_ip = ['192.168.122.111','192.168.122.112']
    for ip in lista_ip:
        tabela_arp(ip)

def ex2():
    fisier = open('secret.txt','r')
    conf = fisier.readline()
    fisier.close()
    conf = conf.split(":")
    cisco = {
        'device_type': 'cisco_ios',
        'host': conf[0],
        'username': conf[1],
        'password': conf[2],
    }
    sesiune = ConnectHandler(**cisco)
    output = sesiune.send_command('show arp')
    print(output)

def ex3():
    def send_command(echip):
        cisco={
        'device_type': 'cisco_ios',
        'host': echip,
        'username': 'admin',
        'password': 'cisco123',
        }
        sesiune = ConnectHandler(**cisco)
        output = sesiune.send_command('show ip interface brief')
        print(output)
        time.sleep(1)
        output = sesiune.send_command('show run')
        time.sleep(1)
        print(output)

    lista_ip = ['192.168.122.111','192.168.122.112']
    for ip in lista_ip:
        send_command(ip)

def ex4():
    def send_command(echip):
        password = getpass.getpass()
        cisco={
        'device_type': 'cisco_ios',
        'host': echip,
        'username': 'admin',
        'password': password,
        }
        sesiune = ConnectHandler(**cisco)
        output = sesiune.send_command('show ip interface brief')
        print(output)
        time.sleep(1)
        output = sesiune.send_command('show run')
        time.sleep(1)
        print(output)

    lista_ip = ['192.168.122.111','192.168.122.112']
    for ip in lista_ip:
        send_command(ip)

def ex5():
    comenzi = ['access-list 101 permit tcp any any eq 80','access-list 101 permit tcp any any eq 443','access-list 101 deny ip any any']
    cisco = {
        'device_type': 'cisco_ios',
        'host': '192.168.122.111',
        'username': 'admin',
        'password': 'cisco123',
    }
    sesiune = ConnectHandler(**cisco)
    output = sesiune.send_config_set(comenzi)
    print(output)

def ex6():
    def execute(echipament,comanda):
        cisco = {
            'device_type': echipament['device_type'],
            'host': echipament['host'],
            'username': echipament['username'],
            'password': echipament['password'],
        }
        sesiune = ConnectHandler(**cisco)
        output = sesiune.send_command(comanda)
        print(output)

    sw1 = {
        'device_type': 'cisco_ios',
        'host': '192.168.122.111',
        'username': 'admin',
        'password': 'cisco123',
    }

    sw2 = {
        'device_type': 'cisco_ios',
        'host': '192.168.122.112',
        'username': 'admin',
        'password': 'cisco123',
    }
    execute(sw1,'show ip interface brief')




