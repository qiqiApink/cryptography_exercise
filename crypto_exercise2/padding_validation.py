def unpad(s):
    i = s[-1]
    if i == bytes([0]) or s[-i:] != bytes([i] * i):
        raise ValueError('bad padding')
    return s[0:-i]

if __name__ == '__main__':
    print(unpad(b'ICE ICE BABY\x04\x04\x04\x04'))
    try:
        unpad(b'ICE ICE BABY\x05\x05\x05\x05')
    except ValueError as e:
        print(e)
    try:
        unpad(b'ICE ICE BABY\x01\x02\x03\x04')
    except ValueError as e:
        print(e)
    try:
        unpad(b'ICE ICE BABYYYYY\x00')
    except ValueError as e:
        print(e)
