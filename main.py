import os


class IPAddress:
    def __init__(self, ip_address_section_a, ip_address_section_b, ip_address_section_c, ip_address_section_d,
                 whole_ip_address):
        self.whole_ip_address = whole_ip_address
        self.ip_address_sectionD = ip_address_section_d
        self.ip_address_sectionC = ip_address_section_c
        self.ip_address_sectionB = ip_address_section_b
        self.ip_address_sectionA = ip_address_section_a


def define_ips():
    byte_array1 = os.urandom(1)
    byte_array2 = os.urandom(1)
    byte_array3 = os.urandom(1)
    byte_array4 = os.urandom(1)
    ip_address_sectionA = ''.join(format(byte, '08b') for byte in byte_array1)
    ip_address_sectionB = ''.join(format(byte, '08b') for byte in byte_array2)
    ip_address_sectionC = ''.join(format(byte, '08b') for byte in byte_array3)
    ip_address_sectionD = ''.join(format(byte, '08b') for byte in byte_array4)
    whole_ip_address = ip_address_sectionA + ip_address_sectionB + ip_address_sectionC + ip_address_sectionD
    ip_address = IPAddress(ip_address_sectionA, ip_address_sectionB, ip_address_sectionC, ip_address_sectionD,
                           whole_ip_address)
    return ip_address


def ask_netprefix():
    while True:
        try:
            netprefix = int(input("Netprefix\n> "))
            if netprefix != 24 or netprefix != 8 or netprefix != 16:
                print("Only the numbers 8, 16 or 24!")
            else:
                break
        except ValueError:
            print("Invalid Value")
    return netprefix


class IPIDs:
    def __init__(self, net_id, host_id, net_id_readable, host_portion):
        self.host_portion = host_portion
        self.net_id_readable = net_id_readable
        self.host_id = host_id
        self.net_id = net_id
        self.host_id_decimal = None
        self.net_id_decimal = None


def define_ids(netprefix, ip_address):
    net_id = (ip_address.whole_ip_address[:netprefix])
    host_id = (ip_address.whole_ip_address[netprefix:])
    net_id_readable = net_id_for_reading(netprefix, net_id)
    host_portion = pow(2, (32 - netprefix)) - 2
    ip_ids = IPIDs(net_id, host_id, net_id_readable, host_portion)
    return ip_ids


def net_id_for_reading(netprefix, net_id):
    net_id_for_print = ""

    if 16 < netprefix <= 24:
        net_id_for_print = f"{net_id[:8]}.{net_id[8:16]}.{net_id[16:]}"
    elif 16 >= netprefix > 8:
        net_id_for_print = f"{net_id[:8]}.{net_id[8:]}"
    elif netprefix == 8:
        net_id_for_print = f"{net_id[:]}"
    return net_id_for_print


def convert_binary_net_id_decimal_16_24(net_id):
    # Define Net-ID Sections

    net_id1 = net_id[:8]
    net_id2 = net_id[8:16]
    net_id3 = net_id[16:24]

    # Convert Net-ID Sections into Decimal

    net_id_decimal_a = 0
    for digit in net_id1:
        net_id_decimal_a = net_id_decimal_a * 2 + int(digit)
    net_id_decimal_b = 0
    for digit in net_id2:
        net_id_decimal_b = net_id_decimal_b * 2 + int(digit)
    net_id_decimal_c = 0
    for digit in net_id3:
        net_id_decimal_c = net_id_decimal_c * 2 + int(digit)

    # Define Net-ID Decimal (Put Sections into one)

    net_id_decimal = f"{net_id_decimal_a}.{net_id_decimal_b}.{net_id_decimal_c}"
    return net_id_decimal


# Giga Chad Methode
def convert_binary_to_decimal(netprefix, ip_ids):
    net_id_decimal = 0
    host_id_decimal = 0

    if 16 < netprefix <= 24:
        net_id_decimal = convert_binary_net_id_decimal_16_24(ip_ids.net_id)
        host_id_decimal = convert_binary_to_decimal_host_id_16_24(ip_ids)

    elif 16 >= netprefix > 8:
        net_id_decimal = convert_net_id_to_decimal_16_8(ip_ids)
        host_id_decimal = convert_binary_host_id_decimal_16_8(ip_ids)

    elif netprefix == 8:
        net_id_decimal = convert_binary_to_decimal_net_id_8(ip_ids)
        host_id_decimal = convert_binary_to_decimal_host_id_8(ip_ids)
    ip_ids.host_id_decimal = host_id_decimal
    ip_ids.net_id_decimal = net_id_decimal
    return ip_ids


