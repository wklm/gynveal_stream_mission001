import hashlib


def proof(word1, word2):
    w1 = hashlib.md5()
    w1.update(word1)

    w2 = hashlib.md5()
    w2.update(word2)

    w1_hex = w1.hexdigest()
    w2_hex = w2.hexdigest()

    w1_bin = bin(int(w1_hex, 16))[2:]
    w2_bin = bin(int(w2_hex, 16))[2:]

    hex_xor = hex(int(w1_bin, 2) ^ int(w2_bin, 2))[2:-1]

    return hex_xor == '76fb930fd0dbc6cba6cf5bd85005a92a'


def main():
    print(proof('virology', 'ambrosia'))


if __name__ == '__main__':
    main()
