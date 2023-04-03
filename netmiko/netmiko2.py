from netmiko import ConnectHandler

#crearea listei de ip-uri
with open("fisier_ip.txt") as fisier :
    lista_ip= fisier.read().splitlines()

#crearea listei de comenzi
with open("comenzi_switch.txt") as fisier :
    lista_comenzi = fisier.read().splitlines()


for i in lista_ip :
    switch = {
        "device_type":"cisco_ios",
        "host":i,
        "username":"admin",
        "password":"cisco123"
    }

    sesiune = ConnectHandler(**switch)
    configurare = sesiune.send_config_set(lista_comenzi)

    #Varianta1
    for j in range(1,len(lista_ip)+1):
        with open(f"SW{j}_output.txt","w") as f:
            f.write(configurare)
    """"
    Varianta2
    with open(i + "_output.txt","w") as f:
        #f.write(configurare)
    """
    print(configurare)