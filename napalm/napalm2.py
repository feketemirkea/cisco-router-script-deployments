from napalm import get_network_driver
import json

def ex1():
    driver = get_network_driver("ios")
    echipament = driver("192.168.122.111", "admin", "cisco123")

    echipament.open()
    output = echipament.get_arp_table()

    print(output)
    print(json.dumps(output,indent=4))
    echipament.close()


def ex2():
    driver = get_network_driver("ios")
    echipament = driver("192.168.122.111", "admin", "cisco123")
    echipament.open()
    tabela_arp = echipament.get_arp_table()
    print(tabela_arp)
    print(json.dumps(tabela_arp, indent=4))
    echipament.close()


def ex3():
    driver = get_network_driver("ios")
    echipament = driver("192.168.122.111", "admin", "cisco123")
    echipament.open()
    tabela_mac = echipament.get_mac_address_table()
    print(tabela_mac)
    print(json.dumps(tabela_mac, indent=4))
    echipament.close()


def ex4():
    driver = get_network_driver("ios")
    echipament = driver("192.168.122.111", "admin", "cisco123")
    echipament.open()
    interfaces = echipament.get_interfaces()
    print(interfaces)
    print(json.dumps(interfaces, indent=4))
    echipament.close()


def ex5():
    driver = get_network_driver("ios")
    echipament = driver("192.168.122.111", "admin", "cisco123")
    echipament.open()
    vlans = echipament.get_vlans()
    print(vlans)
    print(json.dumps(vlans, indent=4))
    echipament.close()


def ex6():

    driver = get_network_driver("ios")
    echipament = driver("192.168.122.111", "admin", "cisco123")
    echipament.open()
    vlans = echipament.get_vlans()
    print(vlans)
    print(json.dumps(vlans, indent=4))
    strdict=[vlans, echipament]
    f = open("fisier_config_sw.txt", "w")
    f.write(str(dict))
    """""
    with open(f'fisier_config_sw.txt', 'w') as f:
        f.write(vlans)
    """
    echipament.close()


ex6()