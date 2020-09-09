"""Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one."""


def ips_between(addr1, addr2):
    diffs = [int(b) - int(a) for a,b in zip(addr1.split('.'), addr2.split('.'))]
    sump = 0
    for d in diffs:
        sump *=256
        sump +=d
    return sump


from ipaddress import ip_address

def ips_between(start, end):
    return int(ip_address(end)) - int(ip_address(start))


assert ips_between("10.0.0.0", "10.0.0.50") == 50
assert ips_between("10.0.0.0", "10.0.1.0") == 256
assert ips_between("20.0.0.10", "20.0.1.0") == 246