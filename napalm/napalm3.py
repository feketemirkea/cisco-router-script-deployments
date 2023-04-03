from napalm import get_network_driver
import json

driver = get_network_driver("ios")


lista_ip= ["192.168.122.111", "192.168.122.112"]
for i in lista_ip:
    print("======================== {} ========================".format(i))
    echipament = driver(hostname=i, username="admin", password="cisco123")
    echipament.open()



    output = echipament.get_facts()
    print(output)
    print(json.dumps(output, indent=4))
    with open('fisier_config_' + i, 'w') as f:
        f.write(json.dumps(output, indent=4))

    echipament.close()