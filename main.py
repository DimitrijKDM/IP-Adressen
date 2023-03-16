import os

# Global variables
global ip_address
global netprefix
global ip_address_sectionA
global ip_address_sectionB
global ip_address_sectionC
global ip_address_sectionD

# Define 4 bytes
byte_array1 = os.urandom(1)
byte_array2 = os.urandom(1)
byte_array3 = os.urandom(1)
byte_array4 = os.urandom(1)


def define_ips():
    global ip_address
    global ip_address_sectionA
    global ip_address_sectionB
    global ip_address_sectionC
    global ip_address_sectionD

    ip_address_sectionA = ''.join(format(byte, '08b') for byte in byte_array1)
    ip_address_sectionB = ''.join(format(byte, '08b') for byte in byte_array2)
    ip_address_sectionC = ''.join(format(byte, '08b') for byte in byte_array3)
    ip_address_sectionD = ''.join(format(byte, '08b') for byte in byte_array4)
    print(f"IP Address Section A: {ip_address_sectionA}")
    print(f"IP Address Section B: {ip_address_sectionB}")
    print(f"IP Address Section C: {ip_address_sectionC}")
    print(f"IP Address Section D: {ip_address_sectionD}")
    ip_address_for_print = f"{ip_address_sectionA}.{ip_address_sectionB}.{ip_address_sectionC}.{ip_address_sectionD}"
    ip_address = ip_address_sectionA + ip_address_sectionB + ip_address_sectionC + ip_address_sectionD
    print(f"IP Address Full: {ip_address_for_print}")


define_ips()


def ask_netprefix():
    global netprefix
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


ask_netprefix()


def define_ids():
    net_id = (ip_address[:netprefix])
    host_id = (ip_address[netprefix:])
    net_id_for_reading(net_id)
    print(f"Host-ID: {host_id}")
    host_portion = pow(2, (32 - netprefix)) - 2
    print(f"Host_Portion: {host_portion:_}")


def net_id_for_reading(net_id):
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


define_ids()


def convert_binary_to_decimal():
    ip_address_decimal_a = 0
    for digit in ip_address_sectionA:
        ip_address_decimal_a = ip_address_decimal_a * 2 + int(digit)

    ip_address_decimal_b = 0
    for digit in ip_address_sectionB:
        ip_address_decimal_b = ip_address_decimal_b * 2 + int(digit)

    ip_address_decimal_c = 0
    for digit in ip_address_sectionC:
        ip_address_decimal_c = ip_address_decimal_c * 2 + int(digit)

    ip_address_decimal_d = 0
    for digit in ip_address_sectionD:
        ip_address_decimal_d = ip_address_decimal_d * 2 + int(digit)

    ip_address_decimal = f"{ip_address_decimal_a}.{ip_address_decimal_b}.{ip_address_decimal_c}.{ip_address_decimal_d}"
    print(f"IPv6: {ip_address_decimal}")


convert_binary_to_decimal()
