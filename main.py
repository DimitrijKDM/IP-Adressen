import os


class IPAddress:
    def __init__(self, ip_address_section_a, ip_address_section_b, ip_address_section_c, ip_address_section_d,
                 whole_ip_address):
        self.whole_ip_address = whole_ip_address
        self.ip_address_sectionD = ip_address_section_d
        self.ip_address_sectionC = ip_address_section_c
        self.ip_address_sectionB = ip_address_section_b
        self.ip_address_sectionA = ip_address_section_a


class IPAddressDecimal:
    def __init__(self, whole_ip_address_decimal, ip_address_decimal_a, ip_address_decimal_b, ip_address_decimal_c,
                 ip_address_decimal_d, ip_address_decimal_readable):
        self.ip_address_decimal_readable = ip_address_decimal_readable
        self.ip_address_decimal_d = ip_address_decimal_d
        self.ip_address_decimal_c = ip_address_decimal_c
        self.ip_address_decimal_b = ip_address_decimal_b
        self.ip_address_decimal_a = ip_address_decimal_a
        self.whole_ip_address_decimal = whole_ip_address_decimal


class IPAddress32:
    def __init__(self, ip_address_decimal_a_8d, ip_address_decimal_b_8d, ip_address_decimal_c_8d,
                 ip_address_decimal_d_8d, whole_ip_address_decimal_32):
        self.whole_ip_address_decimal_32 = whole_ip_address_decimal_32
        self.ip_address_decimal_d_8d = ip_address_decimal_d_8d
        self.ip_address_decimal_c_8d = ip_address_decimal_c_8d
        self.ip_address_decimal_b_8d = ip_address_decimal_b_8d
        self.ip_address_decimal_a_8d = ip_address_decimal_a_8d


class IPIDs:
    def __init__(self, net_id, host_id, host_portion):
        self.host_portion = host_portion
        self.host_id = host_id
        self.net_id = net_id


class IPIDeeznutsDecimal:
    def __init__(self, host_id_decimal, net_id_decimal):
        self.net_id_decimal = net_id_decimal
        self.host_id_decimal = host_id_decimal


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
            if netprefix > 24:
                print("Only numbers from 8-24!")
            elif netprefix < 8:
                print("Only numbers from 8-24!")
            else:
                break
        except ValueError:
            print("Invalid Value")
    return netprefix


def define_ids(netprefix, ip_address):
    net_id = (ip_address.whole_ip_address[netprefix:])
    host_id = (ip_address.whole_ip_address[:netprefix])
    host_portion = pow(2, (32 - netprefix)) - 2
    ip_ids = IPIDs(net_id, host_id, host_portion)
    return ip_ids


def convert_binary_to_decimal(ip_address_decimal_32, netprefix):
    print(ip_address_decimal_32.whole_ip_address_decimal_32)
    net_id_decimal = ip_address_decimal_32.whole_ip_address_decimal_32[:netprefix]
    net_id_decimal = net_id_decimal.replace("0", "")

    host_id_decimal = ip_address_decimal_32.whole_ip_address_decimal_32[netprefix:]
    host_id_decimal = host_id_decimal.replace("0", "")
    ip_ids_decimals = IPIDeeznutsDecimal(net_id_decimal, host_id_decimal)
    return ip_ids_decimals


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
    ip_address_decimal_readable = f"{ip_address_decimal_a}.{ip_address_decimal_b}.{ip_address_decimal_c}." \
                                  f"{ip_address_decimal_d}"
    whole_ip_address_decimal = ip_address_decimal_a + ip_address_decimal_b + ip_address_decimal_c + ip_address_decimal_d
    ip_address_decimal = IPAddressDecimal(whole_ip_address_decimal, ip_address_decimal_a, ip_address_decimal_b,
                                          ip_address_decimal_c, ip_address_decimal_d, ip_address_decimal_readable)
    return ip_address_decimal


def ip_address_sections_always_eight_digits(ip_address_decimal):
    ip_address_decimal_a_8d = str(ip_address_decimal.ip_address_decimal_a).zfill(8)
    ip_address_decimal_b_8d = str(ip_address_decimal.ip_address_decimal_b).zfill(8)
    ip_address_decimal_c_8d = str(ip_address_decimal.ip_address_decimal_c).zfill(8)
    ip_address_decimal_d_8d = str(ip_address_decimal.ip_address_decimal_d).zfill(8)
    whole_ip_address_decimal_32 = f"{ip_address_decimal_a_8d}.{ip_address_decimal_b_8d}.{ip_address_decimal_c_8d}." \
                                  f"{ip_address_decimal_d_8d}"

    ip_address_decimal_32 = IPAddress32(whole_ip_address_decimal_32, ip_address_decimal_b_8d, ip_address_decimal_c_8d,
                                        ip_address_decimal_d_8d, ip_address_decimal_a_8d)
    return ip_address_decimal_32


def main():
    ip_address = define_ips()
    netprefix = ask_netprefix()
    ip_ids = define_ids(netprefix, ip_address)
    ip_address_decimal = convert_ip_address_to_decimal(ip_address)
    ip_address_decimal_32 = ip_address_sections_always_eight_digits(ip_address_decimal)
    ip_ids_decimals = convert_binary_to_decimal(ip_address_decimal_32, netprefix)
    print(f"IPv4: {ip_address_decimal.ip_address_decimal_readable}")
    print(f"Net-ID: {ip_ids_decimals.net_id_decimal}")
    print(f"Host-ID: {ip_ids_decimals.host_id_decimal}")
    print(f"Host Portion: {ip_ids.host_portion}")


if __name__ == '__main__':
    main()

# todo: fix the Display of Net- Host-ID
