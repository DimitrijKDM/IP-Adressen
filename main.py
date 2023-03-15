import os
# Define 4 bytes
byte_array1 = os.urandom(1)
byte_array2 = os.urandom(1)
byte_array3 = os.urandom(1)
byte_array4 = os.urandom(1)
# Define ip-address sections
ip_address_sectionA = ''.join(format(byte, '08b') for byte in byte_array1)
ip_address_sectionB = ''.join(format(byte, '08b') for byte in byte_array2)
ip_address_sectionC = ''.join(format(byte, '08b') for byte in byte_array3)
ip_address_sectionD = ''.join(format(byte, '08b') for byte in byte_array4)

print(f"IP Address: {ip_address_sectionA}")
print(f"IP Address: {ip_address_sectionB}")
print(f"IP Address: {ip_address_sectionC}")
print(f"IP Address: {ip_address_sectionD}")

ip_address_for_print = f"{ip_address_sectionA}.{ip_address_sectionB}.{ip_address_sectionC}.{ip_address_sectionD}"
ip_address = ip_address_sectionA + ip_address_sectionB + ip_address_sectionC + ip_address_sectionD

print(ip_address_for_print)
# Netprefix query
while True:
    try:
        netprefix = int(input("Netprefix\n> "))
        if netprefix > 31:
            print("Only numbers from 1-31!")
        elif netprefix < 1:
            print("Only numbers from 1-31!")
        else:
            break
    except ValueError:
        print("Invalid Value")
# Define id's
net_id = (ip_address[:netprefix])
host_id = (ip_address[netprefix:])
net_id_for_print = ""
if int(net_id) > 24:
    net_id_for_print = f"{net_id[:8]}.{net_id[8:16]}.{net_id[16:24]}.{net_id[24:]}"
elif 16 < int(net_id) <= 24:
    net_id_for_print = f"{net_id[:8]}.{net_id[8:16]}.{net_id[16:]}"
elif 16 >= int(net_id) > 8:
    net_id_for_print = f"{net_id[:8]}.{net_id[8:]}"
elif 0 < int(net_id) == 8:
    net_id_for_print = f"{net_id[:]}"
print(f"Net-ID: {net_id_for_print.rstrip('.')}")
print(f"Host-ID: {host_id}")
host_portion = pow(2, (32 - netprefix)) - 2
print(f"Host_Portion: {host_portion}")
# todo: Umwandeln von binärer ip-adresse zu dezimalzahl
