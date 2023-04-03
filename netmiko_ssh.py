from netmiko import ConnectHandler

fisier_cmd=input("Introduceti un fisier de comenzi")

switch1 = {
    "device_type":"cisco_ios",
    "host":"192.168.122.111",
    "username":"admin",
    "password":"cisco123"
}

switch2 = {
    "device_type":"cisco_ios",
    "host":"192.168.122.112",
    "username":"admin",
    "password":"cisco123"
}

lista_ipuri=[switch1, switch2]
with open(fisier_cmd) as fisier:
    lista_comenzi = fisier.read().splitlines()




for ip in lista_ipuri:
    sesiune = ConnectHandler(**ip)
    configurare=sesiune.send_config_set(lista_comenzi)
    print(configurare)


