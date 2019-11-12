from test_framework import generic_test

def second(s):
    results, ip = [], [0] * 4

    def get_numbers(s, rank):
        if rank == 3:
            if s.startswith('0') and len(s) > 1: return
            if 0 <= int(s) <= 255:
                ip[rank] = s
                results.append('.'.join(ip))
        else:
            if s.startswith('0'):
                if len(s) > 1:
                    ip[rank] = '0'
                    get_numbers(s[1:], rank + 1)
            else:
                for i in range(3):
                    if 0 < int(s[:i+1]) <= 255 and i + 1 < len(s):
                        ip[rank] = s[:i+1]
                        get_numbers(s[i+1:], rank + 1)

    if s:
        get_numbers(s, 0)
    
    return results


# IPv4 address has a size 32 bits, in its dot-decimal notation, which consisting
# of 4 decimal numbers, each range from 1 - 255 (8 bits of the address)
def first(s):
    results = []
    ip_list = [0] * 4

    def get_numbers(s, count):
        if count == 3:
            if s.startswith('0') and len(s) > 1:
                return
            if 0 <= int(s) <= 255:
                ip_list[count] = s
                results.append('.'.join(ip_list))
        else:
            if s[0] == '0':
                if len(s) > 1:
                    ip_list[count] = s[0]
                    get_numbers(s[1:], count + 1)
            else:
                for i in range(3):
                    if 0 < int(s[:i+1]) <= 255 and i + 1 < len(s):
                        ip_list[count] = s[:i+1]
                        get_numbers(s[i+1:], count + 1)

    if s:
        get_numbers(s, 0)

    return results

def get_valid_ip_address(s):
    # return first(s)
    return second(s)


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "valid_ip_addresses.py",
            'valid_ip_addresses.tsv',
            get_valid_ip_address,
            comparator=comp))
