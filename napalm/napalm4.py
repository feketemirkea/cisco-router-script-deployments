from napalm import get_network_driver



driver = get_network_driver("ios")
echipament = driver("192.168.122.112", "admin", "cisco123")
echipament.open()



print("Conectare la 192.168.122.112")
echipament.load_merge_candidate(filename='ACL.cfg')
diferente = echipament.compare_config()



if len(diferente) > 0:
    print(diferente)
    echipament.commit_config()
else:
    print('Nu este nevoie de nici o schimbare pe echipament.')
    echipament.discard_config()



echipament.close()
