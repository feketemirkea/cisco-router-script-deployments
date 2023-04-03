from netmiko import ConnectHandler

switch1 = {
    "device_type":"cisco_ios",
    "host":"192.168.122.111",
    "username":"admin",
    "password":"cisco123"
}

sesiune = ConnectHandler(**switch1)




for i in range(11, 19):
    print("Crearea vlan-ului {} a fost cu succes".format(i))
    lista = ["vlan " + str(i),"name Vlan_" + str(i)]
    iesire = sesiune.send_config_set(lista)
    print(iesire)


output = sesiune.send_command('show vlan brief')
print(output)