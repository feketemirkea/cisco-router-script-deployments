from napalm import get_network_driver
import json

lista_echipamente =["192.168.122.111", "192.168.122.112"]
def conectivitate_ip():
    while True:
        sursa = input("Introduceti echipamentul sursa:")

        if sursa == 'q':
            break

        elif sursa in lista_echipamente:
            driver = get_network_driver("ios")
            echipament = driver(sursa, "admin", "cisco123")
            echipament.open()
            ping=input("Introdu un ip pentru ping: ")
            if ping in lista_echipamente:
                rezultat_ping = echipament.ping(ping)
                return json.dumps(rezultat_ping, indent=4)
            else:
                print("Destinatia nu este valida")
                break
            echipament.close()

        else:
            print("Nu este un ip valid")

            output = conectivitate_ip()
            print(output)

conectivitate_ip()