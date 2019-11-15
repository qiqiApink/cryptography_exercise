def padpkcs7(m, block_size):
    c = block_size - len(m) % block_size
    m += bytes([c] * c)
    return m

def main():
    m = b"YELLOW SUBMARINE"
    print(padpkcs7(m, 20))

if __name__ == '__main__':
    main()