def convert_binary_to_decimal_host_id_8(ip_ids):
    host_id1 = ip_ids.net_id[24:]
    host_id2 = ip_ids.net_id[16:24]
    host_id3 = ip_ids.net_id[8:16]
    host_id_decimal_a = 0
    for digit in host_id1:
        host_id_decimal_a = host_id_decimal_a * 2 + int(digit)
    host_id_decimal_b = 0
    for digit in host_id2:
        host_id_decimal_b = host_id_decimal_b * 2 + int(digit)
    host_id_decimal_c = 0
    for digit in host_id3:
        host_id_decimal_c = host_id_decimal_c * 2 + int(digit)
    host_id_decimal = f"{host_id_decimal_a}.{host_id_decimal_b}.{host_id_decimal_c}"
    return host_id_decimal


def convert_binary_to_decimal_net_id_8(ip_ids):
    net_id1 = ip_ids.net_id[:8]
    net_id_decimal_a = 0
    for digit in net_id1:
        net_id_decimal_a = net_id_decimal_a * 2 + int(digit)
    net_id_decimal = f"{net_id_decimal_a}"
    return net_id_decimal


def convert_binary_host_id_decimal_16_8(ip_ids):
    host_id1 = ip_ids.net_id[24:]
    host_id2 = ip_ids.net_id[16:24]
    host_id_decimal_a = 0
    for digit in host_id1:
        host_id_decimal_a = host_id_decimal_a * 2 + int(digit)
    host_id_decimal_b = 0
    for digit in host_id2:
        host_id_decimal_b = host_id_decimal_b * 2 + int(digit)
    host_id_decimal = f"{host_id_decimal_a}.{host_id_decimal_b}"
    return host_id_decimal


def convert_binary_to_decimal_host_id_16_24(ip_ids):
    # Define Host-ID Sections
    host_id1 = ip_ids.net_id[24:]
    # Convert Host-ID Sections into Decimal
    host_id_decimal_a = 0
    for digit in host_id1:
        host_id_decimal_a = host_id_decimal_a * 2 + int(digit)
    # Put Sections into one
    host_id_decimal = f"{host_id_decimal_a}"
    return host_id_decimal


def convert_net_id_to_decimal_16_8(ip_ids):
    net_id1 = ip_ids.net_id[:8]
    net_id2 = ip_ids.net_id[8:16]
    net_id_decimal_a = 0
    for digit in net_id1:
        net_id_decimal_a = net_id_decimal_a * 2 + int(digit)
    net_id_decimal_b = 0
    for digit in net_id2:
        net_id_decimal_b = net_id_decimal_b * 2 + int(digit)
    net_id_decimal = f"{net_id_decimal_a}.{net_id_decimal_b}"
    return net_id_decimal


def convert_ip_address_to_decimal(ip_address):
    ip_address_decimal_a = 0
    # Convert Sections into Decimals
    for digit in ip_address.ip_address_sectionA:
        ip_address_decimal_a = ip_address_decimal_a * 2 + int(digit)
    ip_address_decimal_b = 0
    for digit in ip_address.ip_address_sectionB:
        ip_address_decimal_b = ip_address_decimal_b * 2 + int(digit)
    ip_address_decimal_c = 0
    for digit in ip_address.ip_address_sectionC:
        ip_address_decimal_c = ip_address_decimal_c * 2 + int(digit)
    ip_address_decimal_d = 0
    for digit in ip_address.ip_address_sectionD:
        ip_address_decimal_d = ip_address_decimal_d * 2 + int(digit)
    # Define Decimal IP Address (Put all Sections into one)
    ip_address_decimal = f"{ip_address_decimal_a}.{ip_address_decimal_b}.{ip_address_decimal_c}.{ip_address_decimal_d}"
    return ip_address_decimal


def main():
    ip_address = define_ips()
    netprefix = ask_netprefix()
    ip_ids = define_ids(netprefix, ip_address)
    ip_ids = convert_binary_to_decimal(netprefix, ip_ids)
    print(f"IPv4-Adresse: {convert_ip_address_to_decimal(ip_address)}")
    print(f"Net-ID: {ip_ids.net_id_readable.rstrip('.')}")
    print(f"Host-ID: {ip_ids.host_id}")
    print(f"Host_Portion: {ip_ids.host_portion:_}")
    print(f"Net-ID: {ip_ids.net_id_decimal.rstrip('.')}")
    print(f"Host-ID: {ip_ids.host_id_decimal.rstrip('.')}")


if __name__ == '__main__':
    main()

# todo: In Dezimalzahlen umwandeln
