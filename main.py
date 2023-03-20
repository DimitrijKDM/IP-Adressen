import os

# Global variables
global ip_address
global netprefix
global ip_address_sectionA
global ip_address_sectionB
global ip_address_sectionC
global ip_address_sectionD
global ip_address_decimal
global net_id
global net_id_decimal
global net_id_for_print
global host_id
global host_portion

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
    ip_address = ip_address_sectionA + ip_address_sectionB + ip_address_sectionC + ip_address_sectionD


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


def define_ids():
    global net_id
    global host_id
    global host_portion
    net_id = (ip_address[:netprefix])
    host_id = (ip_address[netprefix:])
    net_id_for_reading()
    host_portion = pow(2, (32 - netprefix)) - 2


def net_id_for_reading():
    global net_id_for_print
    global net_id_decimal
    net_id_for_print = ""
    if int(net_id) > 24:
        net_id_for_print = f"{net_id[:8]}.{net_id[8:16]}.{net_id[16:24]}.{net_id[24:]}"
        # Split net_id into sections
        net_id1 = net_id[:8]
        net_id2 = net_id[8:2*8]
        net_id3 = net_id[2*8:3*8]
        net_id4 = net_id[3*8:]
        # Make net_id decimal
        net_id_decimal_a = 0
        for digit in net_id1:
            net_id_decimal_a = net_id_decimal_a * 2 + int(digit)
        net_id_decimal_b = 0
        for digit in net_id2:
            net_id_decimal_b = net_id_decimal_b * 2 + int(digit)
        net_id_decimal_c = 0
        for digit in net_id3:
            net_id_decimal_c = net_id_decimal_c * 2 + int(digit)
        net_id_decimal_d = 0
        for digit in net_id4:
            net_id_decimal_d = net_id_decimal_d * 2 + int(digit)
        net_id_decimal = f"{net_id_decimal_a}.{net_id_decimal_b}.{net_id_decimal_c}.{net_id_decimal_d}"
    elif 16 < int(net_id) <= 24:
        net_id_for_print = f"{net_id[:8]}.{net_id[8:16]}.{net_id[16:]}"
        net_id1 = net_id[:8]
        net_id2 = net_id[8:2 * 8]
        net_id3 = net_id[2 * 8:3 * 8]
        net_id_decimal_a = 0
        for digit in net_id1:
            net_id_decimal_a = net_id_decimal_a * 2 + int(digit)
        net_id_decimal_b = 0
        for digit in net_id2:
            net_id_decimal_b = net_id_decimal_b * 2 + int(digit)
        net_id_decimal_c = 0
        for digit in net_id3:
            net_id_decimal_c = net_id_decimal_c * 2 + int(digit)
        net_id_decimal = f"{net_id_decimal_a}.{net_id_decimal_b}.{net_id_decimal_c}"
    elif 16 >= int(net_id) > 8:
        net_id_for_print = f"{net_id[:8]}.{net_id[8:]}"
        net_id1 = net_id[:8]
        net_id2 = net_id[8:2 * 8]
        net_id_decimal_a = 0
        for digit in net_id1:
            net_id_decimal_a = net_id_decimal_a * 2 + int(digit)
        net_id_decimal_b = 0
        for digit in net_id2:
            net_id_decimal_b = net_id_decimal_b * 2 + int(digit)
        net_id_decimal = f"{net_id_decimal_a}.{net_id_decimal_b}"
    elif 0 < int(net_id) == 8:
        net_id_for_print = f"{net_id[:]}"
        net_id1 = net_id[:8]
        net_id_decimal_a = 0
        for digit in net_id1:
            net_id_decimal_a = net_id_decimal_a * 2 + int(digit)
        net_id_decimal = f"{net_id_decimal_a}"


def convert_binary_to_decimal():
    global ip_address_decimal
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


def main():
    define_ips()
    ask_netprefix()
    define_ids()
    convert_binary_to_decimal()
    print(f"IPv4-Adresse: {ip_address_decimal}")
    print(f"Net-ID: {net_id_decimal.rstrip('.')}")
    print(f"Host-ID: {host_id}")
    print(f"Host_Portion: {host_portion:_}")


if __name__ == '__main__':
    main()

# todo: In Dezimalzahlen umwandeln
