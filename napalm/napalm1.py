from napalm import get_network_driver
import json

driver = get_network_driver("ios")
echipament = driver("192.168.122.111", "admin", "cisco123")

echipament.open()
output = echipament.get_facts()
print(output)
print(json.dumps(output,indent=4))
echipament.close()
